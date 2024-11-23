import pygame 
from .ships import *
from .button import *
from .settings import *
from .map import *

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

def placement():
    run_placement = True
    
    x, y = 68, 142
    number = 0

    big_sq = pygame.Rect(68, 142, PLACE_LENGTH, PLACE_LENGTH)
    small_sq = pygame.Rect(836, 142, SHIPS_BAY_LENGTH + 30, SHIPS_BAY_LENGTH)

    sq_list = [big_sq, small_sq]
    row_list = []
    cell_list = []

    for row in range(10):
        for cell in range(10):
            row_list.append(RectBetter(x, y, 60, 60, False))
            cell_list.append(pygame.Rect(x + 2, y + 2, 56, 56))
            x +=60
        y += 60
        x = 68


    while run_placement:
        screen.fill(MAIN_WINDOW_COLOR)
        
        for sq in sq_list:
            pygame.draw.rect(screen, BUTTON_COLOR, sq)
        for item in row_list:
            pygame.draw.rect(screen, BUTTON_COLOR, item)
        for item in cell_list:
            pygame.draw.rect(screen, MAIN_WINDOW_COLOR, item)

        position = pygame.mouse.get_pos()
        press = pygame.mouse.get_pressed()
        
        put_ships.button_draw(screen = screen)
        your_ships.button_draw(screen = screen)
        
        button_ready.button_draw(screen = screen)
        button_ready_window = button_ready.checkPress(position = position, press = press)

        

        for ship in ship_list:
            ship.ship_draw(screen= screen)
            ship.move(position= position, press= press)

        pygame.display.flip()
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and not press[1] and not press[2] and not press[0]:
                for ship in ship_list:
                    ship.take_ship(position= position, press= press)

            if event.type == pygame.MOUSEBUTTONUP and not press[1] and not press[2]:
                number = 0
                for item in row_list:
                    for ship in ship_list:
                        if item.collidepoint(position) and ship.MOVE and sq_list[0].collidepoint(position):
                            cell = number % 10
                            row = number // 10               

                        #перевірка кораблів та клітинок при горизонтальному положенні кораблика.
                            #умова, при якій кораблик поміщається в обрану клітинку
                            if ship.DIR and cell + ship.count_length <= 10 and not item.CLOSE:
                                ship.x = item.x
                                ship.y = item.y
                                item.CLOSE = True
                                # for count in range(ship.count_length):
                                #     player_map1.append[row][cell](1)
                                print(f'"координати"{ship.x}, {ship.y}, {ship.count_length}, "горизонтальний:"{ship.DIR}, "Поставили" {item.CLOSE}')
                            
                            #умова, при якій кораблик повертається на стартові координати, якщо клітинка зайнята
                            
                            #умова, при якій кораблик повертається на стартові координати, якщо кораблик виходить за рамки поля.
                            elif ship.DIR and cell + ship.count_length > 10 and item.CLOSE or ship.DIR and cell + ship.count_length <= 10 and item.CLOSE:
                                item.CLOSE = False
                                ship.DIR =  True
                                ship.x = ship.start_x
                                ship.y = ship.start_y
                                print(f'"координати"{ship.x}, {ship.y}, {ship.count_length}, "горизонтальний:"{ship.DIR}, "ПОВЕРНЕНО" {item.CLOSE}')
                            
                            
                        #перевірка кораблів та клітинок при вертикальному положенні кораблика.
                            #умова, при якій кораблик поміщається в обрану клітинку
                            if not ship.DIR and row + ship.count_length <= 10 and not item.CLOSE:
                                ship.x = item.x
                                ship.y = item.y
                                item.CLOSE = True
                                print(f'"координати"{ship.x}, {ship.y}, {ship.count_length}, "горизонтальний:"{ship.DIR}, "Поставили"{item.CLOSE}')

                            #умова, при якій кораблик повертається на стартові координати, якщо клітинка зайнята

                            #умова, при якій кораблик повертається на стартові координати, якщо кораблик виходить за рамки поля.  
                            elif not ship.DIR and row + ship.count_length > 10 and item.CLOSE or not ship.DIR and row + ship.count_length <= 10 and item.CLOSE:
                                item.CLOSE = False
                                ship.DIR =  True
                                ship.x = ship.start_x
                                ship.y = ship.start_y
                                print(f'"координати"{ship.x}, {ship.y}, {ship.count_length}, "горизонтальний:"{ship.DIR}, "ПОВЕРНЕНО" {item.CLOSE}')
                        
                        #умова, при якій наший кораблик повертається на стартові координати, якщо його ставлять за рамками поля.
                        elif ship.MOVE and not sq_list[0].collidepoint(position) and not press[2]:
                            item.CLOSE = False
                            ship.DIR =  True
                            ship.x = ship.start_x
                            ship.y = ship.start_y
                            print(f'"координати"{ship.x}, {ship.y}, {ship.count_length}, "горизонтальний:"{ship.DIR}, "Повернено із-за відсутності обраної клітинки" {item.CLOSE}')
                    number += 1
            if button_ready_window:
                battle()
            
            if event.type == pygame.MOUSEBUTTONUP and press[2]:
                for ship in ship_list:
                    if ship.MOVE:
                        ship.DIR = not ship.DIR  
            
            if event.type == pygame.QUIT:
                run_placement = False
                pygame.quit()

