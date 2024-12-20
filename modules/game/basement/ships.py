import pygame
import os

from .read_json import read_json

data = read_json(fd="settings.json")

PLACE_LENGTH = data["color"]["PLACE_LENGTH"]
SHIPS_BAY_LENGTH = data["color"]["SHIPS_BAY_LENGTH"]

big_sq = pygame.Rect(68, 142, PLACE_LENGTH, PLACE_LENGTH)
small_sq = pygame.Rect(836, 142, SHIPS_BAY_LENGTH + 30, SHIPS_BAY_LENGTH)


def search_abs_path(count_length, DIR):
    path = os.path.abspath(__file__ + f"/../../../../image/ship/{count_length}-SHIP-{DIR}.png")
    return path


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class RectBetter(pygame.Rect):
    def __init__(self, x, y, w, h, close: bool):
        self.CLOSE = close
        pygame.Rect.__init__(
            self, 
            x, y, w, h
            )

class Ships():
    def __init__ (self, x: int, y: int, count_length: int, id : int):
        self.x = x
        self.y = y
        self.start_x = x
        self.start_y = y
        
        self.count_length = count_length
        self.ID = id
        self.COLOR = '#E7C500'

        self.WHERE = False

        self.row = 0
        self.cell = 0

        self.DIR = True
        self.LAST_DIR = True
        self.MOVE = False
        self.TAKE = False

        self.STAY = False
    
    def ship_draw(self, screen):
        if self.DIR:
            self.rect = pygame.Rect(self.x, self.y, 60* self.count_length, 60 )
            self.image = pygame.image.load(search_abs_path(self.count_length, self.DIR))
            self.image = pygame.transform.scale(self.image, [60 * self.count_length, 60])
            screen.blit(self.image, (self.x, self.y))

        elif not self.DIR:
            self.rect = pygame.Rect(self.x, self.y, 60, 60 * self.count_length)
            self.image = pygame.image.load(search_abs_path(self.count_length, self.DIR))
            self.image = pygame.transform.scale(self.image, [60,60 * self.count_length])
            screen.blit(self.image, (self.x, self.y))

    def take_ship(self, position, press):
        if self.rect.collidepoint(position):   
            if not self.MOVE and big_sq.collidepoint(position):
                self.WHERE = True
            elif not self.MOVE and small_sq .collidepoint(position):
                self.WHERE = False
            self.TAKE = True

    def move(self, position, press, screen):
        if press[0] and self.DIR and self.TAKE:
            self.x = position[0] - 30
            self.y = position[1] - 30
            self.MOVE = True
            self.image = pygame.image.load(search_abs_path(self.count_length, self.DIR))
            self.image = pygame.transform.scale(self.image, [60 * self.count_length,60])
            screen.blit(self.image, (self.x, self.y))

        elif press[0] and not self.DIR and self.TAKE:
            self.x = position[0] - 30
            self.y = position[1] - 30
            self.image = pygame.image.load(search_abs_path(self.count_length, self.DIR))
            self.image = pygame.transform.scale(self.image, [60,60 * self.count_length])
            screen.blit(self.image, (self.x, self.y))
            self.MOVE = True
        else:
            self.MOVE = False  
            self.TAKE = False
        
ship1 = Ships(x = 856, y = 162, count_length = 1, id= 0)
ship2 = Ships(x = 936, y = 162, count_length = 1, id= 1)
ship3 = Ships(x = 1016, y = 162, count_length = 1, id= 2)
ship4 = Ships(x = 1096, y = 162, count_length = 1, id= 3)

ship5 = Ships(x = 856, y = 242, count_length = 2, id= 4)
ship6 = Ships(x = 996, y = 242, count_length = 2, id= 5)
ship7 = Ships(x = 1136, y = 242, count_length = 2, id= 6)

ship8 = Ships(x = 856, y = 322, count_length = 3, id= 7)
ship9 = Ships(x = 1056, y = 322, count_length = 3, id= 8)

ship10 = Ships(x = 856, y = 402, count_length = 4, id= 9)

ship_list = [ship1, ship2, ship3, ship4, ship5, ship6, ship7, ship8, ship9, ship10]