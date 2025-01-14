import pygame
import os
pygame.init()
from .read_json import read_json

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
    def button_draw(self, screen):
        #Розміщення нашої кнопки та тексту по кординатам.
        screen.blit(self.button, (self.x, self.y))
        screen.blit(self.text_obj, (self.x + self.text_x, self.y + self.text_y))

    #функція відслідження нажиму на кнопку
    def checkPress(self, position, press):
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
button_shop = Button(x = 100, y = 280, width = BUTTON_MENU_WIDTH, height = BUTTON_MENU_HEIGHT, text = "Shop")
button_quit = Button(x = 100, y = 380, width = BUTTON_MENU_WIDTH, height = BUTTON_MENU_HEIGHT, text = "Quit")


shop_coursor1 = Button(x = 25, y = 200, width = 225, height = 450, text = "1")
shop_coursor2 = Button(x = 300, y = 200, width = 225, height = 450, text = "2")
shop_coursor3 = Button(x = 575, y = 200, width = 225, height = 450, text = "3")
shop_coursor4 = Button(x = 850, y = 200, width = 225, height = 450, text = "4")
shop_coursor5 = Button(x = 1125, y = 200, width = 225, height = 450, text = "5")

#Створення кнопок для екрану 
button_ready = Button(x = 970, y = 680, width = BUTTON_PLACEMENT_WIDTH, height = BUTTON_PLACEMENT_HEIGHT, text = "ready")

# #Створення кнопок для екрану SETTTING
sound1 = Button(x = 50, y = 300, width = 200, height = 100, text = "Sound", text_size = 25)

#Створення кнопок для екрану PLACEMENT
put_ships = Button(x = 66, y = 76, width = 604, height = 60, text = "Put the ships down!", text_size = 20, button_color = BUTTON_DARKER_COLOR)
your_ships = Button(x = 836 , y = 76, width = 430, height = 60, text = "Your ships", text_size = 20, button_color = BUTTON_DARKER_COLOR)

button_ready = Button(x = 836, y = 630, width = 430, height = BUTTON_PLACEMENT_HEIGHT, text = "ready")

#Створення кнопок для екрану WAIT_OPPOENENT
join = Button(x = 1000, y = 300, width = 300, height = BUTTON_MENU_HEIGHT, text = "Join", text_size= 25)
create = Button(x = 200, y = 300, width = 400, height = BUTTON_MENU_HEIGHT, text = "Create server", text_size= 25)

#Створення кнопок для екрану BATTLE
your_screen_text = Button(x = 70, y = 98, width = 600, height = 80, text = "Your screen", text_size = 20, button_color = BUTTON_DARKER_COLOR)
enemy_screen_text = Button(x = 730, y = 98, width = 600, height = 80, text = "Enemy screen", text_size = 20, button_color = BUTTON_DARKER_COLOR)

class Text():
    def __init__(self, x, y, text, text_size = 20, color = MAIN_WINDOW_COLOR):
        self.x = x
        self.y= y
        self.text = text
        self.text_size = text_size
        self.color = color 

        self.load()

    def load(self):
                
        #шрифт тексту та його величина
        path_to_fonts = os.path.abspath(__file__+ "/../../../../fonts/")
        self.main_font = pygame.font.Font(path_to_fonts + "/m_font.ttf", self.text_size)

    def text_draw(self, screen):

        text = self.main_font.render(self.text, 1, self.color)

        screen.blit(text, (self.x, self.y))

settings_text = Text(x = 50, y = 100, text = "Settings", text_size=45)
shop_text = Text(x = 50, y = 100, text = "Shop", text_size=45)
text_win = Text(x = 560, y = 320, text = "WIN", text_size=100, color="Red")
text_lose = Text(x = 560, y = 320, text = "LOSE", text_size=100, color="Red")
