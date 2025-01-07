import socket
import pygame 
import os
import json

from threading import Thread

from .basement import *
from .map import *

data_settings = read_json(fd="settings.json")

PLACE_LENGTH = data_settings["color"]["PLACE_LENGTH"]
FPS = data_settings["main"]["FPS"]

def battle():

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
    
    global turn
    global run_battle

    turn = False
    stop_thread = True
    run_battle = True

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
        client_socket.connect(("192.168.1.12", 8081))
        print("connect")
    
    def sending(row, cell, number, shot_type, turn, kill_type):
        data = [row, cell, number, shot_type, turn, kill_type]
        print(data)
        data = json.dumps(data)
        client_socket.sendall(data.encode())

        print("sending")

    def check_lose():
        if all(cell != 1 for row in player_map1 for cell in row):
            data_settings["main"]["GOLD"] += 25
            write_json(fd='settings.json', name_dict = data_settings)
            return "LOSE"
             
    def check_win():
        if all(cell != 1 for row in player_map2 for cell in row):
            data_settings["main"]["GOLD"] += 100
            write_json(fd='settings.json', name_dict = data_settings)
            return "WIN"
        
    def add_miss(list, number, place, operation):
        if operation == "minus" and not list[number - place].CLOSE:
            miss_list.append(pygame.Rect(list[number - place].x, list[number - place].y, 60, 60)) 
            list[number - place].CLOSE = True 

        elif operation == "plus" and not list[number + place].CLOSE:
            miss_list.append(pygame.Rect(list[number + place].x, list[number + place].y, 60, 60)) 
            list[number + place].CLOSE = True 

    def map(list, row, cell, number, shot_type):
        print(list[number].x, list[number].x)
        print(type(row), type(cell), type(number), type(shot_type))
        print(row, cell, number, shot_type) 

        if shot_type == 100:
            print("all good")

        if shot_type == 20:
            if row != 0:
                add_miss(list, number, 10, "minus")
                add_miss(list, number, 11, "minus")
                add_miss(list, number, 9, "minus")
            if row != 9:
                add_miss(list, number, 10, "plus")
                add_miss(list, number, 11, "plus")
                add_miss(list, number, 9, "plus")
            if cell != 0 and cell != 1:
                add_miss(list, number, 2, "minus")
            if cell != 8 and cell != 9:
                add_miss(list, number, 2, "plus")
            if cell != 0 and cell != 1 and row != 0:
                add_miss(list, number, 12, "minus")
            if cell != 8 and cell != 9 and row != 0:
                add_miss(list, number, 8, "minus")
            if cell != 0 and cell != 1 and row != 9:
                add_miss(list, number, 8, "plus")
            if cell != 8 and cell != 9 and row != 9:
                add_miss(list, number, 12, "plus")

        elif shot_type == 12:
            if row != 8:
                add_miss(list, number, 20, "plus")
            if row != 0:
                add_miss(list, number, 10, "minus")
            if cell != 0:
                add_miss(list, number, 1, "minus")
                add_miss(list, number, 9, "plus")
            if cell != 9:
                add_miss(list, number, 1, "plus")
                add_miss(list, number, 11, "plus")
            if cell != 0 and row != 0:
                add_miss(list, number, 11, "minus")
            if cell != 9 and row != 0:
                add_miss(list, number, 9, "minus")
            if cell != 0 and row != 8:
                add_miss(list, number, 19, "plus")
            if cell != 9 and row != 8:
                add_miss(list, number, 21, "plus")

        elif shot_type == 14:
            if row != 9:
                add_miss(list, number, 10, "plus")
            if row != 0 and row != 1:
                add_miss(list, number, 20, "minus")
            if cell != 0:
                add_miss(list, number, 1, "minus")
                add_miss(list, number, 11, "minus")
            if cell != 9:
                add_miss(list, number, 1, "plus")
                add_miss(list, number, 9, "minus")
            if cell != 0 and row != 0 and row != 1:
                add_miss(list, number, 21, "minus")
            if cell != 9 and row != 0 and row != 1:
                add_miss(list, number, 19, "minus")
            if cell != 0 and row != 9:
                add_miss(list, number, 9, "plus")
            if cell != 9 and row != 9:
                add_miss(list, number, 11, "plus")

        elif shot_type == 13:
            if row != 0:
                add_miss(list, number, 11, "minus")
                add_miss(list, number, 10, "minus")
            if row != 9:
                add_miss(list, number, 10, "plus")
                add_miss(list, number, 9, "plus")
            if cell != 0 and cell != 1:
                add_miss(list, number, 2, "minus")
            if cell != 9:
                add_miss(list, number, 1, "plus")
            if cell != 0 and cell != 1 and row != 0:
                add_miss(list, number, 12, "minus")
            if cell != 8 and cell != 9 and row != 0:
                add_miss(list, number, 9, "minus")
            if cell != 0 and row != 9:
                add_miss(list, number, 8, "plus")
            if cell != 9 and row != 9:
                add_miss(list, number, 11, "plus")

        elif shot_type == 11:
            if row != 0:
                add_miss(list, number, 10, "minus")
                add_miss(list, number, 9, "minus")
            if row != 9:
                add_miss(list, number, 10, "plus")
                add_miss(list, number, 11, "plus")
            if cell != 0:
                add_miss(list, number, 1, "minus")
            if cell != 8 and cell != 9:
                add_miss(list, number, 2, "plus")
            if cell != 0 and row != 0:
                add_miss(list, number, 11, "minus")
            if cell != 8 and cell != 9 and row != 0:
                add_miss(list, number, 8, "minus")
            if cell != 0 and row != 9:
                add_miss(list, number, 9, "plus")
            if cell != 8 and cell != 9 and row != 9:
                add_miss(list, number, 12, "plus")

        elif shot_type == 1:
            if row != 9 and player_map2[row+1][cell] == 0:
                add_miss(list, number, 10, "plus")
            if row != 0 and player_map2[row-1][cell] == 0:
                add_miss(list, number, 10, "minus")
            if cell != 0 and player_map2[row][cell-1] == 0:
                add_miss(list, number, 1, "minus")
            if cell != 9 and player_map2[row][cell+1] == 0:
                add_miss(list, number, 1, "plus")
            if cell != 0 and row != 0:
                add_miss(list, number, 11, "minus")
            if cell != 9 and row != 0:
                add_miss(list, number, 9, "minus")
            if cell != 0 and row != 9:
                add_miss(list, number, 9, "plus")
            if cell != 9 and row != 9:
                add_miss(list, number, 11, "plus")

    def finder(row, cell):
        #########################
        # 100 nothing
        # 1 solo
        # 1-1 11 duo left
        # 1-2 12 duo top
        # 1-3 13 duo right
        # 1-4 14 duo down
        # 2-0 20 trio center
 
        if row != 0 and row != 9 and cell != 0 and cell != 9 and player_map2[row][cell] == 2 and player_map2[row][cell+1] == 0 and player_map2[row][cell-1] == 0 and player_map2[row+1][cell] == 0 and player_map2[row-1][cell] == 0:
            type = 1
            return type

        elif row == 0 and cell != 0 and cell != 9 and player_map2[row][cell] == 2 and player_map2[row][cell+1] == 0 and player_map2[row][cell-1] == 0 and player_map2[row+1][cell] == 0:
            type = 1
            return type

        elif row == 9 and cell != 0 and cell != 9 and player_map2[row][cell] == 2 and player_map2[row][cell+1] == 0 and player_map2[row][cell-1] == 0 and player_map2[row-1][cell] == 0:
            type = 1
            return type
        
        elif cell == 0 and row != 0 and row != 9 and player_map2[row][cell] == 2 and player_map2[row][cell+1] == 0 and player_map2[row+1][cell] == 0 and player_map2[row-1][cell] == 0:
            type = 1
            return type

        elif cell == 9 and row != 0 and row != 9 and player_map2[row][cell] == 2 and player_map2[row][cell-1] == 0 and player_map2[row+1][cell] == 0 and player_map2[row-1][cell] == 0:
            type = 1
            return type
        
        elif cell == 0 and row == 0 and player_map2[row][cell] == 2 and player_map2[row][cell+1] == 0 and player_map2[row+1][cell] == 0:
            type = 1
            return type

        elif cell == 0 and row == 9 and player_map2[row][cell] == 2 and player_map2[row][cell+1] == 0 and player_map2[row-1][cell] == 0:
            type = 1
            return type

        elif cell == 9 and row == 0 and player_map2[row][cell] == 2 and player_map2[row][cell-1] == 0 and player_map2[row+1][cell] == 0:
            type = 1
            return type

        elif cell == 9 and row == 9 and player_map2[row][cell] == 2 and player_map2[row][cell-1] == 0 and player_map2[row-1][cell] == 0:
            type = 1
            return type
     
        #########################

        elif row != 0 and row != 9 and cell != 0 and cell != 9 and cell != 8 and player_map2[row][cell] == 2 and player_map2[row][cell+1] == 2 and player_map2[row][cell+2] == 0 and player_map2[row][cell-1] == 0 and player_map2[row+1][cell] == 0 and player_map2[row-1][cell] == 0:
            type = 11
            return type

        elif row == 0 and cell != 0 and cell != 1 and cell != 9 and cell != 8 and player_map2[row][cell] == 2 and player_map2[row][cell+1] == 2 and player_map2[row][cell-1] == 0 and player_map2[row][cell+2] == 0 and player_map2[row+1][cell] == 0:
            type = 11
            return type

        elif row == 9 and cell != 0 and cell != 9 and cell != 8 and player_map2[row][cell] == 2 and player_map2[row][cell+1] == 2 and player_map2[row][cell+2] == 0 and player_map2[row][cell-1] == 0 and player_map2[row-1][cell] == 0:
            type = 11
            return type

        elif row != 0 and row != 9 and cell == 0 and player_map2[row][cell] == 2 and player_map2[row][cell+1] == 2 and player_map2[row][cell+2] == 0 and player_map2[row+1][cell] == 0 and player_map2[row-1][cell] == 0:
            type = 1-1
            return type

        elif row != 9 and row != 0 and cell == 8 and player_map2[row][cell] == 2 and player_map2[row][cell+1] == 2 and player_map2[row][cell-1] == 0 and player_map2[row-1][cell] == 0 and player_map2[row+1][cell] == 0:
            type = 11
            return type
      
        elif row == 0 and cell == 0  and player_map2[row][cell-1] == 0 and player_map2[row][cell] == 2 and player_map2[row+1][cell] == 0 and player_map2[row][cell+2] == 0 and player_map2[row][cell+1] == 2:
            type = 11
            return type

        elif row == 0 and player_map2[row][cell] == 2 and player_map2[row+1][cell] == 0 and player_map2[row][cell-1] == 2 and player_map2[row][cell+1] == 2 and player_map2[row][cell-2] == 0:
            type = 11
            return type

        elif row == 9 and cell == 0 and player_map2[row][cell] == 2 and player_map2[row][cell+1] == 2 and player_map2[row-1][cell] == 0 and player_map2[row][cell+2] == 0:
            type = 11
            return type

        elif row == 9 and cell == 8 and player_map2[row][cell] == 2 and player_map2[row][cell+1] == 2 and player_map2[row-1][cell] == 0 and player_map2[row][cell-1] == 2 and player_map2[row][cell-2] == 0:
            type = 11
            return type

        ######################### 
        
        elif row != 0 and row != 9 and cell != 1 and cell != 9 and player_map2[row][cell] == 2 and player_map2[row][cell-1] == 2 and player_map2[row][cell-2] == 0 and player_map2[row][cell+1] == 0 and player_map2[row+1][cell] == 0 and player_map2[row-1][cell] == 0:
            type = 13
            return type

        elif row == 0 and cell != 1 and cell != 2 and cell != 9 and player_map2[row][cell] == 2 and player_map2[row][cell-1] == 2 and player_map2[row][cell-2] == 0 and player_map2[row][cell+1] == 0 and player_map2[row+1][cell] == 0:
            type = 13
            return type

        elif row == 9 and cell != 1 and cell != 2 and cell != 9 and cell != 8 and player_map2[row][cell] == 2 and player_map2[row][cell-1] == 2 and player_map2[row][cell-2] == 0 and player_map2[row][cell+1] == 0 and player_map2[row-1][cell] == 0:
            type = 13
            return type

        elif row != 0 and row != 9 and cell == 1 and player_map2[row][cell] == 2 and player_map2[row][cell-1] == 2 and  player_map2[row][cell+1] == 0 and player_map2[row+1][cell] == 0 and player_map2[row-1][cell] == 0:
            type = 13
            return type

        elif row != 9 and row != 0 and cell == 9 and player_map2[row][cell] == 2 and player_map2[row][cell-1] == 2 and player_map2[row][cell-2] == 0 and player_map2[row-1][cell] == 0 and player_map2[row+1][cell] == 0:
            type = 13
            return type
      
        elif row == 0 and cell == 1 and player_map2[row][cell] == 2 and player_map2[row][cell-1] == 2 and player_map2[row+1][cell] == 0 and player_map2[row][cell+1] == 0:
            type = 13
            return type

        elif row == 0 and cell == 9 and player_map2[row][cell] == 2 and player_map2[row][cell-1] == 2 and player_map2[row+1][cell] == 0 and player_map2[row][cell-2] == 0:
            type = 13
            return type

        elif row == 9 and cell == 1 and player_map2[row][cell] == 2 and player_map2[row][cell-1] == 2 and player_map2[row-1][cell] == 0 and player_map2[row][cell+1] == 0:
            type = 13
            return type

        elif row == 9 and cell == 9 and player_map2[row][cell] == 2 and player_map2[row][cell-1] == 2 and player_map2[row-1][cell] == 0 and player_map2[row][cell-2] == 0:
            type = 13
            return type

        
        ###########################

        elif cell != 0 and cell != 9 and row !=0 and row !=8 and row != 9 and player_map2[row][cell] == 2 and player_map2[row+1][cell] == 2 and player_map2[row+2][cell] == 0 and player_map2[row-1][cell] == 0 and player_map2[row][cell+1] == 0 and player_map2[row][cell-1] == 0:
            type = 12
            return type

        elif cell != 0 and cell !=9 and row == 0 and player_map2[row][cell] == 2 and player_map2[row+1][cell] == 2 and player_map2[row+2][cell] == 0 and player_map2[row][cell-1] == 0 and player_map2[row][cell-1] == 0:
            type = 12
            return type

        elif cell != 0 and cell !=9 and row == 8 and player_map2[row][cell] == 2 and player_map2[row+1][cell] == 2 and  player_map2[row-1][cell] == 0 and player_map2[row][cell-1] == 0 and player_map2[row][cell+1] == 0:
            type = 12
            return type

        elif cell == 0 and row != 0 and row != 8 and row != 9 and player_map2[row][cell] == 2 and player_map2[row+1][cell] == 2 and player_map2[row+2][cell] == 0 and player_map2[row-1][cell] == 0 and player_map2[row][cell+1] == 0:
            type = 12
            return type
            
        elif cell == 9 and row != 0 and row != 8 and row != 9 and player_map2[row][cell] == 2 and player_map2[row+1][cell] == 2 and player_map2[row+2][cell] == 0 and player_map2[row-1][cell] == 0 and player_map2[row][cell-1] == 0:
            type = 12
            return type

        elif cell == 0 and row == 0 and player_map2[row][cell] == 2 and player_map2[row+1][cell] == 2 and player_map2[row+2][cell] == 0 and player_map2[row][cell+1] == 0:
            type = 12
            return type

        elif cell == 9 and row == 0 and player_map2[row][cell] == 2 and player_map2[row+1][cell] == 2 and player_map2[row+2][cell] == 0 and player_map2[row][cell-1] == 0:
            type = 12
            return type

        elif cell == 0 and row == 8 and player_map2[row][cell] == 2 and player_map2[row+1][cell] == 2 and player_map2[row-1][cell] == 0 and player_map2[row][cell+1] == 0:
            type = 12
            return type

        elif cell == 9 and row == 8 and player_map2[row][cell] == 2 and player_map2[row+1][cell] == 2 and player_map2[row-1][cell] == 0 and player_map2[row-1][cell] == 0:
            type = 12
            return type
        
        #########################   
        
        elif cell != 0 and cell != 9 and row !=0 and row !=1 and row != 9 and player_map2[row][cell] == 2 and player_map2[row-1][cell] == 2 and player_map2[row-2][cell] == 0 and player_map2[row+1][cell] == 0 and player_map2[row][cell+1] == 0 and player_map2[row][cell-1] == 0:
            type = 14
            return type

        elif cell != 0 and cell !=9 and row == 1 and player_map2[row][cell] == 2 and player_map2[row-1][cell] == 2  and player_map2[row+1][cell] == 0  and player_map2[row][cell+1] == 0 and player_map2[row][cell-1] == 0:
            type = 14
            return type

        elif  cell != 0 and cell !=9 and row == 9 and player_map2[row][cell] == 2 and player_map2[row-1][cell] == 2 and player_map2[row-2][cell] == 0  and player_map2[row][cell+1] == 0 and player_map2[row][cell-1] == 0:
            type = 14
            return type

        elif row != 1 and row != 9 and row != 0 and row != 8 and cell == 0 and player_map2[row][cell] == 2 and player_map2[row-1][cell] == 2 and player_map2[row-2][cell] == 0 and player_map2[row+1][cell] == 0 and player_map2[row][cell+1] == 0:
            type = 14
            return type

        elif row != 1 and row != 9 and row != 0 and row != 8 and cell == 9 and player_map2[row][cell] == 2 and player_map2[row-1][cell] == 2 and player_map2[row-2][cell] == 0 and player_map2[row][cell-1] == 0 and player_map2[row+1][cell] == 0:
            type = 14
            return type

        elif row == 1 and cell == 0 and player_map2[row][cell] == 2 and player_map2[row-1][cell] == 2 and player_map2[row+1][cell] == 0 and player_map2[row][cell+1] == 0:
            type = 14
            return type

        elif row == 1 and cell == 9 and player_map2[row][cell] == 2 and player_map2[row-1][cell] == 2 and player_map2[row+1][cell] == 0 and player_map2[row][cell-1] == 0:
            type = 14
            return type

        elif row == 9 and cell == 0 and player_map2[row][cell] == 2 and player_map2[row-1][cell] == 2 and player_map2[row-2][cell] == 0 and player_map2[row][cell+1] == 0:
            type = 14
            return type

        elif row == 9 and cell == 9 and player_map2[row][cell] == 2 and player_map2[row-1][cell] == 2 and player_map2[row-2][cell] == 0 and player_map2[row][cell-1] == 0:
            type = 14
            return type
        
        #########################

        elif row != 0 and row != 9 and cell !=0 and cell != 9 and cell != 1 and cell !=  8 and cell != 2 and cell !=  7 and player_map2[row][cell] == 2 and player_map2[row][cell-1] == 2 and player_map2[row][cell+1] == 2 and player_map2[row][cell-2] == 0 and player_map2[row][cell+2] == 0 and player_map2[row+1][cell] == 0 and player_map2[row-1][cell] == 0: 
            type = 20 
            return type 
     
        elif cell != 8 and cell != 9 and player_map2[row][cell] == 2 and player_map2[row][cell-1] == 2 and player_map2[row][cell+1] == 2 and player_map2[row][cell-2] == 0:  
            type = 20 
            return type

        elif cell != 0 and cell != 1 and cell != 8 and cell != 9 and player_map2[row][cell] == 2 and player_map2[row][cell-1] == 2 and player_map2[row][cell+1] == 2 and player_map2[row][cell+2] == 0:  
            type = 20 
            return type

        elif row == 0 and cell != 0 and cell != 1 and cell != 8 and cell != 9 and player_map2[row][cell] == 2 and player_map2[row][cell-1] == 2 and player_map2[row][cell+1] == 2 and player_map2[row][cell+2] == 0 and player_map2[row][cell+1] == 2 and player_map2[row][cell-2] == 0 and player_map2[row +1][cell] == 0:  
            type = 20 
            return type

        elif row != 9 and cell != 0 and cell != 1 and cell != 8 and cell != 9 and player_map2[row][cell] == 2 and player_map2[row][cell-1] == 2 and player_map2[row][cell+1] == 2 and player_map2[row][cell+2] == 0 and player_map2[row][cell+1] == 2 and player_map2[row][cell-2] == 0 and player_map2[row -1][cell] == 0:  
            type = 20 
            return type

        elif row == 0 and cell == 2 and player_map2[row][cell] == 2 and player_map2[row][cell-1] == 2 and player_map2[row][cell+1] == 2 and player_map2[row][cell+2] == 0 and player_map2[row+1][cell] == 0:
            type = 20 
            return type

        elif row == 0 and cell == 8 and player_map2[row][cell] == 2 and player_map2[row][cell-1] == 2 and player_map2[row][cell+1] == 2 and player_map2[row][cell-2] == 0 and player_map2[row+1][cell] == 0:
            type = 20 
            return type

        elif row == 9 and cell == 2 and player_map2[row][cell] == 2 and player_map2[row][cell-1] == 2 and player_map2[row][cell+1] == 2 and player_map2[row][cell+2] == 0 and player_map2[row-1][cell] == 0:
            type = 20 
            return type

        elif row == 9 and cell == 8 and player_map2[row][cell] == 2 and player_map2[row][cell-1] == 2 and player_map2[row][cell+1] == 2 and player_map2[row][cell-2] == 0 and player_map2[row-1][cell] == 0:
            type = 20 
            return type

        else:
            type = 100
            return type

    connect_to()

    data = json.dumps(player_map1)  
    client_socket.sendall(data.encode())  # Отправляем данные в байтовом формате
    print("sending map")

    data = client_socket.recv(400)
    player_map2 = json.loads(data.decode())
    print("recv map")
    print(player_map2)

    turn = client_socket.recv(10).decode()
    
    if turn == "you":
        turn = True
    elif turn == "not":
        turn = False

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

    def always_recv():
        global turn
        global run_battle
        
        while stop_thread:
            data = client_socket.recv(35).decode()
            if data:
                data = data.strip("[]")
                data = [int(num) for num in data.split(",")]

                c_row = int(data[0])
                c_cell = int(data[1])
                c_number = int(data[2])
                c_type = int(data[3])
                turn = int(data[4])
                kill_type = int(data[5])
                 
                empty= 0
                for item in row_list_player:
                    if empty == c_number:
                        if c_type == 1:                    
                            hit_list.append(pygame.Rect(item.x, item.y ,60, 60)) 
                            print(f"Изменение player_map2[{row}][{cell}] до: {player_map2[row][cell]}")
                            player_map1[c_row][c_cell] = 2
                            print(f"Изменение player_map2[{row}][{cell}] после: {player_map2[row][cell]}") 

                            map(row_list_player, c_row, c_cell, c_number, kill_type)  

                            res = check_lose()
                            print(res)
                            print("hit")
                            if res == "LOSE":
                                turn = False
                                run_battle = False
                                lose()
                        
                        elif c_type == 0:
                            miss_list.append(pygame.Rect(item.x, item.y ,60, 60))  
                            print("miss")
                    
                    empty+= 1

    test_thread = Thread(target = always_recv) 
    test_thread.start()

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

        # print(clock.get_fps())
        
        pygame.display.flip()
        clock.tick(FPS)      
        
        for event in pygame.event.get():
            
            if event.type == pygame.MOUSEBUTTONUP and press[1]:
                number = 0
                for item in row_list_enemy:
                    row = number // 10
                    cell = number % 10
                    if item.collidepoint(position):
                        print(turn)
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
                        
                        shot_type = finder(row, cell)
                        map(row_list_enemy, row, cell, number, shot_type)

                        sending(row, cell, number, 1, 0, kill_type= shot_type)

                        res = check_win()
                        print(res)
                        if res == "WIN":
                            turn = False
                            run_battle = False
                            win()
            
                    elif item.collidepoint(position) and sq_list[1].collidepoint(position) and player_map2[row][cell] == 0 and not item.CLOSE and turn:
                        miss_list.append(pygame.Rect(item.x, item.y, 60, 60))
                        print("Поле врага: Не попал", row , cell , player_map2[row][cell])
                        item.CLOSE = True  
                        turn = False   

                        sending(row, cell, number, 0, 1, kill_type = 100)  

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
