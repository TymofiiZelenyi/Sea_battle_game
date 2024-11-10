import pygame 
from .button import button_back_menu, wait_opponent_text, put_ships, your_ships, button_play, button_quit, button_ready, button_settings, settings_text
from .__settings__ import DARKER_FON, HEAD_COLOR, FPS, WINDOW_HEIGHT, WINDOW_WIDTH, MAIN_WINDOW_COLOR, PLACE_LENGTH, BUTTON_COLOR, BUTTON_MENU_HEIGHT, BUTTON_MENU_WIDTH, SHIPS_BAY_LENGTH

pygame.init()
pygame.display.set_caption("Sea_battle_game")
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))

#ACTIVE_SCREEN = "menu"

#window_active = "menu"

def menu():
    while True:
        screen.fill(MAIN_WINDOW_COLOR)

        #Створення кнопок "play" "settings" "quit", задавання їх величини та кординат на головному екрані. Містять у собі рядковий контент.
        
        button_play.button_draw(screen = screen)
        button_settings.button_draw(screen = screen)
        button_quit.button_draw(screen = screen)

        position = pygame.mouse.get_pos()
        press = pygame.mouse.get_pressed()


        button_play.checkPress(position = position, press = press)
        button_settings.checkPress(position = position, press = press)
        button_quit.checkPress(position = position, press = press)
        
        
        pygame.display.flip()
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            #if event.type == pygame.MOUSEBUTTONDOWN:
                #if button_play.checkPress(position = position, press = press):
                    #wait_opponent()

def wait_opponent():
    while True:
        screen.fill(MAIN_WINDOW_COLOR)
        
        position = pygame.mouse.get_pos()
        press = pygame.mouse.get_pressed()

        wait_opponent_text.button_draw(screen = screen)
        
        button_back_menu.button_draw(screen = screen)
        button_back_menu.checkPress(position = position, press = press)

        pygame.display.flip()
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

def placement():
    while True:
        screen.fill(MAIN_WINDOW_COLOR)

        position = pygame.mouse.get_pos()
        press = pygame.mouse.get_pressed()
        
        put_ships.button_draw(screen = screen)
        your_ships.button_draw(screen = screen)
        
        button_ready.button_draw(screen = screen)
        button_ready.checkPress(position = position, press = press)
        #placemnt square
        pygame.draw.rect(screen, BUTTON_COLOR, (68, 142, PLACE_LENGTH, PLACE_LENGTH))
        #SHIPs bay
        pygame.draw.rect(screen, BUTTON_COLOR, (836, 142, SHIPS_BAY_LENGTH, SHIPS_BAY_LENGTH))

        pygame.display.flip()
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

def battle():
    while True:    
        screen.fill((MAIN_WINDOW_COLOR))
    
        #Наше поле (your screen)
        pygame.draw.rect(screen, BUTTON_COLOR, (50, 80, PLACE_LENGTH, PLACE_LENGTH), 0)
        #Поле противника (enemy screen)
        pygame.draw.rect(screen, BUTTON_COLOR, (750, 80, PLACE_LENGTH, PLACE_LENGTH), 0)

        pygame.display.flip()
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

def settings():
    while True:
        screen.fill(MAIN_WINDOW_COLOR)
        
        position =pygame.mouse.get_pos()
        press =pygame.mouse.get_pressed()

        pygame.draw.rect(screen, HEAD_COLOR, (0, 50, 1400, 150), 0)

        pygame.draw.rect(screen, DARKER_FON, (0, 200, 300, 600), 0)

        settings_text.text_draw(screen = screen)

        button_back_menu.button_draw(screen = screen)
        button_back_menu.checkPress(position = position, press = press)

        pygame.display.flip()
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
    

    
    




