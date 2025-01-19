'''
Цей модуль створює кнопки

Він використовує модулі:
    `pygame`
    `os`
'''


import pygame
import os

from .read_json import read_json

pygame.init()

data = read_json(fd="settings.json")

BUTTON_COLOR = data["button"]["COLOR"]
BUTTON_MENU_WIDTH = data["button"]["MENU_WIDTH"]
BUTTON_MENU_HEIGHT = data["button"]["MENU_HEIGHT"]
BUTTON_PLACEMENT_WIDTH = data["button"]["PLACEMENT_WIDTH"]
BUTTON_PLACEMENT_HEIGHT = data["button"]["PLACEMENT_HEIGHT"]
BUTTON_DARKER_COLOR = data["button"]["DARKER_COLOR"]
MAIN_WINDOW_COLOR = data["main"]["MAIN_WINDOW_COLOR"]

#клас Кнопки (+ її хітбокс "rect")
class Button():
    '''
    За допомогою цього класу ви можете створювати кнопки

    Приклад застосування:
        >>> Button(x = 350, y = 230, width = 500, height = 100, text = "str", text_size = 18, button_color = BUTTON_DARKER_COLOR) 
    '''
    def __init__(self, x: int, y: int, width: int, height: int, text: str, text_size = 40, button_color = BUTTON_COLOR):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.text_size = text_size
        self.button_color = button_color
        
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.load_text()
    
    def load_text(self):
        '''
        Знаходить та завантажує шрифт до гри та змінює його колір та розмір   

        '''
        
        #шрифт тексту та його величина
        path_to_fonts = os.path.abspath(__file__+ "/../../../../fonts/")
        main_font = pygame.font.Font(path_to_fonts + "/m_font.ttf", self.text_size)

        self.button = pygame.image.load(os.path.abspath(__file__ + "/../../../../image/button/default_button_disable_600-150.png"))
        self.button = pygame.transform.scale(self.button, [self.width, self.height])

        #текст та його колір
        self.text_obj = main_font.render(self.text, 1, MAIN_WINDOW_COLOR)
        text_width = self.text_size * len(self.text)

        self.text_x = (self.width - text_width) //2
        self.text_y = (self.height - self.text_size) //2
    
    
    #функція відображення кнопки з її текстом.
    def button_draw(self, screen: object):
        '''
        Відмальовує та розміщює кнопку та текст по координатам -> (x,y)
        
        Приклад застосування:
            >>> button_draw(screen = `screen`)
        '''
        #Розміщення нашої кнопки та тексту по кординатам.
        screen.blit(self.button, (self.x, self.y))
        screen.blit(self.text_obj, (self.x + self.text_x, self.y + self.text_y))

    #функція відслідження нажиму на кнопку
    def checkPress(self, position: str, press: bool) -> True:
        '''
        Перевіряє чи нажав гравець на лкм на хітбокс кнопки

        Приклад застосування:
            >>> checkPress(position = `position`, press = `press`)
        '''
        
        # if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom) and press[0]:
        if self.rect.collidepoint(position) and press[0]:
            return True


#Створення кнопок для всех экранов
button_back_menu = Button(x = 10, y = 675, width = 275, height = 100, text = "Back to menu", text_size=20)
button_sound =Button(x = 10, y = 675, width = 275, height = 100, text = "+", text_size=20)      
button_plus_settings = Button(x = 10, y = 675, width = 275, height = 100, text = "+", text_size=20)    
button_minus_settings = Button(x = 10, y = 675, width = 275, height = 100, text = "-", text_size=20)             
#Створення кнопок для екрану МЕНЮ "play" "settings" "quit", задавання їх величини та кординат на головному екрані. Містять у собі рядковий контент.
button_play = Button(x = 100, y = 80, width = BUTTON_MENU_WIDTH, height = BUTTON_MENU_HEIGHT, text = "Play")
button_settings = Button(x = 100, y = 180, width = BUTTON_MENU_WIDTH, height = BUTTON_MENU_HEIGHT, text = "Setting")
button_Armory = Button(x = 100, y = 280, width = BUTTON_MENU_WIDTH, height = BUTTON_MENU_HEIGHT, text = "Armory")
button_quit = Button(x = 100, y = 380, width = BUTTON_MENU_WIDTH, height = BUTTON_MENU_HEIGHT, text = "Quit")

shop_coursor1 = Button(x = 350, y = 200, width = 225, height = 450, text = "1")
shop_coursor2 = Button(x = 600, y = 200, width = 225, height = 450, text = "2")
shop_coursor3 = Button(x = 850, y = 200, width = 225, height = 450, text = "3")

