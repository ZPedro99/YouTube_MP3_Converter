from PIL import Image
import yt_dlp
from tkinter import messagebox, ttk
import tkinter as tk
import os
import time

def download_music():
    url = url_field.get()
    file_folder = "downloads/"
    progress_bar['value'] = 0
    progress_bar['maximum'] = 100
    ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
    'outtmpl': os.path.join(file_folder, '%(title)s.%(ext)s'),
    'noplaylist': True,
    'quiet': False,
    }
    ydl = yt_dlp.YoutubeDL(ydl_opts)
    if not os.path.exists(file_folder):
        os.makedirs(file_folder)
    for i in range(26):
        progress_bar['value'] = i
        window.update_idletasks()
        time.sleep(0.02)
    ydl.download(url)

    for i in range(101):
        progress_bar['value'] = i
        window.update_idletasks()
        time.sleep(0.02)

    messagebox.showinfo("Success", "Download successful")
    


if __name__ == "__main__":
    window = tk.Tk()
    window.title("YouTube to MP3 converter")
    window.configure(bg='red')

    url_label = tk.Label(window, text="Youtube Video URL:", bg='red', fg="white", font="bold")
    url_label.pack(pady=10)

    url_field = tk.Entry(window, width=50)
    url_field.pack(pady=10)

    download_button = tk.Button(window, text="Download MP3", command=download_music, relief="raised")
    download_button.pack(pady=20)

    progress_bar = ttk.Progressbar(window, orient="horizontal", length=400, mode="determinate")
    progress_bar.pack(pady=10)
    
    window.mainloop()