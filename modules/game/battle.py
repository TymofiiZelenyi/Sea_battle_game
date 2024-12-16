import pygame 
import time
import os
from .basement import *
from .map import *

# x, y = pygame.mouse.get_pos()
# x -= mouse_cursor.get_width()/2
# y -= mouse_cursor.get_height()/2
# screen.blit(mouse_cursor, (x, y))

def battle():
    run_battle = True
    
    turn = True

    #Наше поле (your screen)
    sq_your = pygame.Rect((70, 180, PLACE_LENGTH, PLACE_LENGTH))
    #Поле противника (enemy screen)
    sq_enemy = pygame.Rect((730, 180, PLACE_LENGTH, PLACE_LENGTH))

    bg = pygame.image.load(os.path.abspath(__file__ + "/../../../image/bg/battle_field.png"))
    bg = pygame.transform.scale(bg, [PLACE_LENGTH, PLACE_LENGTH])

    hit = pygame.image.load(os.path.abspath(__file__ + "/../../../image/cell/hit_enemy.png"))
    miss = pygame.image.load(os.path.abspath(__file__ + "/../../../image/cell/kill_enemy.png"))

    sq_list = [sq_your,  sq_enemy]

    miss_list =[]
    hit_list = []

    x1, y1 = 70, 180
    x2, y2 = 730, 180
    
    row_list_player = []
    cell_list_player = []

    row_list_enemy = []
    cell_list_enemy = []
        
    def check(player_map, enemy_map):
        if all(cell != 1 for row in player_map for cell in row):
            print("YOU WIN")
        
        elif all(cell != 1 for row in enemy_map for cell in row):
            print("YOU LOSE")

    def finder(row, cell):
        #########################
 
        if row != 0 and row != 9 and cell != 0 and cell != 9 and player_map2[row][cell] == 2 and player_map2[row][cell+1] == 0 and player_map2[row][cell-1] == 0 and player_map2[row+1][cell] == 0 and player_map2[row-1][cell] == 0:
            type = "solo"
            return type

        if row == 0 and cell != 0 and cell != 9 and player_map2[row][cell] == 2 and player_map2[row][cell+1] == 0 and player_map2[row][cell-1] == 0 and player_map2[row+1][cell] == 0:
            type = "solo"
            return type

        if row == 9 and cell != 0 and cell != 9 and player_map2[row][cell] == 2 and player_map2[row][cell+1] == 0 and player_map2[row][cell-1] == 0 and player_map2[row-1][cell] == 0:
            type = "solo"
            return type
        
        if cell == 0 and row != 0 and row != 9 and player_map2[row][cell] == 2 and player_map2[row][cell+1] == 0 and player_map2[row+1][cell] == 0 and player_map2[row-1][cell] == 0:
            type = "solo"
            return type

        if cell == 9 and row != 0 and row != 9 and player_map2[row][cell] == 2 and player_map2[row][cell-1] == 0 and player_map2[row+1][cell] == 0 and player_map2[row-1][cell] == 0:
            type = "solo"
            return type
        
        if cell == 0 and row == 0 and player_map2[row][cell] == 2 and player_map2[row][cell+1] == 0 and player_map2[row+1][cell] == 0:
            type = "solo"
            return type

        if cell == 0 and row == 9 and player_map2[row][cell] == 2 and player_map2[row][cell+1] == 0 and player_map2[row-1][cell] == 0:
            type = "solo"
            return type

        if cell == 9 and row == 0 and player_map2[row][cell] == 2 and player_map2[row][cell-1] == 0 and player_map2[row+1][cell] == 0:
            type = "solo"
            return type

        if cell == 9 and row == 9 and player_map2[row][cell] == 2 and player_map2[row][cell-1] == 0 and player_map2[row-1][cell] == 0:
            type = "solo"
            return type
     
        #########################

        if row != 0 and row != 9 and cell != 0 and cell != 9 and cell != 8 and player_map2[row][cell] == 2 and player_map2[row][cell+1] == 2 and player_map2[row][cell+2] == 0 and player_map2[row][cell-1] == 0 and player_map2[row+1][cell] == 0 and player_map2[row-1][cell] == 0:
            type = "duo left"
            return type

        if row == 0 and cell != 0 and cell != 1 and cell != 9 and cell != 8 and player_map2[row][cell] == 2 and player_map2[row][cell+1] == 2 and player_map2[row][cell-1] == 0 and player_map2[row][cell+2] == 0 and player_map2[row+1][cell] == 0:
            print("HELLO")
            type = "duo left"
            return type

        if row == 9 and cell != 0 and cell != 9 and cell != 8 and player_map2[row][cell] == 2 and player_map2[row][cell+1] == 2 and player_map2[row][cell+2] == 0 and player_map2[row][cell-1] == 0 and player_map2[row-1][cell] == 0:
            print("ыгзук toфафафxa")
            type = "duo left"
            return type

        if row != 0 and row != 9 and cell == 0 and player_map2[row][cell] == 2 and player_map2[row][cell+1] == 2 and player_map2[row][cell+2] == 0 and player_map2[row+1][cell] == 0 and player_map2[row-1][cell] == 0:
            print("ыгзук toxa")
            type = "duo left"
            return type

        if row != 9 and row != 0 and cell == 8 and player_map2[row][cell] == 2 and player_map2[row][cell+1] == 2 and player_map2[row][cell-1] == 0 and player_map2[row-1][cell] == 0 and player_map2[row+1][cell] == 0:
            print("toxa")
            type = "duo left"
            return type
      
        if row == 0 and cell == 0  and player_map2[row][cell-1] == 0 and player_map2[row][cell] == 2 and player_map2[row+1][cell] == 0 and player_map2[row][cell+2] == 0 and player_map2[row][cell+1] == 2:
            print("tttttttt")
            type = "duo left"
            return type

        if row == 0 and player_map2[row][cell] == 2 and player_map2[row+1][cell] == 0 and player_map2[row][cell-1] == 2 and player_map2[row][cell+1] == 2 and player_map2[row][cell-2] == 0:
            print("toxa1")
            type = "duo left"
            return type

        if row == 9 and cell == 0 and player_map2[row][cell] == 2 and player_map2[row][cell+1] == 2 and player_map2[row-1][cell] == 0 and player_map2[row][cell+2] == 0:
            print("toxa2")
            type = "duo left"
            return type

        if row == 9 and cell == 8 and player_map2[row][cell] == 2 and player_map2[row][cell+1] == 2 and player_map2[row-1][cell] == 0 and player_map2[row][cell-1] == 2 and player_map2[row][cell-2] == 0:
            print("toxa3")
            type = "duo left"
            return type

        ######################### 
        
        if row != 0 and row != 9 and cell != 1 and cell != 9 and player_map2[row][cell] == 2 and player_map2[row][cell-1] == 2 and player_map2[row][cell-2] == 0 and player_map2[row][cell+1] == 0 and player_map2[row+1][cell] == 0 and player_map2[row-1][cell] == 0:
            type = "duo right"
            return type

        if row == 0 and cell != 1 and cell != 2 and cell != 9 and player_map2[row][cell] == 2 and player_map2[row][cell-1] == 2 and player_map2[row][cell-2] == 0 and player_map2[row][cell+1] == 0 and player_map2[row+1][cell] == 0:
            type = "duo right"
            return type

        if row == 9 and cell != 1 and cell != 2 and cell != 9 and cell != 8 and player_map2[row][cell] == 2 and player_map2[row][cell-1] == 2 and player_map2[row][cell-2] == 0 and player_map2[row][cell+1] == 0 and player_map2[row-1][cell] == 0:
            type = "duo right"
            return type

        if row != 0 and row != 9 and cell == 1 and player_map2[row][cell] == 2 and player_map2[row][cell-1] == 2 and  player_map2[row][cell+1] == 0 and player_map2[row+1][cell] == 0 and player_map2[row-1][cell] == 0:
            type = "duo right"
            return type

        if row != 9 and row != 0 and cell == 9 and player_map2[row][cell] == 2 and player_map2[row][cell-1] == 2 and player_map2[row][cell-2] == 0 and player_map2[row-1][cell] == 0 and player_map2[row+1][cell] == 0:
            type = "duo right"
            return type
      
        if row == 0 and cell == 1 and player_map2[row][cell] == 2 and player_map2[row][cell-1] == 2 and player_map2[row+1][cell] == 0 and player_map2[row][cell+1] == 0:
            print("LEFT TOP")
            type = "duo right"
            return type

        if row == 0 and cell == 9 and player_map2[row][cell] == 2 and player_map2[row][cell-1] == 2 and player_map2[row+1][cell] == 0 and player_map2[row][cell-2] == 0:
            print("RIGHT TOP")
            type = "duo right"
            return type

        if row == 9 and cell == 1 and player_map2[row][cell] == 2 and player_map2[row][cell-1] == 2 and player_map2[row-1][cell] == 0 and player_map2[row][cell+1] == 0:
            print("LEFT BUTTON")
            type = "duo right"
            return type

        if row == 9 and cell == 9 and player_map2[row][cell] == 2 and player_map2[row][cell-1] == 2 and player_map2[row-1][cell] == 0 and player_map2[row][cell-2] == 0:
            print("RIGHT BUTTON")
            type = "duo right"
            return type

        
        ###########################

        if cell != 0 and cell != 9 and row !=0 and row !=8 and row != 9 and player_map2[row][cell] == 2 and player_map2[row+1][cell] == 2 and player_map2[row+2][cell] == 0 and player_map2[row-1][cell] == 0 and player_map2[row][cell+1] == 0 and player_map2[row][cell-1] == 0:
            type = "duo top"
            return type

        if cell != 0 and cell !=9 and row == 0 and player_map2[row][cell] == 2 and player_map2[row+1][cell] == 2 and player_map2[row+2][cell] == 0 and player_map2[row][cell-1] == 0 and player_map2[row][cell-1] == 0:
            type = "duo top"
            return type

        if cell != 0 and cell !=9 and row == 8 and player_map2[row][cell] == 2 and player_map2[row+1][cell] == 2 and  player_map2[row-1][cell] == 0 and player_map2[row][cell-1] == 0 and player_map2[row][cell+1] == 0:
            type = "duo top"
            return type

        if cell == 0 and row != 0 and row != 8 and row != 9 and player_map2[row][cell] == 2 and player_map2[row+1][cell] == 2 and player_map2[row+2][cell] == 0 and player_map2[row-1][cell] == 0 and player_map2[row][cell+1] == 0:
            type = "duo top"
            return type
            
        if cell == 9 and row != 0 and row != 8 and row != 9 and player_map2[row][cell] == 2 and player_map2[row+1][cell] == 2 and player_map2[row+2][cell] == 0 and player_map2[row-1][cell] == 0 and player_map2[row][cell-1] == 0:
            type = "duo top"
            return type

        if cell == 0 and row == 0 and player_map2[row][cell] == 2 and player_map2[row+1][cell] == 2 and player_map2[row+2][cell] == 0 and player_map2[row][cell+1] == 0:
            print("duo top 1")
            type = "duo top"
            return type

        if cell == 9 and row == 0 and player_map2[row][cell] == 2 and player_map2[row+1][cell] == 2 and player_map2[row+2][cell] == 0 and player_map2[row][cell-1] == 0:
            print("duo top 2 ")
            type = "duo top"
            return type

        if cell == 0 and row == 8 and player_map2[row][cell] == 2 and player_map2[row+1][cell] == 2 and player_map2[row-1][cell] == 0 and player_map2[row][cell+1] == 0:
            print("duo top 3")
            type = "duo top"
            return type

        if cell == 9 and row == 8 and player_map2[row][cell] == 2 and player_map2[row+1][cell] == 2 and player_map2[row-1][cell] == 0 and player_map2[row-1][cell] == 0:
            print("duo top 4")
            type = "duo top"
            return type
        
        #########################   
        
        if cell != 0 and cell != 9 and row !=0 and row !=1 and row != 9 and player_map2[row][cell] == 2 and player_map2[row-1][cell] == 2 and player_map2[row-2][cell] == 0 and player_map2[row+1][cell] == 0 and player_map2[row][cell+1] == 0 and player_map2[row][cell-1] == 0:
            type = "duo button"
            return type

        if cell != 0 and cell !=9 and row == 1 and player_map2[row][cell] == 2 and player_map2[row-1][cell] == 2  and player_map2[row+1][cell] == 0  and player_map2[row][cell+1] == 0 and player_map2[row][cell-1] == 0:
            type = "duo button"
            return type

        if  cell != 0 and cell !=9 and row == 9 and player_map2[row][cell] == 2 and player_map2[row-1][cell] == 2 and player_map2[row-2][cell] == 0  and player_map2[row][cell+1] == 0 and player_map2[row][cell-1] == 0:
            type = "duo button"
            return type

        if row != 1 and row != 9 and row != 0 and row != 8 and cell == 0 and player_map2[row][cell] == 2 and player_map2[row-1][cell] == 2 and player_map2[row-2][cell] == 0 and player_map2[row+1][cell] == 0 and player_map2[row][cell+1] == 0:
            type = "duo button"
            return type

        if row != 1 and row != 9 and row != 0 and row != 8 and cell == 9 and player_map2[row][cell] == 2 and player_map2[row-1][cell] == 2 and player_map2[row-2][cell] == 0 and player_map2[row][cell-1] == 0 and player_map2[row+1][cell] == 0:
            type = "duo button"
            return type

        if row == 1 and cell == 0 and player_map2[row][cell] == 2 and player_map2[row-1][cell] == 2 and player_map2[row+1][cell] == 0 and player_map2[row][cell+1] == 0:
            type = "duo button"
            return type

        if row == 1 and cell == 9 and player_map2[row][cell] == 2 and player_map2[row-1][cell] == 2 and player_map2[row+1][cell] == 0 and player_map2[row][cell-1] == 0:
            type = "duo button"
            return type

        if row == 9 and cell == 0 and player_map2[row][cell] == 2 and player_map2[row-1][cell] == 2 and player_map2[row-2][cell] == 0 and player_map2[row][cell+1] == 0:
            type = "duo button"
            return type

        if row == 9 and cell == 9 and player_map2[row][cell] == 2 and player_map2[row-1][cell] == 2 and player_map2[row-2][cell] == 0 and player_map2[row][cell-1] == 0:
            type = "duo button"
            return type
        
        #########################

        if row != 0 and row != 9 and cell !=0 and cell != 9 and cell != 1 and cell !=  8 and cell != 2 and cell !=  7 and player_map2[row][cell] == 2 and player_map2[row][cell-1] == 2 and player_map2[row][cell+1] == 2 and player_map2[row][cell-2] == 0 and player_map2[row][cell+2] == 0 and player_map2[row+1][cell] == 0 and player_map2[row-1][cell] == 0: 
            type = "trio center" 
            return type 
     
        if cell != 8 and cell != 9 and player_map2[row][cell] == 2 and player_map2[row][cell-1] == 2 and player_map2[row][cell+1] == 2 and player_map2[row][cell-2] == 0:  
            type = "trio center" 
            return type

        if cell != 0 and cell != 1 and cell != 8 and cell != 9 and player_map2[row][cell] == 2 and player_map2[row][cell-1] == 2 and player_map2[row][cell+1] == 2 and player_map2[row][cell+2] == 0:  
            type = "trio center" 
            return type

        if row == 0 and cell != 0 and cell != 1 and cell != 8 and cell != 9 and player_map2[row][cell] == 2 and player_map2[row][cell-1] == 2 and player_map2[row][cell+1] == 2 and player_map2[row][cell+2] == 0 and player_map2[row][cell+1] == 2 and player_map2[row][cell-2] == 0 and player_map2[row +1][cell] == 0:  
            type = "trio center" 
            return type

        if row != 9 and cell != 0 and cell != 1 and cell != 8 and cell != 9 and player_map2[row][cell] == 2 and player_map2[row][cell-1] == 2 and player_map2[row][cell+1] == 2 and player_map2[row][cell+2] == 0 and player_map2[row][cell+1] == 2 and player_map2[row][cell-2] == 0 and player_map2[row -1][cell] == 0:  
            type = "trio center" 
            return type

        if row == 0 and cell == 2 and player_map2[row][cell] == 2 and player_map2[row][cell-1] == 2 and player_map2[row][cell+1] == 2 and player_map2[row][cell+2] == 0 and player_map2[row+1][cell] == 0:
            type = "trio center" 
            return type

        if row == 0 and cell == 8 and player_map2[row][cell] == 2 and player_map2[row][cell-1] == 2 and player_map2[row][cell+1] == 2 and player_map2[row][cell-2] == 0 and player_map2[row+1][cell] == 0:
            type = "trio center" 
            return type

        if row == 9 and cell == 2 and player_map2[row][cell] == 2 and player_map2[row][cell-1] == 2 and player_map2[row][cell+1] == 2 and player_map2[row][cell+2] == 0 and player_map2[row-1][cell] == 0:
            type = "trio center" 
            return type

        if row == 9 and cell == 8 and player_map2[row][cell] == 2 and player_map2[row][cell-1] == 2 and player_map2[row][cell+1] == 2 and player_map2[row][cell-2] == 0 and player_map2[row-1][cell] == 0:
            type = "trio center" 
            return type
               
    def map(row, cell, number, type):
        if type == "trio center": 
            if row != 0: 
                miss_list.append(pygame.Rect(row_list_enemy[number- 10].x + 25, row_list_enemy[number- 10].y + 25, 10, 10)) 
                row_list_enemy[number- 10].CLOSE = True 
                miss_list.append(pygame.Rect(row_list_enemy[number- 11].x + 25, row_list_enemy[number- 11].y + 25, 10, 10)) 
                row_list_enemy[number- 11].CLOSE = True 
                miss_list.append(pygame.Rect(row_list_enemy[number- 9].x + 25, row_list_enemy[number- 9].y + 25, 10, 10)) 
                row_list_enemy[number- 9].CLOSE = True 
            if row != 9: 
                miss_list.append(pygame.Rect(row_list_enemy[number+ 10].x + 25, row_list_enemy[number+ 10].y + 25, 10, 10)) 
                row_list_enemy[number+ 10].CLOSE = True 
                miss_list.append(pygame.Rect(row_list_enemy[number+ 11].x + 25, row_list_enemy[number+ 11].y + 25, 10, 10)) 
                row_list_enemy[number+ 11].CLOSE = True 
                miss_list.append(pygame.Rect(row_list_enemy[number+ 9].x + 25, row_list_enemy[number+ 9].y + 25, 10, 10)) 
                row_list_enemy[number+ 9].CLOSE = True 
            if cell !=0 and cell != 1 : 
                miss_list.append(pygame.Rect(row_list_enemy[number- 2].x + 25, row_list_enemy[number- 2].y + 25, 10, 10)) 
                row_list_enemy[number- 2].CLOSE = True 
            if  cell != 8 and cell != 9: 
                miss_list.append(pygame.Rect(row_list_enemy[number+ 2].x + 25, row_list_enemy[number+ 2].y + 25, 10, 10)) 
                row_list_enemy[number+ 2].CLOSE = True 
            if cell !=0 and cell != 1 and  row != 0: 
                miss_list.append(pygame.Rect(row_list_enemy[number- 12].x + 25, row_list_enemy[number- 12].y + 25, 10, 10)) 
                row_list_enemy[number- 12].CLOSE = True 
            if  cell != 8 and cell != 9 and row != 0: 
                miss_list.append(pygame.Rect(row_list_enemy[number- 8].x + 25, row_list_enemy[number- 8].y + 25, 10, 10)) 
                row_list_enemy[number- 8].CLOSE = True 
            if cell !=0 and cell != 1 and row != 9: 
                miss_list.append(pygame.Rect(row_list_enemy[number+8].x + 25, row_list_enemy[number+8].y + 25, 10, 10)) 
                row_list_enemy[number+ 8].CLOSE = True 
            if  cell != 8 and cell != 9 and row != 9: 
                miss_list.append(pygame.Rect(row_list_enemy[number+12].x + 25, row_list_enemy[number+12].y + 25, 10, 10)) 
                row_list_enemy[number+ 12].CLOSE = True
        
        elif type == "duo top":
            if row != 8:
                miss_list.append(pygame.Rect(row_list_enemy[number+ 20].x + 25, row_list_enemy[number+ 20].y + 25, 10, 10))
                row_list_enemy[number+ 20].CLOSE = True 
                print("BUTTON")
            if row != 0:
                miss_list.append(pygame.Rect(row_list_enemy[number- 10].x + 25, row_list_enemy[number- 10].y + 25, 10, 10))
                row_list_enemy[number- 10].CLOSE = True
                print("TOP")
            if cell != 0:
                miss_list.append(pygame.Rect(row_list_enemy[number- 1].x + 25, row_list_enemy[number- 1].y + 25, 10, 10))
                row_list_enemy[number- 1].CLOSE = True
                miss_list.append(pygame.Rect(row_list_enemy[number+9].x + 25, row_list_enemy[number+ 9].y + 25, 10, 10))
                row_list_enemy[number+ 9].CLOSE = True
                print("LEFT")
            if cell != 9:
                miss_list.append(pygame.Rect(row_list_enemy[number+ 1].x + 25, row_list_enemy[number+ 1].y + 25, 10, 10)) 
                row_list_enemy[number+ 1].CLOSE = True 
                miss_list.append(pygame.Rect(row_list_enemy[number+ 11].x + 25, row_list_enemy[number+ 11].y + 25, 10, 10))
                row_list_enemy[number+ 11].CLOSE = True
                print("RIGHT")
            if cell != 0 and row != 0:
                miss_list.append(pygame.Rect(row_list_enemy[number- 11].x + 25, row_list_enemy[number- 11].y + 25, 10, 10))
                row_list_enemy[number- 11].CLOSE = True 
                print("LEFT TOP")
            if cell != 9 and row != 0 :
                miss_list.append(pygame.Rect(row_list_enemy[number- 9].x + 25, row_list_enemy[number- 9].y + 25, 10, 10))
                row_list_enemy[number- 9].CLOSE = True 
                print("RIGHT TOP")
            if cell != 0 and row != 8:
                miss_list.append(pygame.Rect(row_list_enemy[number+ 19].x + 25, row_list_enemy[number+ 19].y + 25, 10, 10))
                row_list_enemy[number+ 19].CLOSE = True
                print("LEFT BUTTON")
            if cell != 9 and row !=8:
                miss_list.append(pygame.Rect(row_list_enemy[number+ 21].x + 25, row_list_enemy[number+ 21].y + 25, 10, 10))
                row_list_enemy[number+ 21].CLOSE = True
                print("RIGHR BUTTON")
            
        elif type == "duo button":
            if row != 9:
                miss_list.append(pygame.Rect(row_list_enemy[number+ 10].x + 25, row_list_enemy[number+ 10].y + 25, 10, 10))
                row_list_enemy[number+ 10].CLOSE = True 
                print("BUTTON")
            if row != 0 and row != 1:
                miss_list.append(pygame.Rect(row_list_enemy[number- 20].x + 25, row_list_enemy[number- 20].y + 25, 10, 10))
                row_list_enemy[number- 20].CLOSE = True
                print("TOP")
            if cell != 0:
                miss_list.append(pygame.Rect(row_list_enemy[number- 1].x + 25, row_list_enemy[number- 1].y + 25, 10, 10))
                row_list_enemy[number- 1].CLOSE = True
                miss_list.append(pygame.Rect(row_list_enemy[number- 11].x + 25, row_list_enemy[number- 11].y + 25, 10, 10))
                row_list_enemy[number- 11].CLOSE = True
                print("LEFT")
            if cell != 9:
                miss_list.append(pygame.Rect(row_list_enemy[number+ 1].x + 25, row_list_enemy[number+ 1].y + 25, 10, 10)) 
                row_list_enemy[number+ 1].CLOSE = True 
                miss_list.append(pygame.Rect(row_list_enemy[number- 9].x + 25, row_list_enemy[number- 9].y + 25, 10, 10))
                row_list_enemy[number- 9].CLOSE = True
                print("RIGHT")
            if cell != 0 and row != 0 and row != 1:
                miss_list.append(pygame.Rect(row_list_enemy[number- 21].x + 25, row_list_enemy[number- 21].y + 25, 10, 10))
                row_list_enemy[number- 21].CLOSE = True 
                print("LEFT TOP")
            if cell != 9 and row != 0 and row != 1:
                miss_list.append(pygame.Rect(row_list_enemy[number- 19].x + 25, row_list_enemy[number- 19].y + 25, 10, 10))
                row_list_enemy[number- 19].CLOSE = True 
                print("RIGHT TOP")
            if cell != 0 and row != 9:
                miss_list.append(pygame.Rect(row_list_enemy[number+ 9].x + 25, row_list_enemy[number+ 9].y + 25, 10, 10))
                row_list_enemy[number+ 9].CLOSE = True
                print("LEFT BUTTON")
            if cell != 9 and row !=9:
                miss_list.append(pygame.Rect(row_list_enemy[number+ 11].x + 25, row_list_enemy[number+ 11].y + 25, 10, 10))
                row_list_enemy[number+ 11].CLOSE = True
                print("RIGHR BUTTON")
        
        elif type == "duo right":
            if row != 0:
                miss_list.append(pygame.Rect(row_list_enemy[number- 11].x + 25, row_list_enemy[number- 11].y + 25, 10, 10))
                row_list_enemy[number- 11].CLOSE = True
                miss_list.append(pygame.Rect(row_list_enemy[number- 10].x + 25, row_list_enemy[number- 10].y + 25, 10, 10))
                row_list_enemy[number- 10].CLOSE = True 
            if row != 9:  
                miss_list.append(pygame.Rect(row_list_enemy[number+ 10].x + 25, row_list_enemy[number+ 10].y + 25, 10, 10))
                row_list_enemy[number+ 10].CLOSE = True 
                miss_list.append(pygame.Rect(row_list_enemy[number+ 9].x + 25, row_list_enemy[number+ 9].y + 25, 10, 10))
                row_list_enemy[number+ 9].CLOSE = True 
            if cell != 0 and cell != 1:   
                miss_list.append(pygame.Rect(row_list_enemy[number- 2].x + 25, row_list_enemy[number- 2].y + 25, 10, 10))
                row_list_enemy[number- 2].CLOSE = True
            if cell != 8 and cell != 9:
                miss_list.append(pygame.Rect(row_list_enemy[number+ 1].x + 25, row_list_enemy[number+ 1].y + 25, 10, 10)) 
                row_list_enemy[number+ 1].CLOSE = True
            if cell != 0 and cell != 1 and row != 0:
                miss_list.append(pygame.Rect(row_list_enemy[number- 12].x + 25, row_list_enemy[number- 12].y + 25, 10, 10))
                row_list_enemy[number- 12].CLOSE = True 
                print("LEFT TOP")
            if cell != 8 and cell != 9 and row != 0:
                miss_list.append(pygame.Rect(row_list_enemy[number- 9].x + 25, row_list_enemy[number- 9].y + 25, 10, 10))
                row_list_enemy[number- 9].CLOSE = True 
                print("RIGHT TOP")
            if  cell != 1 and cell != 0 and row != 9:
                miss_list.append(pygame.Rect(row_list_enemy[number+ 8].x + 25, row_list_enemy[number+ 8].y + 25, 10, 10))
                row_list_enemy[number+ 8].CLOSE = True
                print("LEFT BUTTON")
            if cell != 8 and cell != 9 and row !=9:
                miss_list.append(pygame.Rect(row_list_enemy[number+ 11].x + 25, row_list_enemy[number+ 11].y + 25, 10, 10))
                row_list_enemy[number+ 11].CLOSE = True
                print("RIGHR BUTTON")
        
        elif type == "duo left":
            if row != 0:
                miss_list.append(pygame.Rect(row_list_enemy[number- 10].x + 25, row_list_enemy[number- 10].y + 25, 10, 10))
                row_list_enemy[number- 10].CLOSE = True
                miss_list.append(pygame.Rect(row_list_enemy[number- 9].x + 25, row_list_enemy[number- 9].y + 25, 10, 10))
                row_list_enemy[number- 9].CLOSE = True 
                print("TOP")
            if row != 9:  
                miss_list.append(pygame.Rect(row_list_enemy[number+ 10].x + 25, row_list_enemy[number+ 10].y + 25, 10, 10))
                row_list_enemy[number+ 10].CLOSE = True 
                miss_list.append(pygame.Rect(row_list_enemy[number+ 11].x + 25, row_list_enemy[number+ 11].y + 25, 10, 10))
                row_list_enemy[number+ 11].CLOSE = True 
                print("BUTTON")
            if cell != 0:   
                miss_list.append(pygame.Rect(row_list_enemy[number- 1].x + 25, row_list_enemy[number- 1].y + 25, 10, 10))
                row_list_enemy[number- 1].CLOSE = True
                print("LEFT")
            if cell != 8 and cell != 9:
                miss_list.append(pygame.Rect(row_list_enemy[number+ 2].x + 25, row_list_enemy[number+ 2].y + 25, 10, 10)) 
                row_list_enemy[number+ 2].CLOSE = True
                print("RIGHT")
            if cell != 0 and row != 0:
                miss_list.append(pygame.Rect(row_list_enemy[number- 11].x + 25, row_list_enemy[number- 11].y + 25, 10, 10))
                row_list_enemy[number- 11].CLOSE = True 
                print("LEFT TOP")
            if cell != 8 and cell != 9 and row != 0:
                miss_list.append(pygame.Rect(row_list_enemy[number- 8].x + 25, row_list_enemy[number- 8].y + 25, 10, 10))
                row_list_enemy[number- 8].CLOSE = True 
                print("RIGHT TOP")
            if cell != 8 and cell != 0 and row != 9:
                miss_list.append(pygame.Rect(row_list_enemy[number+ 9].x + 25, row_list_enemy[number+ 9].y + 25, 10, 10))
                row_list_enemy[number+ 9].CLOSE = True
                print("LEFT BUTTON")
            if cell != 8 and cell != 9 and row !=9:
                miss_list.append(pygame.Rect(row_list_enemy[number+ 12].x + 25, row_list_enemy[number+ 12].y + 25, 10, 10))
                row_list_enemy[number+ 12].CLOSE = True
                print("RIGHR BUTTON")
            
        elif type == "solo":
            if row != 9 and player_map2[row+1][cell] == 0:
                miss_list.append(pygame.Rect(row_list_enemy[number+ 10].x + 25, row_list_enemy[number+ 10].y + 25, 10, 10))
                row_list_enemy[number+ 10].CLOSE = True 
                print("BUTTON")
            if row != 0 and player_map2[row-1][cell] == 0:
                miss_list.append(pygame.Rect(row_list_enemy[number- 10].x + 25, row_list_enemy[number- 10].y + 25, 10, 10))
                row_list_enemy[number- 10].CLOSE = True
                print("TOP")
            if cell != 0 and player_map2[row][cell-1] == 0:
                miss_list.append(pygame.Rect(row_list_enemy[number- 1].x + 25, row_list_enemy[number- 1].y + 25, 10, 10))
                row_list_enemy[number- 1].CLOSE = True
                print("LEFT")
            if cell != 9 and player_map2[row][cell+1] == 0:
                miss_list.append(pygame.Rect(row_list_enemy[number+ 1].x + 25, row_list_enemy[number+ 1].y + 25, 10, 10)) 
                row_list_enemy[number+ 1].CLOSE = True 
                print("RIGHT")
            if cell != 0 and row != 0:
                miss_list.append(pygame.Rect(row_list_enemy[number- 11].x + 25, row_list_enemy[number- 11].y + 25, 10, 10))
                row_list_enemy[number- 11].CLOSE = True 
                print("LEFT TOP")
            if cell != 9 and row != 0 :
                miss_list.append(pygame.Rect(row_list_enemy[number- 9].x + 25, row_list_enemy[number- 9].y + 25, 10, 10))
                row_list_enemy[number- 9].CLOSE = True 
                print("RIGHT TOP")
            if cell != 0 and row != 9:
                miss_list.append(pygame.Rect(row_list_enemy[number+ 9].x + 25, row_list_enemy[number+ 9].y + 25, 10, 10))
                row_list_enemy[number+ 9].CLOSE = True
                print("LEFT BUTTON")
            if cell != 9 and row !=9:
                miss_list.append(pygame.Rect(row_list_enemy[number+ 11].x + 25, row_list_enemy[number+ 11].y + 25, 10, 10))
                row_list_enemy[number+ 11].CLOSE = True
                print("RIGHR BUTTON")
    
    
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

    time.sleep(0.3) 

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
            pygame.draw.rect(screen, MAIN_WINDOW_COLOR, item)\
            
        screen.blit(bg, (70, 180))
        screen.blit(bg, (730, 180))
       
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
            screen.blit(miss, (item.x, item.y))
        
        for item in hit_list:
            screen.blit(hit, (item.x, item.y))
            # pygame.draw.rect(screen, "black", item)

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
                        hit = Point(item.x, item.y) 
                        hit_list.append(hit)     
                        print(f"Изменение player_map2[{row}][{cell}] до: {player_map2[row][cell]}")
                        player_map2[row][cell] = 2
                        print(f"Изменение player_map2[{row}][{cell}] после: {player_map2[row][cell]}")                    
                        item.CLOSE = True
                        type = finder(row, cell)
                        map(row, cell, number, type)
                        check(player_map2, player_map1)
                   
                    elif item.collidepoint(position) and sq_list[1].collidepoint(position) and player_map2[row][cell] == 0 and not item.CLOSE and turn:
                        miss = Point(item.x, item.y)
                        miss_list.append(miss)
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

def win():
    while True:
        screen.fill((MAIN_WINDOW_COLOR))
        position = pygame.mouse.get_pos()
        press = pygame.mouse.get_pressed()
        text_win.text_draw(screen=screen)
        button_back_menu.button_draw(screen=screen)
        back_to_menu = button_back_menu.checkPress(position = position, press = press)

        if back_to_menu:
            pass

def lose():
    while True:
        screen.fill((MAIN_WINDOW_COLOR))
        position = pygame.mouse.get_pos()
        press = pygame.mouse.get_pressed()
        text_lose.text_draw(screen=screen)
        button_back_menu.button_draw(screen=screen)
        back_to_menu = button_back_menu.checkPress(position = position, press = press)
    
        if back_to_menu:
            pass