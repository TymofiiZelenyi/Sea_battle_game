import pygame 
import os

def play_music():
  path_to_music = os.path.abspath(__file__ + "/../../../../sounds")
  music = (path_to_music + "/All I Want for Christmas Is You.mp3")
  pygame.mixer.music.load(music)
  pygame.mixer.music.play(loops=0, start=0.0, fade_ms=0)
  print("s")