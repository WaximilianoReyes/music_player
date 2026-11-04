import os
import pygame
import time
from tqdm import tqdm
from mutagen.wave import WAVE


def play_music(folder, song_name):

    file_path = os.path.join(folder, song_name)

    song_info = WAVE(file_path)
    song_length = int(song_info.info.length)

    if not os.path.join(folder, song_name):
        print("File found")
        return
    


    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

    # Changing positions of specific songs
    if song_name == "Find a Way(Master).wav":
        pygame.mixer.music.set_pos(40.0)
        pygame.mixer.music.set_volume(0.5)
    if song_name == "PEEL MY SKIN - 120bpm v2.wav":
        pygame.mixer.music.set_pos(13.0)
    if song_name == "Body & Soul - master.wav":
        pygame.mixer.music.set_pos(48.0)
        pygame.mixer.music.set_volume(0.3)

    print(f"\nNow playing: {song_name}")

  
    progress_bar = tqdm(
            total=song_length,
            unit="s"
        )
        
    milliseconds = pygame.mixer.music.get_pos()
    seconds_played = max(milliseconds, 0) / 1000
        
    progress_bar = int(seconds_played)
    time.sleep(0.2)

    # user input controls
    print("Commands: [P]ause, [R]esume, [Re]wind, [S]top")
    while True:

        command = input("> ").upper()

        if command == "P":
            pygame.mixer.music.pause()
            print("Paused")
        elif command == "R":
            pygame.mixer.music.unpause()
            print("Resumed")
        elif command == "S":
            pygame.mixer.music.stop()
            print("Stopped")
            return
        else:
            print("Invalid command")