import socket
import io
import os

from threading import Thread

def start_server(): 
    client_list = []

    # створили socket для передачи даних вказавши версію IP TCP тип з'єднання
    with socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM) as server_socket:
        # зв'язуємо socket з IP та портом
        server_socket.bind(("0.0.0.0", 8081))

        server_socket.listen()
        client_socket, adress = server_socket.accept()
        client_list.append((client_socket, adress))
        print("connected", client_list[0])

        
        # server_socket.listen()
        # client_socket, adress = server_socket.accept()
        # client_list.append((client_socket, adress))
        # print("connected", client_list[1])
        
        # while True:
        #     map = client_socket.rec(100).decode()

        
server_thred = Thread(target = start_server) 
server_thred.start()
print("Работаю одновременно с запуском сервера")
