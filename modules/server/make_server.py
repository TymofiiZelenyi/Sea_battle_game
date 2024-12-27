import socket
import random

from threading import Thread

def start_server(): 

    R = "ready"
    
    # створили socket для передачи даних вказавши версію IP TCP тип з'єднання
    with socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM) as server_socket:
        # зв'язуємо socket з IP та портом
        server_socket.bind(("192.168.1.106", 8081)) #той айпішнік, який не дома у Тимофія

        server_socket.listen(2)
        client_socket1, adress = server_socket.accept()
        print("connected", client_socket1, adress)

        client_socket2, adress = server_socket.accept()
        print("connected", client_socket2, adress)

        data1 = client_socket1.recv(4096)  # Преобразуем байты в строку
        client_socket2.sendall(data1)
        print("sending1 to 2 map")

        data2 = client_socket2.recv(4096)  # Преобразуем байты в строку
        client_socket1.sendall(data2)
        print("sending2 to 1 map")

        number = random.randrange(0, 1)
        if not number:
            print("first 1")
            client_socket1.sendall(str(1).encode())
            client_socket2.sendall(str(0).encode())
        if number:
            print("first 2")
            client_socket1.sendall(str(0).encode())
            client_socket2.sendall(str(1).encode())

        while True:

            try:
                shot1 = client_socket1.recv(12).decode()
                if shot1:
                    print("send 2 by 1")
                    print(shot1)
                    client_socket2.sendall(shot1.encode())

            except:        
                shot2 = client_socket2.recv(12).decode()
                if shot2:
                    print("send 1 by 2")
                    print(shot2)
                    client_socket1.sendall(shot2.encode())
        

server_thread = Thread(target = start_server) 
server_thread.start()
print("Работаю одновременно с запуском сервера")
