from tkinter import filedialog
from tkinter import ttk
import moviepy.editor
from pathlib import Path
from tkinter import *
import tkinter as tk
import time
import threading


root = Tk()

root['bg'] = 'white'
root.title('Converter')
root.geometry('500x500')
root.resizable(False, False)


message_label = tk.Label(root, text="", bg='white',fg='green', font=("Arial", 12))
message_label.pack(pady=10)

def add_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        video_file = Path(file_path)
        print(f"Selected file: {file_path}")
        convert_to_audio(video_file)



def convert_to_audio(video_file):
    video = moviepy.editor.VideoFileClip(f'{video_file}')
    audio = video.audio
    desktop_path = Path.home() / 'Desktop'
    output_path = desktop_path / f'{video_file.stem}.mp3'

    audio.write_audiofile(output_path)
    message_label.config(text=f"Audio saved to {output_path}", fg = 'green')


add_file_button = tk.Button(root, text="Add file", command=add_file)
add_file_button.pack(pady=20)

root.mainloop()
