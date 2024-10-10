from scenedetect import VideoManager, SceneManager
from scenedetect.detectors import ContentDetector
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

def detect_scenes(video_path):
    try:

        video_manager = VideoManager([video_path])
        scene_manager = SceneManager()


        scene_manager.add_detector(ContentDetector())

        # Start video manager to analyze the video
        video_manager.start()

        # Detect scenes
        scene_manager.detect_scenes(frame_source=video_manager)

        # List the start/end times of all scenes found
        scene_list = scene_manager.get_scene_list()
        print(f"Detected {len(scene_list)} scenes.")

        # Print out each scene's start and end time
        for i, scene in enumerate(scene_list):
            print(f"Scene {i+1}: Start {scene[0].get_timecode()} - End {scene[1].get_timecode()}")
        
        return scene_list

    except Exception as e:
        print(f"An error occurred during scene detection: {e}")
        return []

def create_shorts(video_path, scene_list, min_duration=15, max_duration=59):
    try:
        # Go through the detected scenes and create shorts
        for i, (start_time, end_time) in enumerate(scene_list):
            # Convert timecodes to seconds
            start_sec = start_time.get_seconds()
            end_sec = end_time.get_seconds()

            # Calculate duration of the scene
            duration = end_sec - start_sec
            
            # Filter scenes based on duration
            if duration > min_duration:
                # Ensure the short is within the maximum duration
                if duration > max_duration:
                    end_sec = start_sec + max_duration

                # Create short clip
                short_filename = f"short_{i+1}.mp4"
                print(f"Creating short: {short_filename} (Duration: {duration:.2f} seconds)")
                ffmpeg_extract_subclip(video_path, start_sec, end_sec, targetname=short_filename)
            else:
                print(f"Scene {i+1} is too short ({duration:.2f} seconds) and will be skipped.")

    except Exception as e:
        print(f"An error occurred while creating shorts: {e}")

if __name__ == "__main__":
    video_path = "Ride Sisneri Hetauda.mp4" # Replace with your video path
    scenes = detect_scenes(video_path)
    create_shorts(video_path, scenes, min_duration=20, max_duration=59)

