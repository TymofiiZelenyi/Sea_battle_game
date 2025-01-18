'''
Цей модуль відтворює музику 
'''
import pygame 
import os

def play_music(name_music: str, volume: int):
  '''
  Ця функція програє музику та змінює гучність нуя
  '''
  path_to_music = os.path.abspath(__file__ + "/../../../../sounds")
  music = (path_to_music + f"/{name_music}.mp3")
  pygame.mixer.music.load(music)
  pygame.mixer.music.play(loops=0, start=2.0, fade_ms=0)
  pygame.mixer.music.set_volume(volume)



