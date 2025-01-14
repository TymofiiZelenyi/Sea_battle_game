import socket 
import random 
 
from threading import Thread 
 
def start_server():  
    # створили socket для передачи даних вказавши версію IP TCP тип з'єднання 
    with socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM) as server_socket: 
        # зв'язуємо socket з IP та портом 
        server_socket.bind(("localhost", 8081)) #той айпішнік, який не дома у Тимофія 
 
        server_socket.listen(2) 

        try:
            client_socket1, adress1 = server_socket.accept() 
            print(client_socket1, adress1) 
        except socket.timeout:
            print("TIMEOUT 1")
            return
 

        try:
            client_socket2, adress2 = server_socket.accept() 
            print(client_socket2, adress2) 
        except socket.timeout:
            print("TIMEOUT 2")
            return
 
        data1 = client_socket1.recv(4096)  # Преобразуем байты в строку 
        client_socket2.sendall(data1) 
 
        data2 = client_socket2.recv(4096)  # Преобразуем байты в строку 
        client_socket1.sendall(data2) 
 
        number = int(random.randint(0, 1)) 
        print(number) 
        if not number: 
            print("first 1") 
            client_socket1.sendall("you".encode()) 
            client_socket2.sendall("not".encode()) 
        elif number: 
            print("first 2") 
            client_socket1.sendall("not".encode()) 
            client_socket2.sendall("you".encode()) 
 
        print(number) 
 
        while True:   
            if number == 1: 
                shot2 = client_socket2.recv(35).decode() 
 
                shot2 = shot2.strip("[]") 
                shot2 = [int(num) for num in shot2.split(",")] 
                number = bool(shot2[4]) 
                number = not number 
                number = int(number) 
                shot2 = ",".join(map(str, shot2)) 
 
                client_socket1.sendall(shot2.encode()) 
                
            elif number == 0: 
                shot1 = client_socket1.recv(35).decode() 
 
                shot1 = shot1.strip("[]") 
                shot1 = [int(num) for num in shot1.split(",")] 
                number = int(shot1[4]) 
                shot1 = ",".join(map(str, shot1)) 
 
                client_socket2.sendall(shot1.encode())  
 
server_thread = Thread(target = start_server)  
# server_thread.start() 
# print("Работаю одновременно с запуском сервера")
