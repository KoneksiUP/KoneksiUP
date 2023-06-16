import pygame

def play_music(file_path, volume=0.5):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def main():
    file_path = 'musik.mp3'  # Ganti dengan path file musik Anda
    volume = float(input("Masukkan volume (0.0 - 1.0): "))
    play_music(file_path, volume)
    
    while pygame.mixer.music.get_busy():
        continue

    stop_music()

if __name__ == '__main__':
    main()
