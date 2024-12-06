import pygame 
import time

from .basement import *
from .map import *

def battle():
    run_battle = True
    time.sleep(0.3)
    
    turn = True

    #Наше поле (your screen)
    sq_your = pygame.Rect((70, 180, PLACE_LENGTH, PLACE_LENGTH))
    #Поле противника (enemy screen)
    sq_enemy = pygame.Rect((730, 180, PLACE_LENGTH, PLACE_LENGTH))

    sq_list = [sq_your,  sq_enemy]

    miss_list =[]
    hit_list = []

    x1, y1 = 70, 180
    x2, y2 = 730, 180
    
    row_list_player = []
    cell_list_player = []

    row_list_enemy = []
    cell_list_enemy = []
    
    def map(row, cell, number):     
        if row == 0:
            if cell != 0 and cell !=9:      
                miss_list.append(pygame.Rect(row_list_enemy[number+ 9].x + 25, row_list_enemy[number+ 9].y + 25, 10, 10))
                miss_list.append(pygame.Rect(row_list_enemy[number+ 10].x + 25, row_list_enemy[number+ 10].y + 25, 10, 10))
                miss_list.append(pygame.Rect(row_list_enemy[number+ 11].x + 25, row_list_enemy[number+ 11].y + 25, 10, 10))
                row_list_enemy[number+ 9].CLOSE = True
                row_list_enemy[number+ 10].CLOSE = True 
                row_list_enemy[number+ 11].CLOSE = True 
                
                miss_list.append(pygame.Rect(row_list_enemy[number- 1].x + 25, row_list_enemy[number- 1].y + 25, 10, 10))
                row_list_enemy[number- 1].CLOSE = True

                miss_list.append(pygame.Rect(row_list_enemy[number+ 1].x + 25, row_list_enemy[number+ 1].y + 25, 10, 10)) 
                row_list_enemy[number+ 1].CLOSE = True

            elif cell == 9:
                miss_list.append(pygame.Rect(row_list_enemy[number+ 9].x + 25, row_list_enemy[number+ 9].y + 25, 10, 10))
                miss_list.append(pygame.Rect(row_list_enemy[number+ 10].x + 25, row_list_enemy[number+ 10].y + 25, 10, 10))
                row_list_enemy[number+ 9].CLOSE = True
                row_list_enemy[number+ 10].CLOSE = True

                miss_list.append(pygame.Rect(row_list_enemy[number- 1].x + 25, row_list_enemy[number- 1].y + 25, 10, 10))
                row_list_enemy[number- 1].CLOSE = True

            elif cell == 0:
                miss_list.append(pygame.Rect(row_list_enemy[number+ 11].x + 25, row_list_enemy[number+ 11].y + 25, 10, 10))
                miss_list.append(pygame.Rect(row_list_enemy[number+ 10].x + 25, row_list_enemy[number+ 10].y + 25, 10, 10))
                row_list_enemy[number+ 11].CLOSE = True
                row_list_enemy[number+ 10].CLOSE = True

                miss_list.append(pygame.Rect(row_list_enemy[number+ 1].x + 25, row_list_enemy[number+ 1].y + 25, 10, 10))
                row_list_enemy[number+ 1].CLOSE = True


        elif row == 9:
            if cell != 0 and cell !=9:
                miss_list.append(pygame.Rect(row_list_enemy[number- 9].x + 25, row_list_enemy[number- 9].y + 25, 10, 10))
                miss_list.append(pygame.Rect(row_list_enemy[number- 10].x + 25, row_list_enemy[number- 10].y + 25, 10, 10))
                miss_list.append(pygame.Rect(row_list_enemy[number- 11].x + 25, row_list_enemy[number- 11].y + 25, 10, 10))
                row_list_enemy[number- 9].CLOSE = True 
                row_list_enemy[number- 10].CLOSE = True
                row_list_enemy[number- 11].CLOSE = True              

                miss_list.append(pygame.Rect(row_list_enemy[number- 1].x + 25, row_list_enemy[number- 1].y + 25, 10, 10))
                row_list_enemy[number- 1].CLOSE = True

                miss_list.append(pygame.Rect(row_list_enemy[number+ 1].x + 25, row_list_enemy[number+ 1].y + 25, 10, 10)) 
                row_list_enemy[number+ 1].CLOSE = True
            
            elif cell == 0:
                miss_list.append(pygame.Rect(row_list_enemy[number- 10].x + 25, row_list_enemy[number- 10].y + 25, 10, 10))
                miss_list.append(pygame.Rect(row_list_enemy[number- 9].x + 25, row_list_enemy[number- 9].y + 25, 10, 10))
                row_list_enemy[number- 10].CLOSE = True
                row_list_enemy[number- 9].CLOSE = True 

                miss_list.append(pygame.Rect(row_list_enemy[number+ 1].x + 25, row_list_enemy[number+ 1].y + 25, 10, 10)) 
                row_list_enemy[number+ 1].CLOSE = True 

            elif cell == 9:
                miss_list.append(pygame.Rect(row_list_enemy[number- 11].x + 25, row_list_enemy[number- 11].y + 25, 10, 10))
                miss_list.append(pygame.Rect(row_list_enemy[number- 10].x + 25, row_list_enemy[number- 10].y + 25, 10, 10))
                row_list_enemy[number- 11].CLOSE = True 
                row_list_enemy[number- 10].CLOSE = True

                miss_list.append(pygame.Rect(row_list_enemy[number- 1].x + 25, row_list_enemy[number- 1].y + 25, 10, 10))
                row_list_enemy[number- 1].CLOSE = True

        elif row != 0 and row != 9 and  cell == 0 and player_map2[row][cell+1] == 0 and player_map2[row-1][cell] == 0 and player_map2[row+1][cell] == 0:
            miss_list.append(pygame.Rect(row_list_enemy[number+ 10].x + 25, row_list_enemy[number+ 10].y + 25, 10, 10))
            miss_list.append(pygame.Rect(row_list_enemy[number+ 11].x + 25, row_list_enemy[number+ 11].y + 25, 10, 10))
            row_list_enemy[number+ 10].CLOSE = True 
            row_list_enemy[number+ 11].CLOSE = True

            miss_list.append(pygame.Rect(row_list_enemy[number- 10].x + 25, row_list_enemy[number- 10].y + 25, 10, 10))
            miss_list.append(pygame.Rect(row_list_enemy[number- 9].x + 25, row_list_enemy[number- 9].y + 25, 10, 10))
            row_list_enemy[number- 10].CLOSE = True
            row_list_enemy[number- 9].CLOSE = True 

            miss_list.append(pygame.Rect(row_list_enemy[number+ 1].x + 25, row_list_enemy[number+ 1].y + 25, 10, 10)) 
            row_list_enemy[number+ 1].CLOSE = True

        elif row != 0 and row != 9 and cell == 9 and player_map2[row][cell-1] == 0 and player_map2[row-1][cell] == 0 and player_map2[row+1][cell] == 0:
            miss_list.append(pygame.Rect(row_list_enemy[number+ 10].x + 25, row_list_enemy[number+ 10].y + 25, 10, 10))
            miss_list.append(pygame.Rect(row_list_enemy[number+ 9].x + 25, row_list_enemy[number+ 9].y + 25, 10, 10))
            row_list_enemy[number+ 10].CLOSE = True 
            row_list_enemy[number+ 9].CLOSE = True

            miss_list.append(pygame.Rect(row_list_enemy[number- 10].x + 25, row_list_enemy[number- 10].y + 25, 10, 10))
            miss_list.append(pygame.Rect(row_list_enemy[number- 11].x + 25, row_list_enemy[number- 11].y + 25, 10, 10))
            row_list_enemy[number- 10].CLOSE = True
            row_list_enemy[number- 11].CLOSE = True 

            miss_list.append(pygame.Rect(row_list_enemy[number- 1].x + 25, row_list_enemy[number- 1].y + 25, 10, 10)) 
            row_list_enemy[number- 1].CLOSE = True

        elif player_map2[row][cell] == 2 and player_map2[row][cell-1] == 0 and player_map2[row-1][cell] == 0 and player_map2[row+1][cell] == 0:
            miss_list.append(pygame.Rect(row_list_enemy[number+ 9].x + 25, row_list_enemy[number+ 9].y + 25, 10, 10))
            miss_list.append(pygame.Rect(row_list_enemy[number+ 10].x + 25, row_list_enemy[number+ 10].y + 25, 10, 10))
            miss_list.append(pygame.Rect(row_list_enemy[number+ 11].x + 25, row_list_enemy[number+ 11].y + 25, 10, 10))
            row_list_enemy[number+ 9].CLOSE = True
            row_list_enemy[number+ 10].CLOSE = True 
            row_list_enemy[number+ 11].CLOSE = True

            miss_list.append(pygame.Rect(row_list_enemy[number- 9].x + 25, row_list_enemy[number- 9].y + 25, 10, 10))
            miss_list.append(pygame.Rect(row_list_enemy[number- 10].x + 25, row_list_enemy[number- 10].y + 25, 10, 10))
            miss_list.append(pygame.Rect(row_list_enemy[number- 11].x + 25, row_list_enemy[number- 11].y + 25, 10, 10))
            row_list_enemy[number- 9].CLOSE = True 
            row_list_enemy[number- 10].CLOSE = True
            row_list_enemy[number- 11].CLOSE = True 

            miss_list.append(pygame.Rect(row_list_enemy[number- 1].x + 25, row_list_enemy[number- 1].y + 25, 10, 10))
            row_list_enemy[number- 1].CLOSE = True

            miss_list.append(pygame.Rect(row_list_enemy[number+ 1].x + 25, row_list_enemy[number+ 1].y + 25, 10, 10)) 
            row_list_enemy[number+ 1].CLOSE = True        
        number +=1

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
            number1 +=1

        for item in cell_list_player:
            pygame.draw.rect(screen, MAIN_WINDOW_COLOR, item)

        number2 = 0 
        for item in row_list_enemy:
            cell = number2 % 10
            row = number2 // 10
            if player_map2[row][cell] == 0:
                pygame.draw.rect(screen, BUTTON_COLOR, item)
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
            
            if event.type == pygame.MOUSEBUTTONUP and press[1]:
                number = 0
                for item in row_list_enemy:
                    row = number // 10
                    cell = number % 10
                    if item.collidepoint(position):
                        print(row, cell, player_map2[row][cell])
                    
                    number += 1                    
            
            if event.type == pygame.MOUSEBUTTONUP and press[0] and not press[1] and not press[2]:
                number = 0
                for item in row_list_enemy:          
                    cell = number % 10
                    row = number // 10           

                    if item.collidepoint(position) and sq_list[1].collidepoint(position) and player_map2[row][cell] == 1 and not item.CLOSE and turn: 
                        hit_list.append(pygame.Rect(item.x + 15, item.y + 15, 30, 30))         
                        print(f"Изменение player_map2[{row}][{cell}] до: {player_map2[row][cell]}")
                        player_map2[row][cell] = 2
                        print(f"Изменение player_map2[{row}][{cell}] после: {player_map2[row][cell]}")                    
                        item.CLOSE = True
                        map(row, cell, number)
                   
                    elif item.collidepoint(position) and sq_list[1].collidepoint(position) and player_map2[row][cell] == 0 and not item.CLOSE and turn:
                        miss_list.append(pygame.Rect(item.x + 25, item.y + 25, 10, 10))
                        # turn = False
                        item.CLOSE = True   
                        print("Поле врага: Не попал", row , cell , player_map2[row][cell])     

                    number +=1

            #Працюємо з нашим полем
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