def battle():
    run_battle = True

    turn = True

    #Наше поле (your screen)
    sq_yuor = pygame.Rect((70, 180, PLACE_LENGTH, PLACE_LENGTH))
    #Поле противника (enemy screen)
    sq_enemy = pygame.Rect((730, 180, PLACE_LENGTH, PLACE_LENGTH))

    sq_list = [sq_yuor,  sq_enemy]

    miss_list =[]
    hit_list = []

    x1, y1 = 70, 180
    x2, y2 = 730, 180
    
    row_list_player = []
    cell_list_player = []

    row_list_enemy = []
    cell_list_enemy = []

    for row in range(10):
        for cell in range(10):
            row_list_player.append(RectBetter(x1, y1, 60, 60, False))
            cell_list_player.append(pygame.Rect(x1 + 2, y1 + 2, 56, 56))
            x1 +=60
        y1 += 60
        x1 = 70

    for row in range(10):
        for cell in range(10):
            row_list_enemy.append(RectBetter(x2, y2, 60, 60, False))
            cell_list_enemy.append(pygame.Rect(x2 + 2, y2 + 2, 56, 56))
            x2 +=60
        y2 += 60
        x2 = 730

    while run_battle:    
        screen.fill((MAIN_WINDOW_COLOR))

        your_screen_text.button_draw(screen=screen)
        enemy_screen_text.button_draw(screen=screen)

        position = pygame.mouse.get_pos()
        press = pygame.mouse.get_pressed()

        for sq in sq_list:
            pygame.draw.rect(screen, BUTTON_COLOR, sq)

        number1 = 0 
        for item in row_list_player:
            cell = number1 % 10
            row = number1 // 10
            if player_map1[row][cell] == 0:
                pygame.draw.rect(screen, BUTTON_COLOR, item)
            # elif player_map1[row][cell] == 1:         
            #     pygame.draw.rect(screen, "yellow", item)
            number1 +=1

        for item in cell_list_player:
            pygame.draw.rect(screen, MAIN_WINDOW_COLOR, item)

        number2 = 0 
        for item in row_list_enemy:
            cell = number2 % 10
            row = number2 // 10
            if player_map2[row][cell] == 0:
                pygame.draw.rect(screen, BUTTON_COLOR, item)
            # if player_map2[row][cell] == 1:
            #     pygame.draw.rect(screen, "green", item)
            number2 += 1

        for item in cell_list_enemy:
            pygame.draw.rect(screen, MAIN_WINDOW_COLOR, item)
       
        number1 = 0 
        for item in row_list_player:
            cell = number1 % 10
            row = number1 // 10
            if player_map1[row][cell] == 1:
                pygame.draw.rect(screen, "yellow", item)
            number1 += 1

        number2 = 0 
        for item in row_list_enemy:
            cell = number2 % 10
            row = number2 // 10
            if player_map2[row][cell] == 1:
                pygame.draw.rect(screen, "green", item)
            number2 += 1
        
        for item in miss_list:
            pygame.draw.rect(screen, "black", item)
        
        for item in hit_list:
            pygame.draw.rect(screen, "black", item)

        pygame.display.flip()
        clock.tick(FPS)       
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and turn and not press[1] and not press[2]:
                number = 0
                for item in row_list_enemy: 
                    
                    cell = number % 10
                    row = number // 10                

                    if item.collidepoint(position) and sq_list[1].collidepoint(position) and player_map2[row][cell] == 1 and not item.CLOSE:
                        hit_list.append(pygame.Rect(item.x + 10, item.y + 10, 40, 40))
                        print("Поле врага: Попал")
                        print(row, cell)
                        turn = True
                        item.CLOSE = True
                    elif item.collidepoint(position) and sq_list[1].collidepoint(position) and player_map2[row][cell] == 0 and not item.CLOSE:
                        miss_list.append(pygame.Rect(item.x + 25, item.y + 25, 10, 10))
                        print("Поле врага: Не попал")
                        print(row, cell)
                        turn =False
                        item.CLOSE = True
                    
                    number += 1
            
            if event.type == pygame.MOUSEBUTTONUP and not press[1] and not press[2]:
                number = 0
                for item in row_list_player: 
                    cell = number % 10
                    row = number // 10                
                    
                    if item.collidepoint(position) and sq_list[0].collidepoint(position):
                        print("Это ваше поле")
                        print(row, cell)
            
            if event.type == pygame.QUIT:
                run_battle = False
                pygame.quit()

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
    
    




