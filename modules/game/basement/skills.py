import pygame 
import os 
from .button import Text 
from .read_json import read_json 
 
data = read_json(fd="settings.json") 
 
PLACE_LENGTH = data["color"]["PLACE_LENGTH"] 
SHIPS_BAY_LENGTH = data["color"]["SHIPS_BAY_LENGTH"] 

#Наше поле (your screen)
sq_your = pygame.Rect((70, 180, PLACE_LENGTH, PLACE_LENGTH))
#Поле противника (enemy screen)
sq_enemy = pygame.Rect((730, 180, PLACE_LENGTH, PLACE_LENGTH))

sq_list = [sq_your,  sq_enemy]
 
class Skills(): 
    def __init__(self, name_skill, x, y, price): 
        self.skill = name_skill 
        self.count = 0 
        self.x= x  
        self.y = y 
        self.price = price 
         
        self.TAKE = False 
        self.OUT = False
 
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
        self.image_plus = pygame.transform.scale(self.image_plus, [30, 30]) 
 
        self.plus_rect = pygame.Rect((self.x + 80, self.y, 30, 30)) 
        self.rect_move = pygame.Rect(self.x,self.y, 80, 80) 
        self.counter = Text(self.x, self.y, text= str(self.count), color = "Black") 

        # self.rect = pygame.Rect((self.x + 15, self.y + 15, 50, 50)) 
        # self.rect = pygame.Rect((self.rect_x, self.rect_y, 50, 50)) 
 
    def draw_skill(self, screen): 
        self.counter.text_draw(screen= screen) 
        pygame.draw.rect(screen, "Green", self.plus_rect) 
        screen.blit(self.image_plus, (self.x + 75, self.y)) 
        self.price_text.text_draw(screen= screen) 
 
        pygame.draw.rect(screen, "Yellow", self.rect_move) 
        screen.blit(self.image, (self.x, self.y)) 
 
    def plus(self, point):    
        if point >= 20: 
            self.count += 1 
            self.counter = Text(self.x, self.y, text= str(self.count), color = "Black") 
            return True
         
        return False
     
    def take(self): 
        if self.count > 0:
            print("TAKE") 
            self.TAKE = True 
 
    def move(self, position, press, screen): 
        if press[0] and self.TAKE: 
            self.rect_x = position[0] - 25 
            self.rect_y = position[1] - 25 

            screen.blit(self.image, (self.rect_x, self.rect_y)) 

        # elif not self.TAKE and self.OUT:
        #     print("out")
        #     self.rect_x= self.x
        #     self.rect_y= self.y
        #     self.OUT= False



 
bomb= Skills(name_skill = "bomb",x= 70 ,y= 15 ,price= 500) 
dynamite= Skills(name_skill = "dynamite",x= 190 ,y= 15, price= 30) 
unfire= Skills(name_skill= "unfire",x= 310, y= 15, price= 40) 
flamethrower = Skills(name_skill = "flamethrower", x= 430 ,y= 15, price= 50) 
rocket= Skills(name_skill = "rocket",x= 550 , y= 15, price= 30) 
shield= Skills(name_skill = "shield",x= 670 ,y= 15, price= 20) 
torpedo= Skills(name_skill = "torpedo",x= 790 , y= 15, price= 40) 
 
skills_list = [bomb, dynamite, unfire, flamethrower, rocket, shield, torpedo]