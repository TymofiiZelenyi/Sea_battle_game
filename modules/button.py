import pygame
from .__settings__ import BUTTON_COLOR, MAIN_WINDOW_COLOR, BUTTON_WIDTH, BUTTON_HEIGHT
#from .start import position, press

#клас Кнопки (+ її хітбокс "rect")
class Button():
    def __init__(self, x, y , width, height, text):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    
    
    #функція відображення кнопки з її текстом.
    def button_draw(self, screen):

        #шрифт тексту та його величина
        main_font = pygame.font.Font("images/m_font.ttf", 40)

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


            
#Створення кнопок "play" "settings" "quit", задавання їх величини та кординат на головному екрані. Містять у собі рядковий контент.
button_play = Button(x = 100, y = 100, width = BUTTON_WIDTH, height = BUTTON_HEIGHT, text = "Play")
button_settings = Button(x = 100, y = 245, width = BUTTON_WIDTH, height = BUTTON_HEIGHT, text = "Setting")
button_quit = Button(x = 100, y = 390, width = BUTTON_WIDTH, height = BUTTON_HEIGHT, text = "Quit")


