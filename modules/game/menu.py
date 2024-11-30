import pygame 
import time

from .basement import *
from .placement import placement

play_music("All I Want for Christmas Is You")

def menu():
    run_menu = True

    while run_menu:
        
        screen.fill(MAIN_WINDOW_COLOR)

        #Створення кнопок "play" "settings" "quit", задавання їх величини та кординат на головному екрані. Містять у собі рядковий контент.
        
        button_play.button_draw(screen = screen)
        button_settings.button_draw(screen = screen)
        button_quit.button_draw(screen = screen)

        position = pygame.mouse.get_pos()
        press = pygame.mouse.get_pressed()


        wait_opponent_window = button_play.checkPress(position = position, press = press)
        settigs_window = button_settings.checkPress(position = position, press = press)
        quit = button_quit.checkPress(position = position, press = press)

        if wait_opponent_window:
            wait_opponent()
        if settigs_window:
            settings()
        if quit:
            run_menu = False

        pygame.display.flip()
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_menu = False
                pygame.quit()

def settings():
    run_settings = True

    sound_list = []
    space_off = 55
    space_on = 55
    ON = 5

    for item in range (10):
        sound_list.append(RectBetter(380 + space_off, 230, 50, 100, False))
        space_off += 55
    
    while run_settings:
        screen.fill(MAIN_WINDOW_COLOR)
        position =pygame.mouse.get_pos()
        press =pygame.mouse.get_pressed()

        min_rect = pygame.Rect(320, 230, 100, 100)
        plus_rect = pygame.Rect(1000, 230, 100, 100)
        pygame.draw.rect(screen, "blue", min_rect)
        pygame.draw.rect(screen, "blue", plus_rect)

        if ON < 0:
            ON = 0
        elif ON > 10:
            ON = 10

        for item in sound_list:
            pygame.draw.rect(screen, "black", item)

        for item in range(ON):
            pygame.draw.rect(screen, "red", (380 + space_on, 230, 50, 100))
            space_on += 55

        space_on = 55

        pygame.draw.rect(screen, "#CCCCCC", (0, 200, 300, 600), 0)

        pygame.draw.rect(screen, HEAD_COLOR, (0, 50, 1400, 150), 0)
        
        pygame.draw.rect(screen, HEAD_COLOR, (320, 255, 100, 50))

        pygame.draw.rect(screen, HEAD_COLOR, (1000, 255, 100, 50))
        pygame.draw.rect(screen, HEAD_COLOR, (1025, 230, 50, 100))
    
        settings_text.text_draw(screen = screen)
        button_back_menu.button_draw(screen = screen)
        sound1.button_draw(screen = screen)

        back_to_menu = button_back_menu.checkPress(position = position, press = press)
        
        if back_to_menu:
            menu()
        
        pygame.display.flip()
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTonUP and plus_rect.collidepoint(position) and press[0]:
                on +=1
                print(f"Plus {on}")
            elif event.type == pygame.MOUSEBUTTonUP and min_rect.collidepoint(position) and press[0]:
                on -= 1
                print(f"Minus {on}")
            
            
            if event.type == pygame.QUIT:
                run_settings = False
                pygame.quit()

def wait_opponent():
    run_wait_opponent = True

    while run_wait_opponent:
        screen.fill(MAIN_WINDOW_COLOR)
        
        position = pygame.mouse.get_pos()
        press = pygame.mouse.get_pressed()

        wait_opponent_text.button_draw(screen = screen)
        button_back_menu.button_draw(screen = screen)
        
        placement_window = wait_opponent_text.checkPress(position = position, press = press)
        back_to_menu = button_back_menu.checkPress(position = position, press = press)

        if placement_window:
            placement()
        if back_to_menu:
            menu()

        pygame.display.flip()
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_wait_opponent = False
                pygame.quit()

