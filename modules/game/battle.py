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
    global stop_thread

    turn = False
    stop_thread = True
    run_battle = True

    clean_right_side = False
    clean_left_side = False
    clean_down_side = False
    clean_top_side = False
    clean_side_list = [clean_right_side, clean_left_side, clean_down_side, clean_top_side]

    ship_right_side = False
    ship_left_side = False
    ship_down_side = False
    ship_top_side = False
    ship_side_list = [ship_right_side, ship_left_side, ship_down_side, ship_top_side]

    dead_ship_right_side = False
    dead_ship_left_side = False
    dead_ship_down_side = False
    dead_ship_top_side = False
    dead_ship_side_list = [dead_ship_right_side, dead_ship_left_side, dead_ship_down_side, dead_ship_top_side]

    point = 0

    Text_point = Text(x= 1050, y= 50, text = str(point), color= "Black", text_size= 50)

    buy = None

    #Наше поле (your screen)
    sq_your = pygame.Rect((70, 180, PLACE_LENGTH, PLACE_LENGTH))
    #Поле противника (enemy screen)
    sq_enemy = pygame.Rect((730, 180, PLACE_LENGTH, PLACE_LENGTH))

    bg = pygame.image.load(os.path.abspath(__file__ + "/../../../image/bg/battle_field.png"))
    bg = pygame.transform.scale(bg, [PLACE_LENGTH, PLACE_LENGTH])

    clean_bg = pygame.image.load(os.path.abspath(__file__ + "/../../../image/bg/clean_bg.png")).convert_alpha()
    clean_bg = pygame.transform.scale(clean_bg, [PLACE_LENGTH, PLACE_LENGTH])

    frame= pygame.image.load(os.path.abspath(__file__ + "/../../../image/skills/sp_weapon_holder.png"))
    frame= pygame.transform.scale(frame, [85, 85])

    hit = pygame.image.load(os.path.abspath(__file__ + "/../../../image/cell/hit.png"))
    hit = pygame.transform.scale(hit, [60,60])
    
    miss = pygame.image.load(os.path.abspath(__file__ + "/../../../image/cell/miss.png"))
    miss = pygame.transform.scale(miss, [60, 60])

    lamp_active = pygame.image.load(os.path.abspath(__file__ + "/../../../image/skills/lamp_active.png")).convert_alpha()
    lamp_active = pygame.transform.scale(lamp_active, [60, 450])

    lamp_unactive = pygame.image.load(os.path.abspath(__file__ + "/../../../image/skills/lamp_unactive.png"))
    lamp_unactive = pygame.transform.scale(lamp_unactive, [60, 450])

    sq_list = [sq_your,  sq_enemy]

    miss_list =[]
    hit_list = []

    x1, y1 = 70, 180
    x2, y2 = 730, 180
    
    row_list_player = []
    cell_list_player = []

    row_list_enemy = []
    cell_list_enemy = []

    run = True

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect_to():
        client_socket.connect(("localhost", 8081))
        print("connect")
    
    def sending(row, cell, number, shot_type, turn, kill_type, skill = 0):
        data = [row, cell, number, shot_type, turn, kill_type, skill]
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

        print(row, cell, number, shot_type)
        
        if shot_type == 100:
            print("miss")  

        if shot_type == 21: 
            print("trio left goh")   
            if row != 0:
                add_miss(list, number, 10, "minus")
                add_miss(list, number, 8, "minus")
                add_miss(list, number, 9, "minus")
            if row != 9:
                add_miss(list, number, 10, "plus")
                add_miss(list, number, 11, "plus")
                add_miss(list, number, 12, "plus")
            if cell != 0:
                add_miss(list, number, 1, "minus")
            if cell != 7 and cell != 8 and cell != 9:
                add_miss(list, number, 3, "plus")
            if cell != 0 and row != 0:
                add_miss(list, number, 11, "minus")
            if cell != 7 and cell != 8 and cell != 9 and row != 0:
                add_miss(list, number, 7, "minus")
            if cell != 0 and row != 9:
                add_miss(list, number, 9, "plus")
            if cell != 7 and cell != 8 and cell != 9 and row != 9:
                add_miss(list, number, 13, "plus")
 
        elif shot_type == 22:
            print("trio right gor") 
            if row != 0:
                add_miss(list, number, 10, "minus")
                add_miss(list, number, 11, "minus")
                add_miss(list, number, 12, "minus")
            if row != 9:
                add_miss(list, number, 10, "plus")
                add_miss(list, number, 9, "plus")
                add_miss(list, number, 8, "plus")
            if cell != 1 and cell != 2 and cell != 0:
                add_miss(list, number, 3, "minus")
            if cell != 9:
                add_miss(list, number, 1, "plus")
            if cell != 1 and cell != 2 and cell != 0 and row != 0:
                add_miss(list, number, 13, "minus")
            if cell != 9 and row != 0:
                add_miss(list, number, 9, "minus")
            if cell != 1 and cell != 2 and cell != 0 and row != 9:
                add_miss(list, number, 7, "plus")
            if cell != 9 and row != 9:
                add_miss(list, number, 11, "plus")

        elif shot_type == 24:
            print("trio top ver") 
            if row != 9 and row != 8 and row != 7:
                add_miss(list, number, 30, "plus")
            if row != 0:
                add_miss(list, number, 10, "minus")
            if cell != 0:
                add_miss(list, number, 1, "minus")
                add_miss(list, number, 9, "plus")
                add_miss(list, number, 19, "plus")
            if cell != 9:
                add_miss(list, number, 1, "plus")
                add_miss(list, number, 11, "plus")
                add_miss(list, number, 21, "plus")
            if cell != 0 and row != 0:
                add_miss(list, number, 11, "minus")
            if cell != 9 and row != 0:
                add_miss(list, number, 9, "minus")
            if cell != 0 and row != 7 and row != 8 and row != 9:
                add_miss(list, number, 29, "plus")
            if cell != 9 and row != 7 and row != 8 and row != 9:
                add_miss(list, number, 31, "plus")

        # if shot_type == 25:
        #     print("trio down ver") 
        
        elif shot_type == 25:
            print("trio down ver")
            if row != 2:
                add_miss(list, number, 30, "minus")
            if row != 9:
                add_miss(list, number, 10, "plus")
            if cell != 0:
                add_miss(list, number, 1, "minus")
                add_miss(list, number, 21, "minus")
                add_miss(list, number, 11, "minus")
            if cell != 9:
                add_miss(list, number, 1, "plus")
                add_miss(list, number, 9, "minus")
                add_miss(list, number, 19, "minus")
            
            if cell != 0 and row != 9:
                add_miss(list, number, 9, "plus")
            if cell != 9 and row != 9:
                add_miss(list, number, 11, "plus")
            
            if cell != 0 and row != 2:
                add_miss(list, number, 31, "minus")

            if cell != 9 and row != 2:
                add_miss(list, number, 29, "minus")
            
            # if row < 7:
            #     add_miss(list, number, 30, "plus")
            # if row != 9:
            #     add_miss(list, number, 10, "plus")
            # if cell != 0:
            #     add_miss(list, number, 1, "minus")
            #     add_miss(list, number, 9, "plus")
            #     add_miss(list, number, 19, "plus")
            # if cell != 9:
            #     add_miss(list, number, 1, "plus")
            #     add_miss(list, number, 11, "plus")
            #     add_miss(list, number, 21, "plus")
            # if cell != 0 and row < 7:
            #     add_miss(list, number, 29, "plus")
            # if cell != 9 and row < 7:
            #     add_miss(list, number, 31, "plus")
  
        # if shot_type == 30:
        #     print("four 1center gor") 
        #     unuse

        elif shot_type == 30:
            print("four 1center gor")
            if row != 0:
                add_miss(list, number, 10, "minus")
                add_miss(list, number, 11, "minus")
                add_miss(list, number, 9, "minus")
                add_miss(list, number, 8, "minus")
            if row != 9:
                add_miss(list, number, 10, "plus")
                add_miss(list, number, 11, "plus")
                add_miss(list, number, 12, "plus")
                add_miss(list, number, 9, "plus")
            if cell != 1:
                add_miss(list, number, 2, "minus")
            if cell != 7:
                add_miss(list, number, 3, "plus")
            
            if cell != 1 and row != 0:
                add_miss(list, number, 12, "minus")
            if cell != 7 and row != 0:
                add_miss(list, number, 7, "minus")
            if cell != 1 and row != 9:
                add_miss(list, number, 8, "plus")
            if cell != 7 and row != 9:
                add_miss(list, number, 13, "plus")
        
        # if shot_type == 31:
        #     print("four 2center gor") 
        # #     unuse   

        elif shot_type == 31:
            print("four 2center gor")
            if row != 0:
                add_miss(list, number, 10, "minus")
                add_miss(list, number, 11, "minus")
                add_miss(list, number, 12, "minus")
                add_miss(list, number, 9, "minus")
            if row != 9:
                add_miss(list, number, 10, "plus")
                add_miss(list, number, 11, "plus")
                add_miss(list, number, 9, "plus")
                add_miss(list, number, 8, "plus")
            if cell != 2:
                add_miss(list, number, 3, "minus")
            if cell != 8:
                add_miss(list, number, 2, "plus")
            if cell != 2 and row != 0:
                add_miss(list, number, 13, "minus")
            if cell != 8 and row != 0:
                add_miss(list, number, 8, "minus")
            if cell != 2 and row != 9:
                add_miss(list, number, 7, "plus")
            if cell != 8 and row != 9:
                add_miss(list, number, 12, "plus")

        # if shot_type == 32:
        #     print("four left gor") 

        elif shot_type == 32:
            print("four left gor")
            if row != 0:
                add_miss(list, number, 10, "minus")
                add_miss(list, number, 9, "minus")
                add_miss(list, number, 8, "minus")
                add_miss(list, number, 7, "minus")
            if row != 9:
                add_miss(list, number, 10, "plus")
                add_miss(list, number, 11, "plus")
                add_miss(list, number, 12, "plus")
                add_miss(list, number, 13, "plus")
            if cell != 0:
                add_miss(list, number, 1, "minus")
            if cell != 6:
                add_miss(list, number, 4, "plus")
            
            if cell != 0 and row != 0:
                add_miss(list, number, 11, "minus")
            if cell != 6 and row != 0:
                add_miss(list, number, 6, "minus")
            if cell != 0 and row != 9:
                add_miss(list, number, 9, "plus")
            if cell != 6 and row != 9:
                add_miss(list, number, 14, "plus")

        # if shot_type == 33:
        #     print("four right gor") 

        elif shot_type == 33:
            print("four right gor")
            if row != 0:
                add_miss(list, number, 10, "minus")
                add_miss(list, number, 11, "minus")
                add_miss(list, number, 12, "minus")
                add_miss(list, number, 13, "minus")
            if row != 9:
                add_miss(list, number, 10, "plus")
                add_miss(list, number, 9, "plus")
                add_miss(list, number, 8, "plus")
                add_miss(list, number, 7, "plus")
            if cell != 9:
                add_miss(list, number, 1, "plus")
            if cell != 2:
                add_miss(list, number, 4, "minus")
            
            if cell != 9  and row != 0:
                add_miss(list, number, 9, "minus")
            if cell != 2 and row != 0:
                add_miss(list, number, 14, "minus")
            if cell != 9 and row != 9:
                add_miss(list, number, 11, "plus")
            if cell != 2 and row != 9:
                add_miss(list, number, 6, "plus")

        # if shot_type == 34:
        #     print("four 1center ver") 
        #     unuse

        elif shot_type == 34:
            print("four 1center ver")
            if row != 7:
                add_miss(list, number, 30, "plus")
            if row != 1:
                add_miss(list, number, 20, "minus")
            if cell != 0:
                add_miss(list, number, 1, "minus")
                add_miss(list, number, 11, "minus")
                add_miss(list, number, 9, "plus")
                add_miss(list, number, 19, "plus")
            if cell != 9:
                add_miss(list, number, 1, "plus")
                add_miss(list, number, 11, "plus")
                add_miss(list, number, 9, "minus")
                add_miss(list, number, 21, "plus")

            if cell != 0 and row != 7:
                add_miss(list, number, 29, "plus")

            if cell != 9 and row != 7:
                add_miss(list, number, 31, "plus")

            if cell != 0 and row != 1:
                add_miss(list, number, 21, "minus")

            if cell != 9 and row != 1:
                add_miss(list, number, 19, "minus")

        # if shot_type == 35:
        #     print("four 2center ver")
        #     unuse

        elif shot_type == 35:
            print("four 2center ver")
            if row != 8:
                add_miss(list, number, 20, "plus")
            if row != 2:
                add_miss(list, number, 30, "minus")
            if cell != 0:
                add_miss(list, number, 1, "minus")
                add_miss(list, number, 11, "minus")
                add_miss(list, number, 9, "plus")
                add_miss(list, number, 21, "minus")
            if cell != 9:
                add_miss(list, number, 1, "plus")
                add_miss(list, number, 11, "plus")
                add_miss(list, number, 9, "minus")
                add_miss(list, number, 19, "minus")

            if cell != 0 and row != 8:
                add_miss(list, number, 19, "plus")

            if cell != 9 and row != 8:
                add_miss(list, number, 21, "plus")

            if cell != 0 and row != 2:
                add_miss(list, number, 31, "minus")

            if cell != 9 and row != 2:
                add_miss(list, number, 29, "minus")

        # if shot_type == 36:
        #     print("four top ver") 

        elif shot_type == 36:
            print("four top ver")
            if row != 0:
                add_miss(list, number, 10, "minus")
            if row != 6:
                add_miss(list, number, 40, "plus")
            if cell != 0:
                add_miss(list, number, 1, "minus")
                add_miss(list, number, 9, "plus")
                add_miss(list, number, 19, "plus")
                add_miss(list, number, 29, "plus")
            if cell != 9:
                add_miss(list, number, 1, "plus")
                add_miss(list, number, 11, "plus")
                add_miss(list, number, 21, "plus")
                add_miss(list, number, 31, "plus")

            if cell != 0 and row != 0:
                add_miss(list, number, 11, "minus")

            if cell != 9 and row != 0:
                add_miss(list, number, 9, "minus")

            if cell != 0 and row != 6:
                add_miss(list, number, 39, "plus")

            if cell != 9 and row != 6:
                add_miss(list, number, 41, "plus")

        # if shot_type == 37:
        #     print("four down ver")

        elif shot_type == 37:
            print("four down ver")
            if row != 9:
                add_miss(list, number, 10, "plus")
            if row != 3:
                add_miss(list, number, 40, "minus")
            if cell != 0:
                add_miss(list, number, 1, "minus")
                add_miss(list, number, 11, "minus")
                add_miss(list, number, 21, "minus")
                add_miss(list, number, 31, "minus")
            if cell != 9:
                add_miss(list, number, 1, "plus")
                add_miss(list, number, 9, "minus")
                add_miss(list, number, 19, "minus")
                add_miss(list, number, 29, "minus")

            if row != 9 and cell != 0:
                add_miss(list, number, 9, "plus")

            if row != 9 and cell != 9:
                add_miss(list, number, 11, "plus")

            if row != 3 and cell != 0:
                add_miss(list, number, 41, "minus")
            
            if row != 3 and cell != 0:
                add_miss(list, number, 39, "minus")
                
        elif shot_type == 20:
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
           
        if shot_type == 23:
            print("trio center vert")
            if row != 1:
                add_miss(list, number, 20, "minus")           
            if row != 8:
                add_miss(list, number, 20, "plus")            
            if cell != 0:
                add_miss(list, number, 1, "minus")
                add_miss(list, number, 11, "minus")
                add_miss(list, number, 9, "plus")  
            if cell != 9:
                add_miss(list, number, 1, "plus")
                add_miss(list, number, 11, "plus")
                add_miss(list, number, 9, "minus")
            if cell != 0 and row != 1:
                add_miss(list, number, 21, "minus")
            if cell != 9 and row != 1:
                add_miss(list, number, 19, "minus")
            if cell != 0 and row != 8:
                add_miss(list, number, 19, "plus")
            if cell != 9 and row != 8:
                add_miss(list, number, 21, "plus")

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
            if cell != 9 and row != 0:
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
         
    def check_side(type, list, row, cell):
        ship_count = 2
        if type == 0 and cell + 2 <= 9:
            new_cell = cell + 2
            next_cell = new_cell +1
            print("RIGHT")
            while run:
                if new_cell <= 9 and list[row][new_cell] == 2:
                    print("RIGHT + 1")
                    ship_count += 1
                elif next_cell <= 9 and list[row][next_cell] == 1:
                    print("RIGHT NEXT SHIP OUT")
                    return
                elif new_cell <= 9 and list[row][new_cell] == 0:
                    print("RIGHT CLEAN")
                    return ship_count
                elif new_cell > 9:
                    print("RIGHT CLOSE")
                    return ship_count
                
                new_cell = new_cell + 1
                next_cell = next_cell + 1

        if type == 0 and cell + 2 > 9:
            return ship_count
        
        if type == 1 and cell - 2 >= 0:
            new_cell = cell - 2
            next_cell = new_cell - 1
            print("LEFT")
            while  run:
                if new_cell >= 0 and list[row][new_cell] == 2:
                    print("Left + 1")
                    ship_count += 1
                elif next_cell >= 0 and list[row][new_cell] == 1:
                    print("Left NEXT SHIP OUT")
                    return
                elif new_cell >= 0 and list[row][new_cell] == 0:
                    print("Left CLEAN")
                    return ship_count
                
                elif new_cell < 0:
                    print("Left CLEAN")
                    return ship_count
                
                new_cell = new_cell - 1
                next_cell = next_cell + 1

        if type == 1 and cell - 2 < 0:
            return ship_count
        
        if type == 2 and row + 2 <= 9:
            new_row = row + 2
            next_row = new_row + 1
            print("TOP")
            while run:
                if new_row <= 9 and list[new_row][cell] == 2:
                    print("Top + 1")
                    ship_count += 1
                elif next_row <= 9 and list[next_row][cell] == 1:
                    print("Top NEXT SHIP OUT")
                    return
                elif new_row <= 9 and list[new_row][cell] == 0:
                    print("Top CLEAN")
                    return ship_count
                elif new_row > 9:
                    print("Top CLOSE")
                    return ship_count
    
                new_row = new_row + 1
                next_row = next_row + 1
        
        if type == 2 and row + 2 > 9:
            return ship_count
        
        if type == 3 and row - 2 >= 0:
            new_row = row - 2
            next_row = new_row - 1
            print("DOWN")
            while run:
                if new_row >= 0 and list[new_row][cell] == 2:
                    print("DOWN + 1")
                    ship_count += 1
                elif next_row >= 0 and list[next_row][cell] == 1:
                    print("DOWN NEXT SHIP OUT")
                    return
                elif new_row >= 0 and list[new_row][cell] == 0:
                    print("DOWN CLEAN")
                    return ship_count
                elif new_row < 0:
                    print("DOWN CLOSE")
                    return ship_count
    
                new_row = new_row - 1
                next_row = next_row + 1
            
        if type == 3 and row - 2 < 0:
            return ship_count
          
    def radar(list, list2, row, cell, type):
        # print(list2, row, cell, type)

        for i in range(len(list2)):
            list2[i] = False

        if list[row][cell] == 2:
            if cell + 1 <= 9 and list[row][cell+1] == type:
                list2[0] = True
            if cell - 1 >= 0 and list[row][cell-1] == type:
                list2[1] = True
            if row + 1 <= 9 and list[row+1][cell] == type:
                list2[2] = True
            if row - 1 >= 0 and list[row-1][cell] == type:
                list2[3] = True 
        
        return list2
    
    def new_finder(list, row, cell):

        #########################
        # 100 nothing
        # 1 solo
        
        # 1-1 11 duo left
        # 1-2 12 duo top
        # 1-3 13 duo right
        # 1-4 14 duo down
        
        # 2-0 20 trio center gor///
        # 2-1 21 trio left gor
        # 2-2 22 trio right gor
        # 2-3 23 trio center ver////
        # 2-4 24 trio top ver
        # 2-5 25 trio down ver

        # 3-0 30 four 1center gor//
        # 3-1 31 four 2center gor//
        # 3-2 32 four left gor
        # 3-3 33 four right gor
        # 3-4 34 four 1center ver//
        # 3-5 35 four 2center ver//
        # 3-6 36 four top ver
        # 3-7 37 four down ver

        clean = radar(list, clean_side_list, row, cell, 0)
        ship = radar(list, ship_side_list, row, cell, 1)
        dead_ship = radar(list, dead_ship_side_list, row, cell, 2)

        if all(meaning for meaning in clean) or all(not meaning for meaning in ship) and all(not meaning for meaning in dead_ship):
            return 1
        
        if dead_ship[0] and dead_ship[1]:
            right = check_side(0, list, row, cell)
            left = check_side(1, list, row, cell)

            if right == 2 and left == 2:
                print("TRIO CENTER GOH")
                return 20
            
            elif right == 2 and left == 3:
                print("FOUR")
                return 31
            
            elif right == 3 and left == 2:
                print("FOUR 2")
                return 30
            
        if dead_ship[2] and dead_ship[3]:
            down = check_side(2, list, row, cell)
            top = check_side(3, list, row, cell)

            if down == 2 and top == 2:
                print("TRIO CENTER VER")
                return 23
            
            elif down == 2 and top == 3:
                print("FOUR VER ")
                return 35
            
            elif down == 3 and top == 2:
                print("FOUR VER 2")
                return 34
        
        for index, dead in enumerate(dead_ship) :
            print(dead, index)

            ##########

            if cell != 0 and dead and index == 0 and clean[1]:
                res = check_side(index, list, row, cell)
                print(f"ship_count {res}")
                if res == 2:
                    return  11               
                elif res == 3:
                    return 21               
                elif res == 4:
                    return  32


            if cell == 0 and dead and index == 0:
                res = check_side(index, list, row, cell)
                print(f"ship_count {res}")
                if res == 2:
                    return  11               
                elif res == 3:
                    return 21               
                elif res == 4:
                    return  32
            
            ##########
            
            if cell != 9 and dead and index == 1 and clean[0]:
                res = check_side(index, list, row, cell)
                print(f"ship_count {res}")
                if res == 2:
                    return 13                 
                elif res == 3:
                    return 22               
                elif res == 4:
                    return  33
            
            if cell == 9 and dead and index == 1:
                res = check_side(index, list, row, cell)
                print(f"ship_count {res}")
                if res == 2:
                    return 13                 
                elif res == 3:
                    return 22               
                elif res == 4:
                    return  33
            
            ##########
            
            if row != 0 and dead and index == 2 and clean[3]:
                res = check_side(index, list, row, cell)
                print("ship_count", res)
                if res == 2:
                    return 12                
                elif res == 3:
                    return 24               
                elif res == 4:
                    return  36

            if row == 0 and dead and index == 2:
                res = check_side(index, list, row, cell)
                print("ship_count", res)
                if res == 2:
                    return 12                
                elif res == 3:
                    return 24               
                elif res == 4:
                    return  36
            
            ##########
            
            if row != 9 and dead and index == 3 and clean[2]:
                res = check_side(index, list, row, cell)
                print("ship_count", res)
                if res == 2:
                    return 14                 
                elif res == 3:
                    return 25               
                elif res == 4:
                    return  37

            if row == 9 and dead and index == 3:
                res = check_side(index, list, row, cell)
                print("ship_count", res)
                if res == 2:
                    return 14                 
                elif res == 3:
                    return 25               
                elif res == 4:
                    return  37
        
        return 100

    try:
        print("True")
        connect_to()
    except:
        print("False")
        return

    data = json.dumps(player_map1)  
    client_socket.sendall(data.encode())  # Отправляем данные в байтовом формате
    print("sending map")

    data = client_socket.recv(400)
    player_map2 = json.loads(data.decode())
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
        global stop_thread

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
                skill = int(data[6])
                
                if skill == 1:
                    first_cell = True                         
                    bomb_list= [(row, cell), (row, cell- 1), (row, cell+ 1), (row- 1, cell), (row+ 1, cell), (row- 1, cell- 1), (row- 1, cell+ 1), (row+ 1, cell- 1), (row+ 1, cell+ 1)]
                    for coordinate in bomb_list:
                        if coordinate[0] >= 0 and coordinate[0] <= 9 and coordinate[1] >= 0 and coordinate[1] <= 9 and player_map2[coordinate[0]][coordinate[1]] == 1:
                            print(coordinate[0], coordinate[1], player_map2[coordinate[0]][coordinate[1]])
                            num = int(str(coordinate[0]) + str(coordinate[1]))
                            hit_list.append(pygame.Rect(row_list_enemy[num].x, row_list_enemy[num].y ,60, 60))   
                            player_map2[coordinate[0]][coordinate[1]] = 2
                            point += 10                   
                            row_list_enemy[num].CLOSE = True
                            
                            shot_type = new_finder(player_map2, coordinate[0], coordinate[1])
                            map(row_list_enemy, coordinate[0], coordinate[1], num, shot_type)

                            if first_cell:
                                print(coordinate[0], coordinate[1], num, 0, 1, kill_type= shot_type)
                                sending(coordinate[0], coordinate[1], num, 0, 1, kill_type= shot_type, skill= 2)
                                first_cell = False

                            print(f'Попал по кораблику')

                            
                            res = check_win()
                            print(res)
                            if res == "WIN":
                                turn = False
                                run_battle = False
                                back = win()
                                if back == "BACK":
                                    stop_thread = True
                                    return "BACK"

                        elif coordinate[0] >= 0 and coordinate[0] <= 9 and coordinate[1] >= 0 and coordinate[1] <= 9 and player_map2[coordinate[0]][coordinate[1]] == 0:
                            print(coordinate[0], coordinate[1], player_map2[coordinate[0]][coordinate[1]])


                print(skill)
                if skill == 2:
                    dynamite_list= [(c_row, c_cell), (c_row, c_cell- 1), (c_row, c_cell+ 1), (c_row- 1, c_cell), (c_row+ 1, c_cell)]
                    for coordinate in dynamite_list:
                        if coordinate[0] >= 0 and coordinate[0] <= 9 and coordinate[1] >= 0 and coordinate[1] <= 9 and player_map1[coordinate[0]][coordinate[1]] == 1:
                            print(coordinate[0], coordinate[1], player_map1[coordinate[0]][coordinate[1]])
                            num = int(str(coordinate[0]) + str(coordinate[1]))
                            hit_list.append(pygame.Rect(row_list_player[num].x, row_list_player[num].y ,60, 60))   
                            player_map1[coordinate[0]][coordinate[1]] = 2                 
                            row_list_player[num].CLOSE = True
                            
                            shot_type = new_finder(player_map1, coordinate[0], coordinate[1])
                            map(row_list_player, coordinate[0], coordinate[1], num, shot_type)

                            print(f'Попал по кораблику')
                            
                            res = check_win()
                            print(res)
                            if res == "WIN":
                                turn = False
                                run_battle = False
                                back = win()
                                if back == "BACK":
                                    stop_thread = True
                                    return "BACK"

                        elif coordinate[0] >= 0 and coordinate[0] <= 9 and coordinate[1] >= 0 and coordinate[1] <= 9 and player_map1[coordinate[0]][coordinate[1]] == 0:
                            print(coordinate[0], coordinate[1], player_map2[coordinate[0]][coordinate[1]])

                            num = int(str(coordinate[0]) + str(coordinate[1]))
                            miss_list.append(pygame.Rect(row_list_player[num].x, row_list_player[num].y, 60, 60))
                            print("Поле врага: Не попал", [coordinate[0]], [coordinate[1]] , player_map1[coordinate[0]][coordinate[1]])
                            row_list_player[num].CLOSE = True  
                            turn = False                  
                    
                empty= 0
                for item in row_list_player:
                    if empty == c_number:
                        if c_type == 1:                    
                            hit_list.append(pygame.Rect(item.x, item.y ,60, 60)) 
                            print(f"Изменение player_map2[{row}][{cell}] до: {player_map1[row][cell]}")
                            player_map1[c_row][c_cell] = 2
                            print(f"Изменение player_map2[{row}][{cell}] после: {player_map1[row][cell]}") 

                            map(row_list_player, c_row, c_cell, c_number, kill_type)  

                            res = check_lose()
                            if res == "LOSE":
                                stop_thread = False
                        
                        elif c_type == 0:
                            miss_list.append(pygame.Rect(item.x, item.y ,60, 60))  
                            print("miss")
                    
                    empty+= 1

    test_thread = Thread(target = always_recv) 
    test_thread.start()

    for ship in ship_list:
        ship.x += 3
        ship.y += 38

    while run_battle:    
        screen.fill((MAIN_WINDOW_COLOR))

        # screen.blit(clean_bg, (0, 0))

        if turn:
            screen.blit(lamp_active, (5, 175))
            screen.blit(lamp_unactive, (1335, 175))
        
        if not turn:
            screen.blit(lamp_unactive, (5, 175))
            screen.blit(lamp_active, (1335, 175))

        shot = True

        gap = 68
        for i in range(0, 7):
            screen.blit(frame, (gap, 12))
            gap += 120

        Text_point = Text(x= 1300, y= 20, text = str(point), color= "Black", text_size= 50)

        Text_point.text_draw(screen=screen)

        position = pygame.mouse.get_pos()
        press = pygame.mouse.get_pressed()
        
        res = check_lose()
        if res == "LOSE":
            turn = False
            run_battle = False
            back_lose = lose()
            if back_lose == "BACK":
                return "BACK"
            
        for skill in skills_list:
            skill.draw_skill(screen=screen)

        your_screen_text.button_draw(screen=screen)
        enemy_screen_text.button_draw(screen=screen)

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
                for ship in ship_list:
                    ship.ship_draw(screen= screen)  
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

        for skill in skills_list:
            skill.draw_skill(screen=screen)
            skill.move(position= position, press= press, screen= screen)

        # print(clock.get_fps())
        
        pygame.display.flip()
        clock.tick(FPS)      
        
        for event in pygame.event.get():

            if not press[1] and not press[2] and event.type == pygame.MOUSEBUTTONDOWN:  
                for skill in skills_list: 
                    if skill.rect.collidepoint(position):
                        print("TAKE")   
                        skill.take() 
            
            if event.type == pygame.MOUSEBUTTONUP and press[1]:             
                for item in row_list_enemy:
                    row = number // 10
                    cell = number % 10
                    if item.collidepoint(position):
                        print(turn)
                        print(row, cell, player_map2[row][cell])
                    
                    number += 1                    
            
            if event.type == pygame.MOUSEBUTTONUP and press[0] and not press[1] and not press[2]:      
                for skill in skills_list: 
                    if skill.plus_rect.collidepoint(position): 
                        buy = skill.plus(point) 

                        if buy:   
                            point -= 20
                    
                    if not sq_list[1].collidepoint(position) and not sq_list[0].collidepoint(position) and turn and not skill.TAKE:
                        print("OUT")
                        print(skill.rect_x, skill.rect_y)
                        print(skill.x,skill.y)
                        skill.rect_x = skill.x
                        skill.rect_y = skill.y
                        print("STOP")
                        skill.OUT = True
                        skill.TAKE = False 

                    number = 0 
                    for item in row_list_enemy:          
                        cell = number % 10
                        row = number // 10   

                        if item.collidepoint(position) and sq_list[1].collidepoint(position) and turn and skill.TAKE and not item.CLOSE:
                            if skill.id == 1:
                                print(f"ENEMY FEILD {skill.id}, {row}, {cell}")
                                print("BomB")

                                # first_cell = True
                                
                                # bomb_list= [(row, cell), (row, cell- 1), (row, cell+ 1), (row- 1, cell), (row+ 1, cell), (row- 1, cell- 1), (row- 1, cell+ 1), (row+ 1, cell- 1), (row+ 1, cell+ 1)]
                                # for coordinate in bomb_list:
                                #     if coordinate[0] >= 0 and coordinate[0] <= 9 and coordinate[1] >= 0 and coordinate[1] <= 9 and player_map2[coordinate[0]][coordinate[1]] == 1:
                                #         print(coordinate[0], coordinate[1], player_map2[coordinate[0]][coordinate[1]])
                                #         num = int(str(coordinate[0]) + str(coordinate[1]))
                                #         hit_list.append(pygame.Rect(row_list_enemy[num].x, row_list_enemy[num].y ,60, 60))   
                                #         player_map2[coordinate[0]][coordinate[1]] = 2
                                #         point += 10                   
                                #         row_list_enemy[num].CLOSE = True
                                        
                                #         shot_type = new_finder(player_map2, coordinate[0], coordinate[1])
                                #         map(row_list_enemy, coordinate[0], coordinate[1], num, shot_type)

                                #         if first_cell:
                                #             print(coordinate[0], coordinate[1], num, 0, 1, kill_type= shot_type)
                                #             sending(coordinate[0], coordinate[1], num, 0, 1, kill_type= shot_type, skill= 2)
                                #             first_cell = False

                                #         print(f'Попал по кораблику')
                                #         shot = False
                                        
                                #         res = check_win()
                                #         print(res)
                                #         if res == "WIN":
                                #             turn = False
                                #             run_battle = False
                                #             back = win()
                                #             if back == "BACK":
                                #                 stop_thread = True
                                #                 return "BACK"

                                #     elif coordinate[0] >= 0 and coordinate[0] <= 9 and coordinate[1] >= 0 and coordinate[1] <= 9 and player_map2[coordinate[0]][coordinate[1]] == 0:
                                #         print(coordinate[0], coordinate[1], player_map2[coordinate[0]][coordinate[1]])

                                #         num = int(str(coordinate[0]) + str(coordinate[1]))
                                #         # miss_list.append(pygame.Rect(row_list_enemy[num].x, row_list_enemy[num].y, 60, 60))
                                #         # print("Поле врага: Не попал", [coordinate[0]], [coordinate[1]] , player_map2[coordinate[0]][coordinate[1]])
                                #         # point += 2
                                #         # row_list_enemy[num].CLOSE = True  
                                #         # turn = False   
                                            
                                #         if first_cell:
                                #             sending(coordinate[0], coordinate[1], num, 0, 1, kill_type = 10, skill= 2)
                                #             first_cell = False 

                            if skill.id == 2:
                                print(f"ENEMY FEILD {skill.id}, {row}, {cell}")
                                print("Dynamite")

                                first_cell = True
                                
                                dynamite_list= [(row, cell), (row, cell- 1), (row, cell+ 1), (row- 1, cell), (row+ 1, cell)]
                                for coordinate in dynamite_list:
                                    if coordinate[0] >= 0 and coordinate[0] <= 9 and coordinate[1] >= 0 and coordinate[1] <= 9 and player_map2[coordinate[0]][coordinate[1]] == 1:
                                        print(coordinate[0], coordinate[1], player_map2[coordinate[0]][coordinate[1]])
                                        num = int(str(coordinate[0]) + str(coordinate[1]))
                                        hit_list.append(pygame.Rect(row_list_enemy[num].x, row_list_enemy[num].y ,60, 60))   
                                        player_map2[coordinate[0]][coordinate[1]] = 2
                                        point += 10                   
                                        row_list_enemy[num].CLOSE = True
                                        
                                        shot_type = new_finder(player_map2, coordinate[0], coordinate[1])
                                        map(row_list_enemy, coordinate[0], coordinate[1], num, shot_type)

                                        if first_cell:
                                            print(coordinate[0], coordinate[1], num, 0, 1)
                                            sending(coordinate[0], coordinate[1], num, 0, 1, kill_type= shot_type, skill= 2)
                                            first_cell = False

                                        print(f'Попал по кораблику')
                                        shot = False
                                        
                                        res = check_win()
                                        print(res)
                                        if res == "WIN":
                                            turn = False
                                            run_battle = False
                                            back = win()
                                            if back == "BACK":
                                                stop_thread = True
                                                return "BACK"

                                    elif coordinate[0] >= 0 and coordinate[0] <= 9 and coordinate[1] >= 0 and coordinate[1] <= 9 and player_map2[coordinate[0]][coordinate[1]] == 0:
                                        print(coordinate[0], coordinate[1], player_map2[coordinate[0]][coordinate[1]])

                                        num = int(str(coordinate[0]) + str(coordinate[1]))
                                        miss_list.append(pygame.Rect(row_list_enemy[num].x, row_list_enemy[num].y, 60, 60))
                                        print("Поле врага: Не попал", [coordinate[0]], [coordinate[1]] , player_map2[coordinate[0]][coordinate[1]])
                                        point += 2
                                        row_list_enemy[num].CLOSE = True  
                                        turn = False   
                                            
                                        if first_cell:
                                            sending(coordinate[0], coordinate[1], num, 0, 1, kill_type = 100, skill= 2)
                                            first_cell = False 
                            
                            
                            if skill.id == 3:
                                print(f"ENEMY FEILD {skill.id}, {row}, {cell}")
                                print("Unfire")

                            if skill.id == 4:
                                print(f"ENEMY FEILD {skill.id}, {row}, {cell}")
                                print("Flamethower")

                            if skill.id == 5:
                                print(f"ENEMY FEILD {skill.id}, {row}, {cell}")
                                print("Rocet")

                            if skill.id == 7:
                                print(f"ENEMY FEILD {skill.id}, {row}, {cell}")
                                print("Topedo")
                                for i in range(0, 10):
                                    print(player_map2[row][i], row, i)
                                    if player_map2[row][i] == 1 and shot:
                                        num = int(str(row) + str(i))
                                        hit_list.append(pygame.Rect(row_list_enemy[num].x, row_list_enemy[num].y ,60, 60))   
                                        print(f"Изменение player_map2[{row}][{i}] до: {player_map2[row][i]}")
                                        player_map2[row][i] = 2
                                        print(f"Изменение player_map2[{row}][{i}] после: {player_map2[row][i]}") 
                                        point += 10                   
                                        row_list_enemy[num].CLOSE = True
                                        
                                        shot_type = new_finder(player_map2, row, i)
                                        map(row_list_enemy, row, i, num, shot_type)

                                        sending(row, i, num, 0, 1, kill_type= shot_type)

                                        print(f'Попал по кораблику')
                                        shot = False
                                        
                                        res = check_win()
                                        print(res)
                                        if res == "WIN":
                                            turn = False
                                            run_battle = False
                                            back = win()
                                            if back == "BACK":
                                                stop_thread = True
                                                return "BACK"
                                            
                                if shot:
                                    turn = False   
                                    sending(0, 0, 0, 0, 1, kill_type = 10)
                            
                            shot = False

                        number += 1
              
                    number = 0 
                    for item in row_list_player:          
                        cell = number % 10
                        row = number // 10           

                        if item.collidepoint(position) and sq_list[0].collidepoint(position) and turn and skill.TAKE and not item.CLOSE:
                            if skill.id == 6:
                                print(f"ENEMY FEILD {skill.id}, {row}, {cell}")
                                print("Sild")
                            
                            shot = False
                        
                        
                        number += 1

                
                if shot:
                    number = 0
                    for item in row_list_enemy:          
                        cell = number % 10
                        row = number // 10           

                        if item.collidepoint(position) and sq_list[1].collidepoint(position) and player_map2[row][cell] == 1 and not item.CLOSE and turn: 
                            hit_list.append(pygame.Rect(item.x, item.y ,60, 60))   
                            print(f"Изменение player_map2[{row}][{cell}] до: {player_map2[row][cell]}")
                            player_map2[row][cell] = 2
                            print(f"Изменение player_map2[{row}][{cell}] после: {player_map2[row][cell]}") 
                            point += 10                   
                            item.CLOSE = True
                            
                            shot_type = new_finder(player_map2, row, cell)
                            map(row_list_enemy, row, cell, number, shot_type)

                            sending(row, cell, number, 1, 0, kill_type= shot_type)

                            res = check_win()
                            print(res)
                            if res == "WIN":
                                turn = False
                                run_battle = False
                                back = win()
                                if back == "BACK":
                                    stop_thread = True
                                    return "BACK"
                
                        elif item.collidepoint(position) and sq_list[1].collidepoint(position) and player_map2[row][cell] == 0 and not item.CLOSE and turn:
                            miss_list.append(pygame.Rect(item.x, item.y, 60, 60))
                            print("Поле врага: Не попал", row , cell , player_map2[row][cell])
                            point += 2
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

            shot = True

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
        
        pygame.display.flip()
        clock.tick(FPS) 
        
        for event in pygame.event.get():
            if press[0]:
                back_to_menu = button_back_menu.checkPress(position = position, press = press)

                if back_to_menu:
                    return "BACK"
            
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
        
        pygame.display.flip()
        clock.tick(FPS) 
        
        for event in pygame.event.get():
            if press[0]:
                back_to_menu = button_back_menu.checkPress(position = position, press = press)
        
                if back_to_menu:
                    return "BACK"
            
            if event.type == pygame.QUIT:
                run_lose = False
                pygame.quit()
