import socket
import pygame 
import os
import json

from threading import Thread

from .basement import *
from .map import *

data = read_json(fd="settings.json")

PLACE_LENGTH = data["color"]["PLACE_LENGTH"]
FPS = data["main"]["FPS"]

def battle():
    run_battle = True

    player_map2 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    
    turn = False

    #Наше поле (your screen)
    sq_your = pygame.Rect((70, 180, PLACE_LENGTH, PLACE_LENGTH))
    #Поле противника (enemy screen)
    sq_enemy = pygame.Rect((730, 180, PLACE_LENGTH, PLACE_LENGTH))

    bg = pygame.image.load(os.path.abspath(__file__ + "/../../../image/bg/battle_field.png"))
    bg = pygame.transform.scale(bg, [PLACE_LENGTH, PLACE_LENGTH])

    hit = pygame.image.load(os.path.abspath(__file__ + "/../../../image/cell/hit.png"))
    hit = pygame.transform.scale(hit, [60,60])
    
    miss = pygame.image.load(os.path.abspath(__file__ + "/../../../image/cell/miss.png"))
    miss = pygame.transform.scale(miss, [60, 60])

    sq_list = [sq_your,  sq_enemy]

    miss_list =[]
    hit_list = []

    x1, y1 = 70, 180
    x2, y2 = 730, 180
    
    row_list_player = []
    cell_list_player = []

    row_list_enemy = []
    cell_list_enemy = []

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect_to():
            print("1")
            client_socket.connect(("192.168.1.106", 8081))
            print("connect")
        
    def sending(row, cell, type, turn):
        data = [row, cell, type, turn]
        data = json.dumps(data)
        client_socket.sendall(data).encode()
        print("sending")
        
        
    def check(player_map, enemy_map):
        if all(cell != 1 for row in player_map for cell in row):
            # client_socket.sendall("WIN")
            return "WIN"
        
        elif all(cell != 1 for row in enemy_map for cell in row):
            # client_socket.sendall("LOSE")
            return "LOSE"

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
               
    def map(list, row, cell, number, type):
        if type == "trio center": 
            if row != 0: 
                miss_list.append(pygame.Rect(list[number- 10].x, list[number- 10].y, 60, 60)) 
                list[number- 10].CLOSE = True 
                miss_list.append(pygame.Rect(list[number- 11].x, list[number- 11].y, 60, 60)) 
                list[number- 11].CLOSE = True 
                miss_list.append(pygame.Rect(list[number- 9].x, list[number- 9].y, 60, 60)) 
                list[number- 9].CLOSE = True 
            if row != 9: 
                miss_list.append(pygame.Rect(list[number+ 10].x, list[number+ 10].y, 60, 60)) 
                list[number+ 10].CLOSE = True 
                miss_list.append(pygame.Rect(list[number+ 11].x, list[number+ 11].y, 60, 60)) 
                list[number+ 11].CLOSE = True 
                miss_list.append(pygame.Rect(list[number+ 9].x, list[number+ 9].y, 60, 60)) 
                list[number+ 9].CLOSE = True 
            if cell !=0 and cell != 1 : 
                miss_list.append(pygame.Rect(list[number- 2].x, list[number- 2].y, 60, 60)) 
                list[number- 2].CLOSE = True 
            if  cell != 8 and cell != 9: 
                miss_list.append(pygame.Rect(list[number+ 2].x, list[number+ 2].y, 60, 60)) 
                list[number+ 2].CLOSE = True 
            if cell !=0 and cell != 1 and  row != 0: 
                miss_list.append(pygame.Rect(list[number- 12].x, list[number- 12].y, 60, 60)) 
                list[number- 12].CLOSE = True 
            if  cell != 8 and cell != 9 and row != 0: 
                miss_list.append(pygame.Rect(list[number- 8].x, list[number- 8].y, 60, 60)) 
                list[number- 8].CLOSE = True 
            if cell !=0 and cell != 1 and row != 9: 
                miss_list.append(pygame.Rect(list[number+8].x, list[number+8].y, 60, 60)) 
                list[number+ 8].CLOSE = True 
            if  cell != 8 and cell != 9 and row != 9: 
                miss_list.append(pygame.Rect(list[number+12].x, list[number+12].y, 60, 60)) 
                list[number+ 12].CLOSE = True
        
        elif type == "duo top":
            if row != 8:
                miss_list.append(pygame.Rect(list[number+ 20].x, list[number+ 20].y, 60, 60))
                list[number+ 20].CLOSE = True 
                print("BUTTON")
            if row != 0:
                miss_list.append(pygame.Rect(list[number- 10].x, list[number- 10].y, 60, 60))
                list[number- 10].CLOSE = True
                print("TOP")
            if cell != 0:
                miss_list.append(pygame.Rect(list[number- 1].x, list[number- 1].y, 60, 60))
                list[number- 1].CLOSE = True
                miss_list.append(pygame.Rect(list[number+9].x, list[number+ 9].y, 60, 60))
                list[number+ 9].CLOSE = True
                print("LEFT")
            if cell != 9:
                miss_list.append(pygame.Rect(list[number+ 1].x, list[number+ 1].y, 60, 60)) 
                list[number+ 1].CLOSE = True 
                miss_list.append(pygame.Rect(list[number+ 11].x, list[number+ 11].y, 60, 60))
                list[number+ 11].CLOSE = True
                print("RIGHT")
            if cell != 0 and row != 0:
                miss_list.append(pygame.Rect(list[number- 11].x, list[number- 11].y, 60, 60))
                list[number- 11].CLOSE = True 
                print("LEFT TOP")
            if cell != 9 and row != 0 :
                miss_list.append(pygame.Rect(list[number- 9].x, list[number- 9].y, 60, 60))
                list[number- 9].CLOSE = True 
                print("RIGHT TOP")
            if cell != 0 and row != 8:
                miss_list.append(pygame.Rect(list[number+ 19].x, list[number+ 19].y, 60, 60))
                list[number+ 19].CLOSE = True
                print("LEFT BUTTON")
            if cell != 9 and row !=8:
                miss_list.append(pygame.Rect(list[number+ 21].x, list[number+ 21].y, 60, 60))
                list[number+ 21].CLOSE = True
                print("RIGHR BUTTON")
            
        elif type == "duo button":
            if row != 9:
                miss_list.append(pygame.Rect(list[number+ 10].x, list[number+ 10].y, 60, 60))
                list[number+ 10].CLOSE = True 
                print("BUTTON")
            if row != 0 and row != 1:
                miss_list.append(pygame.Rect(list[number- 20].x, list[number- 20].y, 60, 60))
                list[number- 20].CLOSE = True
                print("TOP")
            if cell != 0:
                miss_list.append(pygame.Rect(list[number- 1].x, list[number- 1].y, 60, 60))
                list[number- 1].CLOSE = True
                miss_list.append(pygame.Rect(list[number- 11].x, list[number- 11].y, 60, 60))
                list[number- 11].CLOSE = True
                print("LEFT")
            if cell != 9:
                miss_list.append(pygame.Rect(list[number+ 1].x, list[number+ 1].y, 60, 60)) 
                list[number+ 1].CLOSE = True 
                miss_list.append(pygame.Rect(list[number- 9].x, list[number- 9].y, 60, 60))
                list[number- 9].CLOSE = True
                print("RIGHT")
            if cell != 0 and row != 0 and row != 1:
                miss_list.append(pygame.Rect(list[number- 21].x, list[number- 21].y, 60, 60))
                list[number- 21].CLOSE = True 
                print("LEFT TOP")
            if cell != 9 and row != 0 and row != 1:
                miss_list.append(pygame.Rect(list[number- 19].x, list[number- 19].y, 60, 60))
                list[number- 19].CLOSE = True 
                print("RIGHT TOP")
            if cell != 0 and row != 9:
                miss_list.append(pygame.Rect(list[number+ 9].x, list[number+ 9].y, 60, 60))
                list[number+ 9].CLOSE = True
                print("LEFT BUTTON")
            if cell != 9 and row !=9:
                miss_list.append(pygame.Rect(list[number+ 11].x, list[number+ 11].y, 60, 60))
                list[number+ 11].CLOSE = True
                print("RIGHR BUTTON")
        
        elif type == "duo right":
            if row != 0:
                miss_list.append(pygame.Rect(list[number- 11].x, list[number- 11].y, 60, 60))
                list[number- 11].CLOSE = True
                miss_list.append(pygame.Rect(list[number- 10].x, list[number- 10].y, 60, 60))
                list[number- 10].CLOSE = True 
            if row != 9:  
                miss_list.append(pygame.Rect(list[number+ 10].x, list[number+ 10].y, 60, 60))
                list[number+ 10].CLOSE = True 
                miss_list.append(pygame.Rect(list[number+ 9].x, list[number+ 9].y, 60, 60))
                list[number+ 9].CLOSE = True 
            if cell != 0 and cell != 1:   
                miss_list.append(pygame.Rect(list[number- 2].x, list[number- 2].y, 60, 60))
                list[number- 2].CLOSE = True
            if cell != 8 and cell != 9:
                miss_list.append(pygame.Rect(list[number+ 1].x, list[number+ 1].y, 60, 60)) 
                list[number+ 1].CLOSE = True
            if cell != 0 and cell != 1 and row != 0:
                miss_list.append(pygame.Rect(list[number- 12].x, list[number- 12].y, 60, 60))
                list[number- 12].CLOSE = True 
                print("LEFT TOP")
            if cell != 8 and cell != 9 and row != 0:
                miss_list.append(pygame.Rect(list[number- 9].x, list[number- 9].y, 60, 60))
                list[number- 9].CLOSE = True 
                print("RIGHT TOP")
            if  cell != 1 and cell != 0 and row != 9:
                miss_list.append(pygame.Rect(list[number+ 8].x, list[number+ 8].y, 60, 60))
                list[number+ 8].CLOSE = True
                print("LEFT BUTTON")
            if cell != 8 and cell != 9 and row !=9:
                miss_list.append(pygame.Rect(list[number+ 11].x, list[number+ 11].y, 60, 60))
                list[number+ 11].CLOSE = True
                print("RIGHR BUTTON")
        
        elif type == "duo left":
            if row != 0:
                miss_list.append(pygame.Rect(list[number- 10].x, list[number- 10].y, 60, 60))
                list[number- 10].CLOSE = True
                miss_list.append(pygame.Rect(list[number- 9].x, list[number- 9].y, 60, 60))
                list[number- 9].CLOSE = True 
                print("TOP")
            if row != 9:  
                miss_list.append(pygame.Rect(list[number+ 10].x, list[number+ 10].y, 60, 60))
                list[number+ 10].CLOSE = True 
                miss_list.append(pygame.Rect(list[number+ 11].x, list[number+ 11].y, 60, 60))
                list[number+ 11].CLOSE = True 
                print("BUTTON")
            if cell != 0:   
                miss_list.append(pygame.Rect(list[number- 1].x, list[number- 1].y, 60, 60))
                list[number- 1].CLOSE = True
                print("LEFT")
            if cell != 8 and cell != 9:
                miss_list.append(pygame.Rect(list[number+ 2].x, list[number+ 2].y, 60, 60)) 
                list[number+ 2].CLOSE = True
                print("RIGHT")
            if cell != 0 and row != 0:
                miss_list.append(pygame.Rect(list[number- 11].x, list[number- 11].y, 60, 60))
                list[number- 11].CLOSE = True 
                print("LEFT TOP")
            if cell != 8 and cell != 9 and row != 0:
                miss_list.append(pygame.Rect(list[number- 8].x, list[number- 8].y, 60, 60))
                list[number- 8].CLOSE = True 
                print("RIGHT TOP")
            if cell != 8 and cell != 0 and row != 9:
                miss_list.append(pygame.Rect(list[number+ 9].x, list[number+ 9].y, 60, 60))
                list[number+ 9].CLOSE = True
                print("LEFT BUTTON")
            if cell != 8 and cell != 9 and row !=9:
                miss_list.append(pygame.Rect(list[number+ 12].x, list[number+ 12].y, 60, 60))
                list[number+ 12].CLOSE = True
                print("RIGHR BUTTON")
            
        elif type == "solo":
            if row != 9 and player_map2[row+1][cell] == 0:
                miss_list.append(pygame.Rect(list[number+ 10].x, list[number+ 10].y, 60, 60))
                list[number+ 10].CLOSE = True 
                print("BUTTON")
            if row != 0 and player_map2[row-1][cell] == 0:
                miss_list.append(pygame.Rect(list[number- 10].x, list[number- 10].y, 60, 60))
                list[number- 10].CLOSE = True
                print("TOP")
            if cell != 0 and player_map2[row][cell-1] == 0:
                miss_list.append(pygame.Rect(list[number- 1].x, list[number- 1].y, 60, 60))
                list[number- 1].CLOSE = True
                print("LEFT")
            if cell != 9 and player_map2[row][cell+1] == 0:
                miss_list.append(pygame.Rect(list[number+ 1].x, list[number+ 1].y, 60, 60)) 
                list[number+ 1].CLOSE = True 
                print("RIGHT")
            if cell != 0 and row != 0:
                miss_list.append(pygame.Rect(list[number- 11].x, list[number- 11].y, 60, 60))
                list[number- 11].CLOSE = True 
                print("LEFT TOP")
            if cell != 9 and row != 0 :
                miss_list.append(pygame.Rect(list[number- 9].x, list[number- 9].y, 60, 60))
                list[number- 9].CLOSE = True 
                print("RIGHT TOP")
            if cell != 0 and row != 9:
                miss_list.append(pygame.Rect(list[number+ 9].x, list[number+ 9].y, 60, 60))
                list[number+ 9].CLOSE = True
                print("LEFT BUTTON")
            if cell != 9 and row !=9:
                miss_list.append(pygame.Rect(list[number+ 11].x, list[number+ 11].y, 60, 60))
                list[number+ 11].CLOSE = True
                print("RIGHR BUTTON")

    connect_to()

    data = json.dumps(player_map1)  
    client_socket.sendall(data.encode())  # Отправляем данные в байтовом формате
    print("sending map")

    print(player_map2)
    data = client_socket.recv(400)
    
    try:
        player_map2 = json.loads(data.decode())
        print("recv map")
        print(player_map2)
    except Exception as e:
        print(f"Ошибка: {e}")

    print(turn)
    turn = bool(client_socket.recv(400).decode())
    print(turn)

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

    # def test():
    #     while True:
    #         if not turn:
    #             data = list(client_socket.recv(400).decode())
    #             if data:
    #                 print(data[0])
    #                 print(data [1])
    #                 print(data[2])
    #                 print(data [3])

    # test_thread = Thread(target = test) 
    # test_thread.start()

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
                        hit_list.append(pygame.Rect(item.x, item.y ,60, 60))   
                        print(f"Изменение player_map2[{row}][{cell}] до: {player_map2[row][cell]}")
                        player_map2[row][cell] = 2
                        print(f"Изменение player_map2[{row}][{cell}] после: {player_map2[row][cell]}")                    
                        item.CLOSE = True
                        type = finder(row, cell)
                        map(row_list_enemy, row, cell, number, type)
                        res = check(player_map2, player_map1)
                        
                        if res:
                            print("test")
                            if res == "WIN":
                                
                                
                                data['main']['GOLD'] += 100
                                # write_json["main"]["GOLD"] += 100
                                write_json(fd='settings.json', name_dict = data)
                                return win()
                            else:
                                return lose()
                            
                        sending(row, cell, 1, 0)
                  
                    elif item.collidepoint(position) and sq_list[1].collidepoint(position) and player_map2[row][cell] == 0 and not item.CLOSE and turn:
                        miss_list.append(pygame.Rect(item.x, item.y, 60, 60))
                        # turn = False
                        item.CLOSE = True   
                        print("Поле врага: Не попал", row , cell , player_map2[row][cell])  

                        sending(row, cell, 0, 1)  
                        turn = False 

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
    run_win = True
    while run_win:
        screen.fill((MAIN_WINDOW_COLOR))
        
        position = pygame.mouse.get_pos()
        press = pygame.mouse.get_pressed()
        
        text_win.text_draw(screen=screen)
        
        button_back_menu.button_draw(screen=screen)
        back_to_menu = button_back_menu.checkPress(position = position, press = press)

        if back_to_menu:
            return "BACK"
        
        pygame.display.flip()
        clock.tick(FPS) 
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_win = False
                pygame.quit()

def lose():
    run_lose =True
    while run_lose:
        screen.fill((MAIN_WINDOW_COLOR))
        
        position = pygame.mouse.get_pos()
        press = pygame.mouse.get_pressed()
        
        text_lose.text_draw(screen=screen)
        
        button_back_menu.button_draw(screen=screen)
        back_to_menu = button_back_menu.checkPress(position = position, press = press)
    
        if back_to_menu:
            return "BACK"
        
        pygame.display.flip()
        clock.tick(FPS) 
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_lose = False
                pygame.quit()
