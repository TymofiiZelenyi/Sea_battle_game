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

    PAGE1 = True
    PAGE2 = False
    PAGE3 = False

    card = pygame.image.load(os.path.abspath(__file__ + "/../../../image/skills/card.png"))
    card = pygame.transform.scale(card, [240, 380])

    image_torpedo = skills_list[5].image
    
    card_list= [card, card, card, card, card]

    while run_shop:
        screen.fill(MAIN_WINDOW_COLOR)

        if PAGE1:     
            gap = 20
            for card in card_list:
                screen.blit(card, (gap, 230))
                gap += 270


            gap = 32
            for skill in skills_list:
                if skill.id != 6:
                    screen.blit(skill.image, (gap, 245))
                    gap += 270

            text_dynamite.text_draw(screen=screen)
            text_radar.text_draw(screen=screen) 
            text_missile.text_draw(screen=screen) 
            text_shield.text_draw(screen=screen) 
            text_bomb.text_draw(screen=screen) 
            
                
        if PAGE2:
            screen.blit(card, (20, 230))
            screen.blit(image_torpedo, (32, 245))
            text_torpedo .text_draw(screen=screen)
        
        if PAGE3:
            print("PAGE3")

        
        position = pygame.mouse.get_pos()
        press = pygame.mouse.get_pressed()
        
        pygame.draw.rect(screen, HEAD_COLOR, (0, 0, 1400, 150), 0)
        Armory_text.text_draw(screen = screen)
           

        button_back_menu.button_draw(screen = screen)
        
        armory_page1.button_draw(screen = screen)
        armory_page2.button_draw(screen = screen)
        armory_page3.button_draw(screen = screen)
        
        pygame.display.flip()
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and press[0]:

                back_to_menu = button_back_menu.checkPress(position = position, press = press)

                PAGE1 = armory_page1.checkPress(position = position, press = press)
                PAGE2 = armory_page2.checkPress(position = position, press = press)
                PAGE3 = armory_page3.checkPress(position = position, press = press)
                
                if back_to_menu:
                    return "HOME"
                
                if not PAGE1 and not PAGE2 and not PAGE3:
                    pass
                elif PAGE1:
                    PAGE1 = True
                    PAGE2 = False
                    PAGE3 = False
                elif PAGE2:
                    PAGE1 = False
                    PAGE2 = True
                    PAGE3 = False
                elif PAGE3:
                    PAGE1 = False
                    PAGE2 = False
                    PAGE3 = True

                
            if event.type == pygame.QUIT:
                run_shop = False
                pygame.quit()