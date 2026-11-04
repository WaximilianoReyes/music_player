
import os
import pygame
import time
from tqdm import tqdm


def play_music(folder, song_name):

    file_path = os.path.join(folder, song_name)

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
        pygame.mixer.music.set_pos(86.0)
    if song_name == "Body & Soul - master.wav":
        pygame.mixer.music.set_pos(48.0)

    print(f"\nNow playing: {song_name}")
    print("Commands: [P]ause, [R]esume, [Re]wind, [S]top")


    # user input controls
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