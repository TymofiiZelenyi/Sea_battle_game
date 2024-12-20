import pygame

from .read_json import read_json

data = read_json(fd="settings.json")

WINDOW_HEIGHT = data["main"]["WINDOW_HEIGHT"]
WINDOW_WIDTH = data["main"]["WINDOW_WIDTH"]

pygame.init()
pygame.display.set_caption("Sea_battle_game")
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
