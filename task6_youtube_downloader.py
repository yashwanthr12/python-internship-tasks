import yt_dlp
import os

try:
    url = input("Enter YouTube video URL: ")
    path = input("Enter destination folder path: ")

    if not os.path.exists(path):
        print("Invalid folder path")
    else:
        ydl_opts = {
            'outtmpl': os.path.join(path, '%(title)s.%(ext)s')
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        print("Download completed successfully")

except Exception as e:
    print("Error occurred:", e)

#https://youtu.be/3fKXzR0IDRU?si=59DubvVnA0WhvfC0
#C:\Users\Admin\Desktop\Python Internship Tasks
