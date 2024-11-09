import pygame
from .__settings__ import BUTTON_COLOR, MAIN_WINDOW_COLOR, BUTTON_MENU_WIDTH, BUTTON_MENU_HEIGHT, WINDOW_HEIGHT, WINDOW_WIDTH, BUTTON_PLACEMENT_HEIGHT,BUTTON_PLACEMENT_WIDTH
import os
#from .start import position, press

#клас Кнопки (+ її хітбокс "rect")
class Button():
    def __init__(self, x, y, width, height, text, text_size = 40):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.text_size = text_size
        
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    
    
    #функція відображення кнопки з її текстом.
    def button_draw(self, screen):

        #шрифт тексту та його величина
        path_to_fonts = os.path.abspath(__file__+ "/../../fonts/")
        main_font = pygame.font.Font(path_to_fonts + "/m_font.ttf", self.text_size)

        #текст та його колір
        text = main_font.render(self.text, 1, MAIN_WINDOW_COLOR)
        
        # text_rect = text.get_rect(center=(BUTTON_WIDTH/2, BUTTON_HEIGHT/2))
        # screen.blit(text, text_rect)
        
        #створення кнопки з отриманням її ширини та висоти
        button = pygame.surface.Surface((self.width, self.height))
        #заповнити нашу кнопку кольором "BUTTON_COLOR"
        button.fill(BUTTON_COLOR)

        #Розміщення нашої кнопки та тексту по кординатам.
        screen.blit(button, (self.x, self.y))
        screen.blit(text, (self.x + 50, self.y + 50))

    #функція відслідження нажиму на кнопку
    def checkPress(self, position, press):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom) and press == (True, False, False):
            self.text = "НАЖАТО"
            #self.pressed = True
            #return self.pressed
        else:
            self.text= self.text



            
#Створення кнопок для екрану МЕНЮ "play" "settings" "quit", задавання їх величини та кординат на головному екрані. Містять у собі рядковий контент.
button_play = Button(x = 100, y = 100, width = BUTTON_MENU_WIDTH, height = BUTTON_MENU_HEIGHT, text = "Play")
button_settings = Button(x = 100, y = 245, width = BUTTON_MENU_WIDTH, height = BUTTON_MENU_HEIGHT, text = "Setting")
button_quit = Button(x = 100, y = 390, width = BUTTON_MENU_WIDTH, height = BUTTON_MENU_HEIGHT, text = "Quit")

#Створення кнопок для екрану 
button_ready = Button(x = 970, y = 680, width = BUTTON_PLACEMENT_WIDTH, height = BUTTON_PLACEMENT_HEIGHT, text = "ready")

#Створення кнопок для екрану ОЧІКУВАННЯ
button_back_menu = Button(x = 1320 - BUTTON_MENU_WIDTH, y = 740 - BUTTON_MENU_HEIGHT, width = BUTTON_MENU_WIDTH, height = BUTTON_MENU_HEIGHT, text = "Back to menu", text_size = 20)