#Створення кнопок для екрану SETTTING
sound_activated = Button(x = 50, y = 250, width = 200, height = 100, text = "Sounds", text_size = 25)
cursors_activated = Button(x = 50, y = 400, width = 200, height = 100, text = "Cursors", text_size = 25)
music_activated = Button(x = 50, y = 550, width = 200, height = 100, text = "Music", text_size = 25)

#Створення кнопок для екрану PLACEMENT
put_ships = Button(x = 66, y = 76, width = 604, height = 60, text = "Put the ships down!", text_size = 20, button_color = BUTTON_DARKER_COLOR)
your_ships = Button(x = 836 , y = 76, width = 430, height = 60, text = "Your ships", text_size = 20, button_color = BUTTON_DARKER_COLOR)

button_ready = Button(x = 836, y = 630, width = 430, height = BUTTON_PLACEMENT_HEIGHT, text = "ready")
#button_ready = Button(x = 970, y = 680, width = BUTTON_PLACEMENT_WIDTH, height = BUTTON_PLACEMENT_HEIGHT, text = "ready")


#Створення кнопок для екрану WAIT_OPPONENT
join = Button(x = 1000, y = 600, width = 300, height = BUTTON_MENU_HEIGHT, text = "Join", text_size= 25)
create = Button(x = 200, y = 600, width = 400, height = BUTTON_MENU_HEIGHT, text = "Create server", text_size= 25)

#Створення кнопок для екрану BATTLE
your_screen_text = Button(x = 70, y = 133, width = 604, height = 45, text = "Your screen", text_size = 18, button_color = BUTTON_DARKER_COLOR)
enemy_screen_text = Button(x = 728, y = 133, width = 604, height = 45, text = "Enemy screen", text_size = 18, button_color = BUTTON_DARKER_COLOR)

c418 = Button(x = 350, y = 230, width = 500, height = 100, text = "c418", text_size = 18, button_color = BUTTON_DARKER_COLOR)
new_year = Button(x = 350, y = 380, width = 500, height = 100, text = "new_year", text_size = 18, button_color = BUTTON_DARKER_COLOR)
trolo = Button(x = 350, y = 530, width = 500, height = 100, text = "trolo", text_size = 18, button_color = BUTTON_DARKER_COLOR)
rammstein = Button(x = 350, y = 680, width = 500, height = 100, text = "rammstein", text_size = 18, button_color = BUTTON_DARKER_COLOR) 
#

armory_page1 = Button(x = 1000, y = 50, width = 75, height = 75, text = " 1")
armory_page2 = Button(x = 1100, y = 50, width = 75, height = 75, text = " 2")
armory_page3 = Button(x = 1200, y = 50, width = 75, height = 75, text = " 3")

class Text():
    '''
    Створює текст за допомогою шрифтоф, які потрібно завантажити
    '''
    
    def __init__(self, x, y, text, text_size = 20, color = MAIN_WINDOW_COLOR):
        self.x = x
        self.y= y
        self.text = text
        self.text_size = text_size
        self.color = color 

        self.load()

    def load(self):
        '''
        Знаходить та завантажує шрифт до гри та змінює розмір 
        '''        
        #шрифт тексту та його величина
        path_to_fonts = os.path.abspath(__file__+ "/../../../../fonts/")
        self.main_font = pygame.font.Font(path_to_fonts + "/m_font.ttf", self.text_size)
        self.text = self.main_font.render(self.text, 1, self.color)
    def text_draw(self, screen: object):
        '''
        Відмальовує на екрані по координатам -> (x,y)
        '''
        screen.blit(self.text, (self.x, self.y))

settings_text = Text(x = 50, y = 100, text = "Settings", text_size=45)
Armory_text = Text(x = 50, y = 100, text = "Armory", text_size=45)
text_win = Text(x = 560, y = 320, text = "WIN", text_size=100, color="Red")
text_lose = Text(x = 560, y = 320, text = "LOSE", text_size=100, color="Red")
text_dynamite = Text(x = 0, y = 20, text = "Підриває все у формі +", text_size=45, color="Black")
text_torpedo = Text(x = 30, y = 20, text = "Підриває 1 клітину на цілому рядку", text_size=45, color="Black")
text_radar = Text(x = 60, y = 20, text = "Показує місце знаходження кораблів супротивника у радіусі 1 клітини", text_size=45, color="Black")
text_missile = Text(x = 90, y = 20, text = "Підриває 1 корабель у радіусі 2 клітин", text_size=45, color="Black")
text_shield = Text(x = 120, y = 20, text = "Ставить щит на корабель \n який захищає його від 1 попадання", text_size=45, color="Black")
text_bomb= Text(x = 150, y = 20, text = "Підриває всі кораблі у радіусі 1 клітини", text_size=45, color="Black")

skills_info_text = [text_dynamite, text_bomb, text_missile, text_radar, text_shield, text_torpedo]