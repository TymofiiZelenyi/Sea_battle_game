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

def placement():
    run_placement = True
    
    x, y= 68, 142

    row_list = []
    cell_list = []

    for row in range(10):
        for cell in range(10):
            row_list.append(pygame.Rect(x, y, 60, 60))
            cell_list.append(pygame.Rect(x + 2, y + 2, 56, 56))
            x +=60
        y += 60
        x = 68


    while run_placement:
        screen.fill(MAIN_WINDOW_COLOR)

        #placemnt square
        pygame.draw.rect(screen, BUTTON_COLOR, (68, 142, PLACE_LENGTH, PLACE_LENGTH))
        #SHIPs bay
        pygame.draw.rect(screen, BUTTON_COLOR, (836, 142, SHIPS_BAY_LENGTH, SHIPS_BAY_LENGTH))

        for item in row_list:
            pygame.draw.rect(screen, BUTTON_COLOR, item)
        for item in cell_list:
            pygame.draw.rect(screen, MAIN_WINDOW_COLOR, item)

        position = pygame.mouse.get_pos()
        press = pygame.mouse.get_pressed()
        
        put_ships.button_draw(screen = screen)
        your_ships.button_draw(screen = screen)
        
        button_ready.button_draw(screen = screen)
        button_ready.checkPress(position = position, press = press)


        ship1.ship_draw(screen= screen)
        move_ship1 = ship1.move(position= position, press= press)

        ship2.ship_draw(screen= screen)
        move_ship2 = ship2.move(position= position, press= press)

        

        pygame.display.flip()
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                # if ship1.rect.collidepoint(position) and press[0] and press[2] and ship1.dir == "hor":
                #     ship1.dir = "ver"
                # if ship1.rect.collidepoint(position) and press[0] and press[2] and ship1.dir == "ver":
                #     ship1.dir = "hor"

                for item in row_list:
                    if item.collidepoint(position) and press[0] and move_ship1:
                        ship1.x = item.x
                        ship1.y = item.y
                    if item.collidepoint(position) and press[0] and move_ship2:
                        ship2.x = item.x
                        ship2.y = item.y
                    # if item.collidepoint(position) and press[0] and move_ship3:
                    #     ship3.x = item.x
                    #     ship3.y = item.y
                    # if item.collidepoint(position) and press[0] and move_ship4:
                    #     ship4.x = item.x
                    #     ship4.y = item.y
                    # if item.collidepoint(position) and press[0] and move_ship5:
                    #     ship5.x = item.x
                    #     ship5.y = item.y
                    # if item.collidepoint(position) and press[0] and move_ship6:
                    #     ship6.x = item.x
                    #     ship6.y = item.y
                    # if item.collidepoint(position) and press[0] and move_ship7:
                    #     ship1.x = item.x
                    #     ship1.y = item.y
                    # if item.collidepoint(position) and press[0] and move_ship8:
                    #     ship1.x = item.x
                    #     ship1.y = item.y
                    # if item.collidepoint(position) and press[0] and move_ship9:
                    #     ship1.x = item.x
                    #     ship1.y = item.y
                    # if item.collidepoint(position) and press[0] and move_ship10:
                    #     ship1.x = item.x
                    #     ship1.y = item.y
            if event.type == pygame.QUIT:
                run_placement = False

def battle():
    run_battle = True

    while run_battle:    
        screen.fill((MAIN_WINDOW_COLOR))
    
        #Наше поле (your screen)
        pygame.draw.rect(screen, BUTTON_COLOR, (50, 80, PLACE_LENGTH, PLACE_LENGTH), 0)
        #Поле противника (enemy screen)
        pygame.draw.rect(screen, BUTTON_COLOR, (750, 80, PLACE_LENGTH, PLACE_LENGTH), 0)

        pygame.display.flip()
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_battle = False

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
    
    




