import socket
import io
import os

from threading import Thread

def start_server(): 

    R = "ready"
    
    # створили socket для передачи даних вказавши версію IP TCP тип з'єднання
    with socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM) as server_socket:
        # зв'язуємо socket з IP та портом
        server_socket.bind(("192.168.1.101", 8081)) #той айпішнік, який не дома у Тимофія

        server_socket.listen(2)
        client_socket1, adress = server_socket.accept()
        print("connected", client_socket1, adress)

        client_socket2, adress = server_socket.accept()
        print("connected", client_socket2, adress)

        p1 = client_socket1.recv(400)
        client_socket2.send(p1)
        print("sending1 to 2 map")

        p2 = client_socket2.recv(400)
        client_socket1.send(p2)
        print("sending2 to 1 map")

        # while True:

            # shot1 = client_socket1.recv(10).decode()
            # print(shot1)
            # if shot1:
            #     print("send 2 by 1")
                # client_socket2.sendall(shot1.encode())
            
            # shot2 = client_socket2.recv(10).decode()
            # print(shot2)
            # if shot2:
            #     print("send 1 by 2")
                # client_socket1.sendall(shot2.encode())
        

server_thread = Thread(target = start_server) 
server_thread.start()
print("Работаю одновременно с запуском сервера")
