import tkinter as tk
from tkinter import messagebox
from yt_dlp import YoutubeDL
import os
import subprocess

def download_video():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Error", "Please enter a YouTube URL")
        return

    try:
        ydl_opts = {
            'format': 'best',
            'outtmpl': '%(title)s.%(ext)s'
        }
        with YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            file_path = ydl.prepare_filename(info_dict)
        messagebox.showinfo("Success", "Video downloaded successfully!")
        play_video(file_path)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to download video: {str(e)}")

def play_video(file_path):
    try:
        if os.name == 'nt':
            os.startfile(file_path)
        else:
            subprocess.call(['xdg-open', file_path])
    except Exception as e:
        messagebox.showerror("Error", f"Failed to play video: {str(e)}")

def exit_app():
    root.destroy()

root = tk.Tk()
root.title("YouTube Video Downloader")
root.geometry("400x200")
root.resizable(False, False)

url_label = tk.Label(root, text="Enter YouTube URL:")
url_label.pack(pady=10)

url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

download_button = tk.Button(root, text="Download", command=download_video)
download_button.pack(pady=10)

exit_button = tk.Button(root, text="Exit", command=exit_app)
exit_button.pack(pady=5)

root.mainloop()
