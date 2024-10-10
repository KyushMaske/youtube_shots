import yt_dlp

# Function to download YouTube video with video and audio
def download_video(youtube_url, output_path="."):
    try:
        # Options for downloading video and audio together
        ydl_opts = {
            'format': 'best[ext=mp4][acodec!=none]/bestaudio/best',  # Get best mp4 video+audio stream available
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',  # Save with title and extension
            'merge_output_format': 'mp4',  # Ensure it merges video and audio if needed
        }

        # Download the video
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_url])
        print("Download complete.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    youtube_url = input("Enter the YouTube video URL: ")
    download_video(youtube_url)

