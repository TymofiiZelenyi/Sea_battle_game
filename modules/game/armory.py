import pygame
import os

from .basement import *
from .map import *

data = read_json(fd="settings.json")

MAIN_WINDOW_COLOR = data["main"]["MAIN_WINDOW_COLOR"]
HEAD_COLOR = data["color"]["HEAD_COLOR"]
FPS = data["main"]["FPS"]

def shop():
    run_shop = True

    card = pygame.image.load(os.path.abspath(__file__ + "/../../../image/skills/card.png"))
    card = pygame.transform.scale(card, [240, 380])

    card_list= [card, card, card, card, card]

    while run_shop:
        screen.fill(MAIN_WINDOW_COLOR)
        
        gap = 30
        for card in card_list:
            screen.blit(card, (gap, 230))
            gap += 270
        
        position = pygame.mouse.get_pos()
        press = pygame.mouse.get_pressed()
        
        pygame.draw.rect(screen, HEAD_COLOR, (0, 0, 1400, 150), 0)
        Armory_text.text_draw(screen = screen)

        button_back_menu.button_draw(screen = screen)
        
        pygame.display.flip()
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and press[0]:

                back_to_menu = button_back_menu.checkPress(position = position, press = press)
                
                if back_to_menu:
                    return "HOME"
                
            if event.type == pygame.QUIT:
                run_shop = False
                pygame.quit()