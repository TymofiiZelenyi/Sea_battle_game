'''
Цей Модуль створює здібності
'''
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
    '''
    Цей клас створює здібності
    '''
    def __init__(self,name_skill ,x ,y ,price , id): 
        self.skill= name_skill 
        self.count= 0 
        self.x= x  
        self.y= y 
        self.price= price 
        self.id= id
         
        self.TAKE = False 
 
        self.rect_x = x 
        self.rect_y = y 
 
        self.load() 
 
    def load(self): 
        '''
        Ця функція завнтажує фото здібностей до гри та ставить текст
        '''
        self.price_text = Text(self.x + 16, self.y + 60, text= str(self.price), color = "Black", text_size= 25) 
 
        path = os.path.abspath(__file__ + f"/../../../../image/skills/{self.skill}.png")
        self.image = pygame.image.load(path) 
        self.image = pygame.transform.scale(self.image, [80, 80]) 

        if self.id != 3 and self.id != 5:
            path_c = os.path.abspath(__file__ + f"/../../../../image/skills/{self.skill}_clean.png")
            self.image_c = pygame.image.load(path_c) 
            self.image_c = pygame.transform.scale(self.image_c, [80, 80]) 
 
        path_p = os.path.abspath(__file__ + f"/../../../../image/skills/plus.png")
        self.image_plus = pygame.image.load(path_p) 
        self.image_plus = pygame.transform.scale(self.image_plus, [30, 30]) 
 
        self.plus_rect = pygame.Rect((self.x + 80, self.y, 30, 30)) 
        # self.rect_move = pygame.Rect(self.x,self.y, 80, 80) 
        self.counter = Text(self.x, self.y, text= str(self.count), color = "#D3D3D3") 
        
        self.rect = pygame.Rect((self.rect_x, self.rect_y, 80, 80)) 
 
    def draw_skill(self, screen: object): 
        '''
        Ця функція відмальовує скіли на екрані, їх ціну та назву
        '''
        # pygame.draw.rect(screen, "Green", self.plus_rect) 
        screen.blit(self.image_plus, (self.x + 85, self.y)) 
        # pygame.draw.rect(screen, "Yellow", self.rect) 
        screen.blit(self.image, (self.x, self.y)) 
 
        self.counter.text_draw(screen= screen) 
        self.price_text.text_draw(screen= screen) 
 
    def plus(self, point):
        '''
        Ця функція дозволяє купити здібності в грі

        змінна `point` відповідає за ігрову валюту, яку ви отримуєте за потоплення кораблів 
        '''    
        if point >= 20:
            self.count += 1 
            self.counter = Text(self.x, self.y, text= str(self.count), color = "#D3D3D3") 
            return True
         
        return False
     
    def take(self):
        '''
        Ця функція дозволяє брати здібності якщо їх більше 0
        ''' 
        if self.count > 0:
            print("TAKE") 
            self.TAKE = True 
 
    def move(self, position: tuple, press: tuple, screen: object): 
        '''
        Ця функція дозволяє переносити здібності по полю, та розміщювати їх
        '''
        if press[0] and self.TAKE: 
            self.rect_x = position[0] - 25 
            self.rect_y = position[1] - 25 

            if self.id != 3 and self.id !=5:
                screen.blit(self.image_c, (self.rect_x, self.rect_y)) 

            elif self.id == 3 or self.id == 5:
                screen.blit(self.image, (self.rect_x, self.rect_y)) 

        else:
            self.TAKE = False

bomb= Skills(name_skill = "bomb",x= 70 ,y= 15 ,price= 500, id= 1) 
dynamite= Skills(name_skill = "dynamite",x= 190 ,y= 15, price= 30, id= 2) 
radar = Skills(name_skill= "Radar",x= 310, y= 15, price= 40, id= 3) 
rocket= Skills(name_skill = "rocket",x= 430 , y= 15, price= 30, id= 4) 
shield= Skills(name_skill = "shield",x= 550 ,y= 15, price= 20, id= 5) 
torpedo= Skills(name_skill = "torpedo",x= 670 , y= 15, price= 40, id= 6) 
# unfire= Skills(name_skill= "unfire",x= 790, y= 15, price= 40, id= 7) 
# flamethrower = Skills(name_skill = "flamethrower", x= 910 ,y= 15, price= 50, id= 8) 
 
skills_list = [bomb, dynamite, radar, rocket, shield, torpedo]
# skills_list = [bomb, dynamite, radar, rocket, shield, torpedo, unfire, flamethrower,]