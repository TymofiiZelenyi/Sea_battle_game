import pygame 
import time
from .button import *
from .settings import *


def settings():
    run_settings = True
    
    while run_settings:
        screen.fill(MAIN_WINDOW_COLOR)

        pygame.draw.rect(screen, "Red", (400, 700, 50, 50), 0)
        
        position =pygame.mouse.get_pos()
        press =pygame.mouse.get_pressed()

        pygame.draw.rect(screen, HEAD_COLOR, (0, 50, 1400, 150), 0)

        pygame.draw.rect(screen, DARKER_FON, (0, 200, 300, 600), 0)

        settings_text.text_draw(screen = screen)
        button_back_menu.button_draw(screen = screen)
        sound1.button_draw(screen = screen)
        sound2.button_draw(screen = screen)

        set_sound2 = sound2.checkPress(position = position, press = press)
        back_to_menu = button_back_menu.checkPress(position = position, press = press)
        
        if set_sound2:
            settings2()
        if back_to_menu:
            menu()
        
        pygame.display.flip()
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_settings = False
                pygame.quit()



def settings2():
    run_settings2 = True

    while run_settings2:
        screen.fill(MAIN_WINDOW_COLOR)

        pygame.draw.rect(screen, "Blue", (400, 700, 50, 50), 0)
        
        position =pygame.mouse.get_pos()
        press =pygame.mouse.get_pressed()

        pygame.draw.rect(screen, HEAD_COLOR, (0, 50, 1400, 150), 0)

        pygame.draw.rect(screen, DARKER_FON, (0, 200, 300, 600), 0)

        settings_text.text_draw(screen = screen)
        button_back_menu.button_draw(screen = screen)
        sound1.button_draw(screen = screen)
        sound2.button_draw(screen = screen)

        back_to_menu_window = button_back_menu.checkPress(position = position, press = press)
        set_sound1 = sound1.checkPress(position = position, press = press)

        if set_sound1:
            settings()    
        if back_to_menu_window:
            menu()
        
        pygame.display.flip()
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_settings2 = False
                pygame.quit()