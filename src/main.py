import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame
from play_music import play_music
 
def main():

    try:
        pygame.mixer.init()
    except pygame.error as e:
        print("Audio initialization failed! ", e)
        return

    
    folder = 'songs'

    # reminding myself to insert the file
    if not os.path.isdir(folder):
        print(f"Folder '{folder}' not found")
        return

    # begin loading songs
    wav_files = [file for file in sorted(os.listdir(folder)) if file.endswith(".wav".strip())]

    if not wav_files:
        print("No .wav files found!")

    while True:
        print("***** .wav PLAYER *****")
        print("My Playlist: ")

        # print out the list of songs in a folder starting the index from 1
        for index, song in enumerate(wav_files, start=1):
            print(f"{index}. {song}")

        choice_input = input("\nEnter the song # to play (or 'Q' to quit): ")

        if choice_input.upper() == "Q":
            print("Goodbye!")
            break
        if not choice_input.isdigit():
            print("Enter a valid number!")
            continue

        choice = int(choice_input) - 1

        if 0 <= choice < len(wav_files):
            play_music(folder, wav_files[choice])
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()