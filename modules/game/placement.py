import pygame 
import os

from .basement import *
from .map import *
from .wait_opponent import wait_opponent

data = read_json(fd="settings.json")

MAIN_WINDOW_COLOR = data["main"]["MAIN_WINDOW_COLOR"]
HEAD_COLOR = data["color"]["HEAD_COLOR"]
PLACE_LENGTH = data["color"]["PLACE_LENGTH"]
SHIPS_BAY_LENGTH = data["color"]["SHIPS_BAY_LENGTH"]
BUTTON_COLOR = data["button"]["COLOR"]
FPS = data["main"]["FPS"]

def placement():
    run_placement = True
    
    x, y = 68, 142
    number = 0

    big_sq = pygame.Rect(68, 142, PLACE_LENGTH, PLACE_LENGTH)
    small_sq = pygame.Rect(836, 142, SHIPS_BAY_LENGTH + 30, SHIPS_BAY_LENGTH)

    bg = pygame.image.load(os.path.abspath(__file__ + "/../../../image/bg/battle_field.png"))
    bg = pygame.transform.scale(bg, [PLACE_LENGTH, PLACE_LENGTH])

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

    last = True
    last_row = 0 
    last_cell =0

    while run_placement:
        screen.fill(MAIN_WINDOW_COLOR)
        
        for sq in sq_list:
            pygame.draw.rect(screen, BUTTON_COLOR, sq)
        for item in row_list:
            pygame.draw.rect(screen, BUTTON_COLOR, item)
        for item in cell_list:
            pygame.draw.rect(screen, MAIN_WINDOW_COLOR, item)

        screen.blit(bg, (68, 142))

        position = pygame.mouse.get_pos()
        press = pygame.mouse.get_pressed()
        
        put_ships.button_draw(screen = screen)
        your_ships.button_draw(screen = screen)
        
        button_ready.button_draw(screen = screen)
        button_ready_window = button_ready.checkPress(position = position, press = press)

        if button_ready_window and any(ship.STAY for ship in ship_list):
            res = wait_opponent()
            if res == "BACK":
                return "HOME"

        for ship in ship_list:
            ship.ship_draw(screen= screen)
            ship.move(position= position, press= press, screen= screen)

        pygame.display.flip()
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and not press[1] and not press[2]:
                print("TAKE")
                number = 0
                for item in row_list:
                    for ship in ship_list:
                        cell = number % 10
                        row = number // 10 
                        
                        ship.take_ship(position= position, press= press)
                        if item.collidepoint(position) and ship.WHERE and last:
                            last_cell = cell
                            last_row = row
                            last = False
                        else:
                            last = True

                    number += 1
            
            
            if event.type == pygame.MOUSEBUTTONDOWN and not press[1] and not press[2]:
                print("REBUT")
                number = 0
                for item in row_list:
                    for ship in ship_list:
                        cell = number % 10
                        row = number // 10 
                        
                        if ship.rect.collidepoint(position) and ship.WHERE and last:
                            if ship.count_length == 1:
                                player_map1[last_row][last_cell] = 0
                            if ship.count_length != 1 and ship.DIR:
                                for i in range(ship.count_length):
                                    player_map1[last_row][last_cell+i] = 0
                            if ship.count_length != 1 and not ship.DIR:
                                for i in range(ship.count_length):
                                    player_map1[last_row+i][last_cell] = 0

                    number += 1
            
            if event.type == pygame.MOUSEBUTTONUP and not press[1] and not press[2]:
                print("PUT DOWN")
                number = 0
                for item in row_list:
                    for ship in ship_list:
                        if item.collidepoint(position) and ship.MOVE and sq_list[0].collidepoint(position):
                            cell = number % 10
                            row = number // 10               

                            #перевірка кораблів та клітинок при горизонтальному положенні кораблика.
                            if ship.DIR and cell + ship.count_length <= 10 and all(player_map1[row][cell + i] == 0 for i in range(ship.count_length)) and not ship.WHERE:
                                ship.STAY = True 
                                print("ИЗ СТАВИМ В НА ПУСТЫЕ КЛЕТКИ")
                                ship.x = item.x
                                ship.y = item.y
                                for i in range(ship.count_length):
                                    player_map1[row][cell+i] = 1
                                    print(player_map1[row][cell+i])                            

                            elif ship.DIR and cell + ship.count_length <= 10 and all(player_map1[row][cell + i] == 0 for i in range(ship.count_length)) and ship.WHERE:
                                ship.STAY = True
                                print("В НА ПУСТЫЕ")
                                ship.x = item.x
                                ship.y = item.y
                                for i in range(ship.count_length):
                                    player_map1[row][cell+i] = 1

                            elif ship.DIR and cell + ship.count_length <= 10 and any(player_map1[row][cell + i] == 1 for i in range(ship.count_length)) and not ship.WHERE: 
                                print("ИЗ СТАВИМ В ВОЗВРАТ")
                                ship.STAY = False 
                                ship.DIR =  True
                                ship.x = ship.start_x
                                ship.y = ship.start_y 

                            elif ship.DIR and cell + ship.count_length <= 10 and any(player_map1[row][cell + i] == 1 for i in range(ship.count_length)) and ship.WHERE: 
                                print("В ВОЗВРАТ")  
                                ship.STAY = False                 
                                ship.DIR =  True
                                ship.x = ship.start_x
                                ship.y = ship.start_y                   
                                                 
                            #умова, при якій кораблик повертається на стартові координати, якщо кораблик виходить за рамки поля.
                            elif ship.DIR and cell + ship.count_length > 10 and not ship.WHERE:
                                print("ИЗ OVER")  
                                ship.STAY = False                    
                                ship.DIR =  True
                                ship.x = ship.start_x
                                ship.y = ship.start_y
                                
                            
                            elif ship.DIR and cell + ship.count_length > 10 and  ship.WHERE:
                                print("В OVER")  
                                ship.STAY = False 
                                ship.DIR =  True
                                ship.x = ship.start_x
                                ship.y = ship.start_y


                            #перевірка кораблів та клітинок при горизонтальному положенні кораблика.
                            if not ship.DIR and row + ship.count_length <= 10 and all(player_map1[row + i][cell] == 0 for i in range(ship.count_length)) and not ship.WHERE:
                                ship.STAY = True
                                print("ИЗ СТАВИМ В НА ПУСТЫЕ КЛЕТКИ")
                                ship.x = item.x
                                ship.y = item.y
                                for i in range(ship.count_length):
                                    player_map1[row+i][cell] = 1                             

                            elif not ship.DIR and row + ship.count_length <= 10 and all(player_map1[row + i][cell] == 0 for i in range(ship.count_length)) and ship.WHERE:
                                ship.STAY = True
                                print("В НА ПУСТЫЕ")
                                ship.x = item.x
                                ship.y = item.y
                                for i in range(ship.count_length):
                                    player_map1[row+i][cell] = 1

                            elif not ship.DIR and row + ship.count_length <= 10 and any(player_map1[row + i][cell] == 1 for i in range(ship.count_length)) and not ship.WHERE: 
                                print("ИЗ СТАВИМ В ВОЗВРАТ")
                                ship.STAY = False 
                                ship.DIR =  True
                                ship.x = ship.start_x
                                ship.y = ship.start_y 

                            elif not ship.DIR and row + ship.count_length <= 10 and any(player_map1[row+1][cell] == 1 for i in range(ship.count_length)) and ship.WHERE: 
                                print("В ВОЗВРАТ") 
                                ship.STAY = False                    
                                ship.DIR =  True
                                ship.x = ship.start_x
                                ship.y = ship.start_y                   
                                                 
                            #умова, при якій кораблик повертається на стартові координати, якщо кораблик виходить за рамки поля.
                            elif not ship.DIR and row + ship.count_length > 10 and not ship.WHERE:
                                print("ИЗ OVER") 
                                ship.STAY = False                       
                                ship.DIR =  True
                                ship.x = ship.start_x
                                ship.y = ship.start_y
                                
                            
                            elif not ship.DIR and row + ship.count_length > 10 and ship.WHERE:
                                print("В OVER") 
                                ship.STAY = False                      
                                ship.DIR =  True
                                ship.x = ship.start_x
                                ship.y = ship.start_y
                                          

                        
                        
                        #умова, при якій наший кораблик повертається на стартові координати, якщо його ставлять за рамками поля.

                        elif ship.MOVE and not sq_list[0].collidepoint(position) and not press[2]:
                            print("OUT")  
                            ship.STAY = False       
                            ship.DIR =  True
                            ship.x = ship.start_x
                            ship.y = ship.start_y
                        
                    number += 1      
            
            if event.type == pygame.MOUSEBUTTONUP and press[2] and not press[1]:
                for ship in ship_list:
                    if ship.MOVE:
                        ship.LAST_DIR = ship.DIR
                        ship.DIR = not ship.DIR  
            
            if event.type == pygame.QUIT:
                run_placement = False
                pygame.quit()

