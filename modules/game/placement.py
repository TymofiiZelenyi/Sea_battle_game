import pygame 
import time
import socket
import os

from .basement import *
from .map import *
from .battle import battle


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

        if button_ready_window:
            wait_opponent()

        for ship in ship_list:
            ship.ship_draw(screen= screen)
            ship.move(position= position, press= press, screen= screen)

        pygame.display.flip()
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and not press[1] and not press[2] and not press[0]:
                number = 0
                for item in row_list:
                    for ship in ship_list:
                        cell = number % 10
                        row = number // 10 
                        
                        ship.take_ship(position= position, press= press)
                        if item.collidepoint(position) and last:
                            last_cell = cell
                            last_row = row
                            last = False
                        else:
                            last = True

                    number += 1
            
            if event.type == pygame.MOUSEBUTTONUP and not press[1] and not press[2]:
                number = 0
                for item in row_list:
                    for ship in ship_list:
                        if item.collidepoint(position) and ship.MOVE and sq_list[0].collidepoint(position):
                            cell = number % 10
                            row = number // 10               

                            #перевірка кораблів та клітинок при горизонтальному положенні кораблика.
                            if ship.DIR and cell + ship.count_length <= 10 and all(placement_map2[row][cell + i] == 0 for i in range(ship.count_length)) and not ship.WHERE:
                                print("2")
                                ship.x = item.x
                                ship.y = item.y
                                for i in range(ship.count_length):
                                    placement_map2[row][cell+i] = 1                             

                            elif ship.DIR and cell + ship.count_length <= 10 and all(placement_map2[row][cell + i] == 0 for i in range(ship.count_length)) and ship.WHERE:
                                print("4")
                                ship.x = item.x
                                ship.y = item.y
                                for i in range(ship.count_length):
                                    placement_map2[last_row][last_cell+i] = 0
                                for i in range(ship.count_length):
                                    placement_map2[row][cell+i] = 1

                            elif ship.DIR and cell + ship.count_length <= 10 and any(placement_map2[row][cell + i] == 1 for i in range(ship.count_length)) and not ship.WHERE: 
                                print("6")
                                ship.DIR =  True
                                ship.x = ship.start_x
                                ship.y = ship.start_y 

                            elif ship.DIR and cell + ship.count_length <= 10 and any(placement_map2[row][cell + i] == 1 for i in range(ship.count_length)) and ship.WHERE: 
                                print("6")
                                for i in range(ship.count_length):
                                    placement_map2[last_row][last_cell+i] = 0
                                    print(row, cell+1,placement_map2[row][cell+1], ship.WHERE)
                        
                                ship.DIR =  True
                                ship.x = ship.start_x
                                ship.y = ship.start_y                   
                                                 
                            #умова, при якій кораблик повертається на стартові координати, якщо кораблик виходить за рамки поля.
                            elif ship.DIR and cell + ship.count_length > 10 and not ship.WHERE:
                                print("7")
                        
                                ship.DIR =  True
                                ship.x = ship.start_x
                                ship.y = ship.start_y
                                
                            
                            elif ship.DIR and cell + ship.count_length > 10 and  ship.WHERE:
                                print("8/2")
                                for i in range(ship.count_length):
                                    placement_map2[last_row][last_cell+i] = 0
                        
                                ship.DIR =  True
                                ship.x = ship.start_x
                                ship.y = ship.start_y


                            #перевірка кораблів та клітинок при горизонтальному положенні кораблика.
                            if not ship.DIR and row + ship.count_length <= 10 and all(placement_map2[row + i][cell] == 0 for i in range(ship.count_length)) and not ship.WHERE:
                                print("2")
                                ship.x = item.x
                                ship.y = item.y
                                for i in range(ship.count_length):
                                    placement_map2[row+i][cell] = 1                             

                            elif not ship.DIR and row + ship.count_length <= 10 and all(placement_map2[row + i][cell] == 0 for i in range(ship.count_length)) and ship.WHERE:
                                print("4")
                                ship.x = item.x
                                ship.y = item.y
                                for i in range(ship.count_length):
                                    placement_map2[last_row+i][last_cell] = 0
                                for i in range(ship.count_length):
                                    placement_map2[row+i][cell] = 1

                            elif not ship.DIR and row + ship.count_length <= 10 and any(placement_map2[row + i][cell] == 1 for i in range(ship.count_length)) and not ship.WHERE: 
                                print("6")
                                ship.DIR =  True
                                ship.x = ship.start_x
                                ship.y = ship.start_y 

                            elif not ship.DIR and row + ship.count_length <= 10 and any(placement_map2[row+1][cell] == 1 for i in range(ship.count_length)) and ship.WHERE: 
                                print("6")
                                for i in range(ship.count_length):
                                    placement_map2[last_row+1][last_cell] = 0
                                    print(row+1, cell,placement_map2[row+1][cell], ship.WHERE)
                        
                                ship.DIR =  True
                                ship.x = ship.start_x
                                ship.y = ship.start_y                   
                                                 
                            #умова, при якій кораблик повертається на стартові координати, якщо кораблик виходить за рамки поля.
                            elif not ship.DIR and row + ship.count_length > 10 and not ship.WHERE:
                                print("7")
                        
                                ship.DIR =  True
                                ship.x = ship.start_x
                                ship.y = ship.start_y
                                
                            
                            elif not ship.DIR and row + ship.count_length > 10 and ship.WHERE:
                                print("8/2")
                                for i in range(ship.count_length):
                                    placement_map2[last_row+i][last_cell] = 0
                        
                                ship.DIR =  True
                                ship.x = ship.start_x
                                ship.y = ship.start_y
                                          

                        
                        
                        #умова, при якій наший кораблик повертається на стартові координати, якщо його ставлять за рамками поля.

                        elif ship.DIR and ship.MOVE and not sq_list[0].collidepoint(position) and  not press[2] and ship.WHERE:
                            for i in range(ship.count_length):
                                placement_map2[last_row][last_cell+i] = 0          
                            ship.DIR =  True
                            ship.x = ship.start_x
                            ship.y = ship.start_y

                        elif not ship.DIR and ship.MOVE and not sq_list[0].collidepoint(position) and  not press[2] and ship.WHERE:
                            for i in range(ship.count_length):
                                placement_map2[last_row+i][last_cell] = 0          
                            ship.DIR =  True
                            ship.x = ship.start_x
                            ship.y = ship.start_y
                        
                    number += 1      
            
            if event.type == pygame.MOUSEBUTTONUP and press[2]:
                for ship in ship_list:
                    if ship.MOVE:
                        ship.DIR = not ship.DIR  
            
            if event.type == pygame.QUIT:
                run_placement = False
                pygame.quit()


def wait_opponent():
    # with socket.socket(family = socket.AF_INET , type = socket.SOCK_STREAM) as client_socket:
    #     # Підключаємо клієнта  до локального IP та порту
    #     client_socket.connect(("195.248.167.137", 8090))

    #     client_socket.sendall(placement_map2.encode())


    run_wait_opponent = True

    while run_wait_opponent:
        screen.fill(MAIN_WINDOW_COLOR)
        
        position = pygame.mouse.get_pos()
        press = pygame.mouse.get_pressed()

        wait_opponent_text.button_draw(screen = screen)
        # button_back_menu.button_draw(screen = screen)
        
        placement_window = wait_opponent_text.checkPress(position = position, press = press)
        if placement_window:
            battle()
        
        pygame.display.flip()
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_wait_opponent = False
                pygame.quit()