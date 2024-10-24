from pytubefix import YouTube
from pydub import AudioSegment
from tkinter import messagebox, ttk
import tkinter as tk
import os
import time

def download_music():
    url = url_field.get()
    link = YouTube(url)
    file_folder = "../downloads/"
    audio_file = link.streams.filter(only_audio=True).first()
    song_name = audio_file.title
    if not os.path.exists(file_folder):
        os.makedirs(file_folder)
    audio_file.download(output_path=file_folder, filename=song_name)

    progress_bar['value'] = 0
    progress_bar['maximum'] = 100

    for i in range(101):
        progress_bar['value'] = i
        window.update_idletasks()
        time.sleep(0.02)

    file_name = AudioSegment.from_file(file_folder + song_name)
    output_directory = os.path.join(file_folder, f"{song_name}.mp3")
    if not os.path.exists(output_directory):
        file_name.export(output_directory, format="mp3")
    else:
        messagebox.showwarning("Error", "File already exists.")
        os.remove(file_folder + song_name)
        return
    os.remove(file_folder + song_name)
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