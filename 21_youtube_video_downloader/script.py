# from pytube import YouTube
import yt_dlp

link = "https://www.youtube.com/watch?v=XSrJSHXjFew"

ydl_opts = {
    'outtmpl': '%(title)s.%(ext)s',  # Save as video_title.mp4
    'format': 'best'  # Best available quality
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([link])

