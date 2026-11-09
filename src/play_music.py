import os
import pygame
from mutagen.wave import WAVE
from tqdm import tqdm
from menu import audio_menu



def play_music(folder, song_name):

    file_path = os.path.join(folder, song_name)
    song_info = WAVE(file_path)
    song_length = int(song_info.info.length)


    if not os.path.join(folder, song_name):
        print("File found")
        return
    


    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()


    # pygame set_volume is like a decibel meter in fl studio: 0.0-1.0
    
    song_setting = {
        "Find a Way(Master).wav": {"pos": 90.0, "volume": 0.5},
        "PEEL MY SKIN - 120bpm v2.wav": {"pos": 13.0, "volume": 0.2},
        "Body & Soul - master.wav": {"pos": 48.0, "volume": 0.3},
        "Im Scared.wav": {"pos": 48.0, "volume": 1.0},
        "Never Forget.wav": {"pos": 100.0, "volume": 0.8}
    }

    settings = song_setting.get(song_name)
    if settings:
        pygame.mixer.music.set_pos(settings["pos"])
        if "volume" in settings:
            pygame.mixer.music.set_volume(settings["volume"])


    print(f"\nNow playing: {song_name}")

    audio_menu()

# tqdm (self, iterable, desc= “Text You want”)




