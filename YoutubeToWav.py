from pytube import YouTube
from moviepy.editor import *

def download_and_convert(youtube_url, save_path):
    # Download the YouTube video
    yt = YouTube(youtube_url)
    stream = yt.streams.filter(file_extension='mp4').first()
    stream.download(output_path="/tmp", filename="temp_video")

    # Convert the downloaded video to WAV format
    video_clip = VideoFileClip("/tmp/temp_video.mp4")
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(save_path, format='wav')
    audio_clip.close()
    video_clip.close()

if __name__ == "__main__":
    youtube_url = input("Enter the YouTube URL: ")
    save_path = input("Enter the path to save the WAV file: ")
    download_and_convert(youtube_url, save_path)
    print(f"File saved to {save_path}")
