import pygame
import os
from .button import Text
from .read_json import read_json

data = read_json(fd="settings.json")

PLACE_LENGTH = data["color"]["PLACE_LENGTH"]
SHIPS_BAY_LENGTH = data["color"]["SHIPS_BAY_LENGTH"]

big_sq = pygame.Rect(68, 142, PLACE_LENGTH, PLACE_LENGTH)
small_sq = pygame.Rect(836, 142, SHIPS_BAY_LENGTH + 30, SHIPS_BAY_LENGTH)

class Skills():
    def __init__(self, name_skill, x, y, price):
        self.skill = name_skill
        self.count = 0
        self.x= x 
        self.y = y
        self.price = price
        
        self.TAKE = False

        self.rect_x = x
        self.rect_y = y

        self.load()

    def load(self):
        self.price_text = Text(self.x + 16, self.y + 60, text= str(self.price), color = "Black", text_size= 25)

        path = os.path.abspath(__file__ + f"/../../../../image/skills/{self.skill}.png")
        self.image = pygame.image.load(path)
        self.image = pygame.transform.scale(self.image, [80, 80])

        path_p = os.path.abspath(__file__ + f"/../../../../image/skills/plus.png")
        self.image_plus = pygame.image.load(path_p)
        self.image_plus = pygame.transform.scale(self.image_plus, [20, 20])

        self.plus_rect = pygame.Rect((self.x + 60, self.y, 20, 20))

        self.rect = pygame.Rect((self.rect_x, self.rect_y, 50, 50))

    def draw_skill(self, screen):
        self.counter = Text(self.x, self.y, text= str(self.count), color = "Black")
        
        # self.rect = pygame.Rect(50, 50)
        screen.blit(self.image, (self.x, self.y))
        self.counter.text_draw(screen= screen)
        pygame.draw.rect(screen, "Green", self.plus_rect)
        screen.blit(self.image_plus, (self.x + 60, self.y))
        self.price_text.text_draw(screen= screen)

        pygame.draw.rect(screen, "Yellow", self.rect)

    def plus(self, point):
        if point >= 20:
            self.count += 1
            return True
        
        return False
    
    def take(self, position):
        print("TAKE")
        self.TAKE = True

    def move(self, position, press, screen):
        if press[0] and self.TAKE:
            self.rect_x = position[0] - 25
            self.rect_y = position[1] - 25
            self.rect = pygame.Rect((self.rect_x, self.rect_y, 50, 50))
            pygame.draw.rect(screen, "Yellow", self.rect)
            #HITBOX
        else:  
            self.TAKE = False


bomb= Skills(name_skill = "bomb",x= 70 ,y= 15 ,price= 20)
dynamite= Skills(name_skill = "dynamite",x= 175 ,y= 15, price= 20)
unfire= Skills(name_skill= "unfire",x= 280, y= 15, price= 20)
flamethrower= Skills(name_skill = "flamethrower", x= 385 ,y= 15, price= 20)
rocket= Skills(name_skill = "rocket",x= 490 , y= 15, price= 20)
shield= Skills(name_skill = "shield",x= 595 ,y= 15, price= 20)
torpedo= Skills(name_skill = "torpedo",x= 700 , y= 15, price= 20)

skills_list = [bomb, dynamite, unfire, flamethrower, rocket, shield, torpedo]
