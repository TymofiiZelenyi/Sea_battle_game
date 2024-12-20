import socket
import io
import os

from threading import Thread

def start_server(): 
    # створили socket для передачи даних вказавши версію IP TCP тип з'єднання
    with socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM) as server_socket:
        # зв'язуємо socket з IP та портом
        server_socket.bind(("192.168.1.12", 8081))

        server_socket.listen(2)
        client_socket1, adress = server_socket.accept()
        print("connected", client_socket1, adress)

        client_socket2, adress = server_socket.accept()
        print("connected", client_socket2, adress)
        
        while True:
            print(f"PLAYER 1 {client_socket1.recv(10).decode()}")
            print(f"PLAYER 2 {client_socket2.recv(10).decode()}")
            
            

server_thred = Thread(target = start_server) 
server_thred.start()
print("Работаю одновременно с запуском сервера")
