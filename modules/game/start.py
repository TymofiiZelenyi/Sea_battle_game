import pygame 
from .ships import *
from .button import *
from .settings import *

# button_back_menu, sound1, sound2, wait_opponent_text, put_ships, your_ships, button_play, button_quit, button_ready, button_settings, settings_text
# DARKER_FON, HEAD_COLOR, FPS, WINDOW_HEIGHT, WINDOW_WIDTH, MAIN_WINDOW_COLOR, PLACE_LENGTH, BUTTON_COLOR, BUTTON_MENU_HEIGHT, BUTTON_MENU_WIDTH, SHIPS_BAY_LENGTH

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


        wait_opponent_window = button_play.checkPress(position = position, press = press)
        settigs_window = button_settings.checkPress(position = position, press = press)
        quit = button_quit.checkPress(position = position, press = press)

        if wait_opponent_window:
            wait_opponent()
        if settigs_window:
            settings()
        if quit:
            pygame.quit()

        pygame.display.flip()
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

def wait_opponent():
    while True:
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

        ship1.ship_draw(screen= screen)
        ship1.move(position= position, press= press)

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
                pygame.quit()
    
def settings2():
    while True:
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
                pygame.quit()
    
    




