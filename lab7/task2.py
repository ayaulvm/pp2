import pygame
import os
import time
import threading

# Initialize pygame mixer
pygame.mixer.init()

# List of music files (replace with your own paths)
playlist = [
    "song1.mp3",
    "song2.mp3",
    "song3.mp3"
]
current_track = 0

def play():
    pygame.mixer.music.load(playlist[current_track])
    pygame.mixer.music.play()
    print(f"Playing: {playlist[current_track]}")

def stop():
    pygame.mixer.music.stop()
    print("Music stopped.")

def next_track():
    global current_track
    current_track = (current_track + 1) % len(playlist)
    play()

def previous_track():
    global current_track
    current_track = (current_track - 1) % len(playlist)
    play()

def handle_keyboard():
    import pygame.key  # Importing inside to ensure pygame initializes first
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:  # Press 'P' to play
                    play()
                elif event.key == pygame.K_s:  # Press 'S' to stop
                    stop()
                elif event.key == pygame.K_n:  # Press 'N' for next track
                    next_track()
                elif event.key == pygame.K_b:  # Press 'B' for previous track
                    previous_track()
                elif event.key == pygame.K_q:  # Press 'Q' to quit
                    print("Exiting music player.")
                    running = False

# Run keyboard listener in a separate thread
threading.Thread(target=handle_keyboard, daemon=True).start()

print("Music player started. Use keys: P=Play, S=Stop, N=Next, B=Previous, Q=Quit.")

# Keep the script running
while True:
    time.sleep(1)
