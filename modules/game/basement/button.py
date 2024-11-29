import pygame
from .settings import BUTTON_COLOR, MAIN_WINDOW_COLOR, BUTTON_MENU_WIDTH, BUTTON_MENU_HEIGHT, WINDOW_HEIGHT, WINDOW_WIDTH, BUTTON_PLACEMENT_HEIGHT, BUTTON_PLACEMENT_WIDTH, BUTTON_DARKER_COLOR
import os
#from .start import position, press

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
    
    
    #функція відображення кнопки з її текстом.
    def button_draw(self, screen):

        #шрифт тексту та його величина
        path_to_fonts = os.path.abspath(__file__+ "/../../../../fonts/")
        main_font = pygame.font.Font(path_to_fonts + "/m_font.ttf", self.text_size)

        #текст та його колір
        text = main_font.render(self.text, 1, MAIN_WINDOW_COLOR)
        
        
        #створення кнопки з отриманням її ширини та висоти
        button = pygame.surface.Surface((self.width, self.height))
        #заповнити нашу кнопку кольором "BUTTON_COLOR"
        button.fill(self.button_color)

        text_width = self.text_size * len(self.text)

        text_height = self.text_size

        text_x = (self.width - text_width) //2
        text_y = (self.height - text_height) //2


        #Розміщення нашої кнопки та тексту по кординатам.
        screen.blit(button, (self.x, self.y))
        screen.blit(text, (self.x + text_x, self.y + text_y))

    #функція відслідження нажиму на кнопку
    def checkPress(self, position, press):
        # if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom) and press[0]:
        if self.rect.collidepoint(position) and press[0]:
            return True


#Створення кнопок для всех экранов
button_back_menu = Button(x = 930, y = 600, width = 400, height = BUTTON_PLACEMENT_HEIGHT, text = "Back to menu", text_size=25)
            
#Створення кнопок для екрану МЕНЮ "play" "settings" "quit", задавання їх величини та кординат на головному екрані. Містять у собі рядковий контент.
button_play = Button(x = 100, y = 100, width = BUTTON_MENU_WIDTH, height = BUTTON_MENU_HEIGHT, text = "Play")
button_settings = Button(x = 100, y = 245, width = BUTTON_MENU_WIDTH, height = BUTTON_MENU_HEIGHT, text = "Setting")
button_quit = Button(x = 100, y = 390, width = BUTTON_MENU_WIDTH, height = BUTTON_MENU_HEIGHT, text = "Quit")

#Створення кнопок для екрану 
button_ready = Button(x = 970, y = 680, width = BUTTON_PLACEMENT_WIDTH, height = BUTTON_PLACEMENT_HEIGHT, text = "ready")

# #Створення кнопок для екрану SETTTING
sound1 = Button(x = 50, y = 300, width = 200, height = 100, text = "Sound", text_size = 25)

#Створення кнопок для екрану PLACEMENT
put_ships = Button(x = 68, y = 80, width = 600, height = 60, text = "Put the ships down!", text_size = 20, button_color = BUTTON_DARKER_COLOR)
your_ships = Button(x = 836 , y = 80, width = 430, height = 60, text = "Your ships", text_size = 20, button_color = BUTTON_DARKER_COLOR)

button_ready = Button(x = 836, y = 630, width = 430, height = BUTTON_PLACEMENT_HEIGHT, text = "ready")

#Створення кнопок для екрану WAIT_OPOENENT
wait_opponent_text = Button(x = 400, y = 150, width = BUTTON_MENU_WIDTH, height = BUTTON_MENU_HEIGHT, text = "Waiting for opponent...", text_size= 25)

#Створення кнопок для екрану BATTLE
your_screen_text = Button(x = 70, y = 98, width = 600, height = 80, text = "Your screen", text_size = 20, button_color = BUTTON_DARKER_COLOR)
enemy_screen_text = Button(x = 730, y = 98, width = 600, height = 80, text = "Enemy screen", text_size = 20, button_color = BUTTON_DARKER_COLOR)

class Text():
    def __init__(self, x, y, text, text_size = 40):
        self.x = x
        self.y= y
        self.text = text
        self.text_size = text_size

    def text_draw(self, screen):
        
        #шрифт тексту та його величина
        path_to_fonts = os.path.abspath(__file__+ "/../../../../fonts/")
        main_font = pygame.font.Font(path_to_fonts + "/m_font.ttf", self.text_size)

        text = main_font.render(self.text, 1, MAIN_WINDOW_COLOR)

        screen.blit(text, (self.x, self.y))

settings_text = Text(x = 50, y = 100, text = "Settings", text_size=45)
