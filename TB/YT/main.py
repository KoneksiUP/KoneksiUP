import pytube
import tkinter as tk
import io
from PIL import Image, ImageTk

def play_youtube_video(url):
    # Mendapatkan objek YouTube
    youtube = pytube.YouTube(url)

    # Mendapatkan stream video terbaik
    video_stream = youtube.streams.filter(progressive=True).first()

    # Mengunduh video ke objek BytesIO
    video_data = io.BytesIO()
    video_stream.stream_to_buffer(video_data)

    # Mengonversi video ke objek PIL Image
    video_data.seek(0)
    video_image = Image.open(video_data)

    # Membuat jendela Tkinter
    window = tk.Tk()
    window.title("YouTube Video Player")

    # Mengubah ukuran jendela sesuai ukuran video
    window.geometry(f"{video_image.width}x{video_image.height}")

    # Membuat objek Tkinter Label untuk menampilkan video
    video_label = tk.Label(window)
    video_label.pack()

    # Mengubah objek PIL Image menjadi objek Tkinter PhotoImage
    video_photo = ImageTk.PhotoImage(video_image)

    # Menampilkan video pada label
    video_label.config(image=video_photo)
    video_label.image = video_photo

    # Menjalankan jendela Tkinter
    window.mainloop()

# Main program
if __name__ == "__main__":
    video_url = input("Masukkan URL video YouTube: ")
    play_youtube_video(video_url)
