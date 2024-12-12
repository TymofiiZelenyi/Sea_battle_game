import pygame 
import time

from .basement import *
from .map import *
from .battle import battle

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

        position = pygame.mouse.get_pos()
        press = pygame.mouse.get_pressed()
        
        put_ships.button_draw(screen = screen)
        your_ships.button_draw(screen = screen)
        
        button_ready.button_draw(screen = screen)
        button_ready_window = button_ready.checkPress(position = position, press = press)

        if button_ready_window:
            battle()

        for ship in ship_list:
            ship.ship_draw(screen= screen)
            ship.move(position= position, press= press)

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
                            #умова, при якій кораблик поміщається в обрану клітинку
                            if ship.DIR and cell + ship.count_length <= 10 and placement_map2[row][cell] == 0 and not ship.WHERE:
                                if ship.count_length == 1:
                                    ship.x = item.x
                                    ship.y = item.y
                                    print(row, cell, placement_map2[row][cell], ship.WHERE)
                                    placement_map2[row][cell] = 1
                                    print(row, cell, placement_map2[row][cell], ship.WHERE)

                            elif ship.DIR and cell + ship.count_length <= 10 and placement_map2[row][cell] == 0 and ship.WHERE:
                                if ship.count_length == 1:
                                    ship.x = item.x
                                    ship.y = item.y
                                    print(last_row, last_cell, placement_map2[last_row][last_cell], ship.WHERE)
                                    placement_map2[last_row][last_cell] = 0
                                    print(last_row, last_cell, placement_map2[last_row][last_cell], ship.WHERE)
                                    print(row, cell, placement_map2[row][cell], ship.WHERE)
                                    placement_map2[row][cell] = 1
                                    print(row, cell, placement_map2[row][cell], ship.WHERE)

                            
                            #умова, при якій кораблик повертається на стартові координати, якщо клітинка зайнята                          
                            #умова, при якій кораблик повертається на стартові координати, якщо кораблик виходить за рамки поля.
                            elif ship.DIR and cell + ship.count_length > 10:
                                if ship.count_length == 1:
                                    print(row, cell, placement_map2[row][cell], ship.WHERE)
                                    placement_map2[row][cell] = 0
                                    print(row, cell, placement_map2[row][cell], ship.WHERE)
                                    ship.DIR =  True
                                    ship.x = ship.start_x
                                    ship.y = ship.start_y

                            elif ship.DIR and cell + ship.count_length <= 10 and placement_map2[row][cell] == 1:
                                if ship.count_length == 1:
                                    ship.DIR =  True
                                    ship.x = ship.start_x
                                    ship.y = ship.start_y
                                
                            
                            #перевірка кораблів та клітинок при вертикальному положенні кораблика.
                            #умова, при якій кораблик поміщається в обрану клітинку
                            if not ship.DIR and row + ship.count_length <= 10 and placement_map2[row][cell] == 0 and not ship.WHERE:
                                if ship.count_length == 1:
                                    ship.x = item.x
                                    ship.y = item.y
                                    print(row, cell, placement_map2[row][cell], ship.WHERE)
                                    placement_map2[row][cell] = 1
                                    print(row, cell, placement_map2[row][cell], ship.WHERE)

                            elif not ship.DIR and cell + ship.count_length <= 10 and placement_map2[row][cell] == 0 and ship.WHERE:
                                if ship.count_length == 1:
                                    ship.x = item.x
                                    ship.y = item.y
                                    print(last_row, last_cell, placement_map2[last_row][last_cell], ship.WHERE)
                                    placement_map2[last_row][last_cell] = 0
                                    print(last_row, last_cell, placement_map2[last_row][last_cell], ship.WHERE)
                                    print(row, cell, placement_map2[row][cell], ship.WHERE)
                                    placement_map2[row][cell] = 1
                                    print(row, cell, placement_map2[row][cell], ship.WHERE)

 
                            #умова, при якій кораблик повертається на стартові координати, якщо клітинка зайнята
                            #умова, при якій кораблик повертається на стартові координати, якщо кораблик виходить за рамки поля.  
                            elif not ship.DIR and row + ship.count_length > 10:
                                if ship.count_length == 1:
                                    ship.DIR =  True
                                    ship.x = ship.start_x
                                    ship.y = ship.start_y

                            elif not ship.DIR and row + ship.count_length <= 10 and placement_map2[row][cell] == 1:
                                if ship.count_length == 1:
                                    print(row, cell, placement_map2[row][cell], ship.WHERE)
                                    placement_map2[row][cell] = 0
                                    print(row, cell, placement_map2[row][cell], ship.WHERE)
                                    ship.DIR =  True
                                    ship.x = ship.start_x
                                    ship.y = ship.start_y
                        
                        
                        #умова, при якій наший кораблик повертається на стартові координати, якщо його ставлять за рамками поля.
                        elif ship.MOVE and not sq_list[0].collidepoint(position) and not press[2]:
                            item.CLOSE = False
                            ship.DIR =  True
                            ship.x = ship.start_x
                            ship.y = ship.start_y
                            print(f'"координати"{ship.x}, {ship.y}, {ship.count_length}, "горизонтальний:"{ship.DIR}, "Повернено із-за відсутності обраної клітинки" {item.CLOSE}')

                    number += 1
            
            if event.type == pygame.MOUSEBUTTONUP and not press[1] and not press[2]:
                number = 0
                for item in row_list:
                    for ship in ship_list:
                        if item.collidepoint(position) and ship.MOVE and sq_list[0].collidepoint(position):
                            cell = number % 10
                            row = number // 10               

                            #перевірка кораблів та клітинок при горизонтальному положенні кораблика.
                            
                            #умова, при якій кораблик поміщається в обрану клітинку
                            if ship.DIR and cell + ship.count_length <= 10 and ship.count_length == 1 and placement_map2[row][cell] == 0 and not ship.WHERE:
                                print("1")
                                ship.x = item.x
                                ship.y = item.y
                                placement_map2[row][cell] = 1
                                

                            elif ship.DIR and cell + ship.count_length <= 10 and ship.count_length > 1 and all(placement_map2[row][cell + i] == 0 for i in range(ship.count_length)) and not ship.WHERE:
                                print("2")
                                ship.x = item.x
                                ship.y = item.y
                                for i in range(ship.count_length):
                                    placement_map2[row][cell+i] = 1

                            elif ship.DIR and cell + ship.count_length <= 10 and ship.count_length == 1 and placement_map2[row][cell] == 0 and ship.WHERE:
                                print("3")
                                ship.x = item.x
                                ship.y = item.y
                                placement_map2[last_row][last_cell] = 0
                                placement_map2[row][cell] = 1
                                

                            elif ship.DIR and cell + ship.count_length <= 10 and ship.count_length > 1 and all(placement_map2[row][cell + i] == 0 for i in range(ship.count_length)) and ship.WHERE:
                                print("4")
                                ship.x = item.x
                                ship.y = item.y
                                for i in range(ship.count_length):
                                    placement_map2[last_row][last_cell+i] = 0
                                for i in range(ship.count_length):
                                    placement_map2[row][cell+i] = 1

                            elif ship.DIR and cell + ship.count_length <= 10 and ship.count_length == 1 and placement_map2[row][cell] == 1 and ship.WHERE:
                                print("5")
                                placement_map2[last_row][last_cell] = 0
                       
                                ship.DIR =  True
                                ship.x = ship.start_x
                                ship.y = ship.start_y  

                            elif ship.DIR and cell + ship.count_length <= 10 and ship.count_length > 1 and all(placement_map2[row][cell + i] == 1 for i in range(ship.count_length)) and ship.WHERE: 
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
                                
                            
                            elif ship.DIR and cell + ship.count_length > 10 and ship.count_length == 1 and ship.WHERE:
                                print("8")
                                placement_map2[last_row][last_cell] = 0
                        
                                ship.DIR =  True
                                ship.x = ship.start_x
                                ship.y = ship.start_y

                            elif ship.DIR and cell + ship.count_length > 10 and ship.count_length > 1 and ship.WHERE:
                                print("8/2")
                                for i in range(ship.count_length):
                                    placement_map2[last_row][last_cell+i] = 0
                        
                                ship.DIR =  True
                                ship.x = ship.start_x
                                ship.y = ship.start_y

                            elif ship.DIR and cell + ship.count_length <= 10 and ship.count_length == 1 and placement_map2[row][cell] == 1 and not ship.WHERE:
                                print("9")
                        
                                ship.DIR =  True
                                ship.x = ship.start_x
                                ship.y = ship.start_y
                                

                            elif ship.DIR and cell + ship.count_length <= 10 and ship.count_length > 1 and any(placement_map2[row][cell + i] == 1 for i in range(ship.count_length)) and not ship.WHERE:
                                print("10")
                        
                                ship.DIR =  True
                                ship.x = ship.start_x
                                ship.y = ship.start_y
                                

                            elif ship.DIR and cell + ship.count_length <= 10 and ship.count_length == 1 and placement_map2[row][cell] == 1 and ship.WHERE:
                                print("11")
                                placement_map2[row][cell] = 0  
                        
                                ship.DIR =  True
                                ship.x = ship.start_x
                                ship.y = ship.start_y

                            elif ship.DIR and cell + ship.count_length <= 10 and ship.count_length > 1 and any(placement_map2[row][cell + i] == 1 for i in range(ship.count_length)) and ship.WHERE:
                                print("12")
                                for i in range(ship.count_length):
                                    placement_map2[last_row][last_cell+i] = 0
                                    print(row, cell+i, placement_map2[row][cell+i], ship.WHERE)
                        
                                ship.DIR =  True
                                ship.x = ship.start_x
                                ship.y = ship.start_y
                                          
                            
                            #перевірка кораблів та клітинок при вертикальному положенні кораблика.
                            
                            #умова, при якій кораблик поміщається в обрану клітинку
                            if not ship.DIR and row + ship.count_length <= 10 and ship.count_length == 1 and placement_map2[row][cell] == 0 and not ship.WHERE:
                                print("not 1")
                                ship.x = item.x
                                ship.y = item.y                         
                                placement_map2[row][cell] = 1 

                            elif not ship.DIR and row + ship.count_length <= 10 and ship.count_length > 1 and all(placement_map2[row + i][cell] == 0 for i in range(ship.count_length)) and not ship.WHERE:
                                print("not 2")
                                ship.x = item.x
                                ship.y = item.y
                                for i in range(ship.count_length):
                                    placement_map2[row+i][cell] = 1                                  

                            elif not ship.DIR and row + ship.count_length <= 10 and ship.count_length == 1 and placement_map2[row][cell] == 0 and ship.WHERE:
                                print("not 3")
                                ship.x = item.x
                                ship.y = item.y                               
                                placement_map2[last_row][last_cell] = 0                        
                                placement_map2[row][cell] = 1

                            elif not ship.DIR and row + ship.count_length <= 10 and ship.count_length > 1 and all(placement_map2[row + i][cell] == 0 for i in range(ship.count_length)) and ship.WHERE:
                                print("not 4")
                                ship.x = item.x
                                ship.y = item.y
                                for i in range(ship.count_length):
                                    placement_map2[last_row+i][last_cell] = 0
                                for i in range(ship.count_length):
                                    placement_map2[row+i][cell] = 1
                                    

                            elif not ship.DIR and row + ship.count_length <= 10 and ship.count_length == 1 and placement_map2[row][cell] == 1 and ship.WHERE:                            
                                print("not 5")
                                placement_map2[last_row][last_cell] = 0                       
                        
                                ship.DIR =  True
                                ship.x = ship.start_x
                                ship.y = ship.start_y   

                            elif not ship.DIR and row + ship.count_length <= 10 and ship.count_length > 1 and all(placement_map2[row + i][cell] == 1 for i in range(ship.count_length)) and ship.WHERE: 
                                print("not 6")
                                for i in range(ship.count_length):
                                    placement_map2[last_row+i][last_cell] = 0
                        
                                ship.DIR = True
                                ship.x = ship.start_x
                                ship.y = ship.start_y                            
                                                 
                            #умова, при якій кораблик повертається на стартові координати, якщо кораблик виходить за рамки поля.
                            elif not ship.DIR and row + ship.count_length > 10 and ship.count_length == 1 and not ship.WHERE:
                                print("not 7")
                        
                                ship.DIR =  True
                                ship.x = ship.start_x
                                ship.y = ship.start_y
                            
                            elif not ship.DIR and row + ship.count_length > 10 and ship.count_length == 1 and ship.WHERE:                                 
                                print("not 8")
                                placement_map2[row][cell] = 0                                
                        
                                ship.DIR =  True
                                ship.x = ship.start_x
                                ship.y = ship.start_y
                            
                            elif not ship.DIR and row + ship.count_length > 10 and ship.count_length == 1 and ship.WHERE:
                                print("8/2")
                                for i in range(ship.count_length):
                                    placement_map2[last_row+i][last_cell] = 0
                        
                                ship.DIR =  True
                                ship.x = ship.start_x
                                ship.y = ship.start_y

                            elif not ship.DIR and row + ship.count_length <= 10 and ship.count_length == 1 and placement_map2[row][cell] == 1 and not ship.WHERE:
                                print("not 9")
                        
                                ship.DIR =  True
                                ship.x = ship.start_x
                                ship.y = ship.start_y

                            elif not ship.DIR and row + ship.count_length <= 10 and ship.count_length > 1 and any(placement_map2[row + i][cell] == 1 for i in range(ship.count_length)) and not ship.WHERE:
                                print("not 10")
                        
                                ship.DIR =  True
                                ship.x = ship.start_x
                                ship.y = ship.start_y

                            elif not ship.DIR and row + ship.count_length <= 10 and ship.count_length == 1 and placement_map2[row][cell] == 1:                               
                                print("not 11")
                                placement_map2[row][cell] = 0                              
                        
                                ship.DIR =  True
                                ship.x = ship.start_x
                                ship.y = ship.start_y
                            
                            elif not ship.DIR and row + ship.count_length <= 10 and ship.count_length > 1 and any(placement_map2[row + i][cell] == 1 for i in range(ship.count_length)) and ship.WHERE:
                                print("not 12")
                                for i in range(ship.count_length):
                                    placement_map2[last_row+i][last_cell] = 0
                        
                                ship.DIR =  True
                                ship.x = ship.start_x
                                ship.y = ship.start_y
                        
                        
                        #умова, при якій наший кораблик повертається на стартові координати, якщо його ставлять за рамками поля.
                        elif ship.MOVE and not sq_list[0].collidepoint(position) and not press[2] and not ship.WHERE:
                            print("13")
                    
                            ship.DIR =  True
                            ship.x = ship.start_x
                            ship.y = ship.start_y

                        elif ship.MOVE and not sq_list[0].collidepoint(position) and ship.count_length == 1 and not press[2] and ship.WHERE:
                            print("14")                         
                            placement_map2[last_row][last_cell] = 0 
                            
                            ship.DIR =  True
                            ship.x = ship.start_x
                            ship.y = ship.start_y

                        elif ship.DIR and ship.MOVE and not sq_list[0].collidepoint(position) and ship.count_length > 1 and not press[2] and ship.WHERE:
                            print("15")
                            print(ship.LAST_DIR)
                            for i in range(ship.count_length):
                                placement_map2[last_row][last_cell+i] = 0          
                            ship.DIR =  True
                            ship.x = ship.start_x
                            ship.y = ship.start_y

                        elif not ship.DIR and ship.MOVE and not sq_list[0].collidepoint(position) and ship.count_length > 1 and not press[2] and ship.WHERE:
                            print("15")
                            print(ship.LAST_DIR)
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