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