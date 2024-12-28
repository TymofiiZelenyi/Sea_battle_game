import socket
import random

from threading import Thread

def start_server(): 

    R = "ready"
    
    # створили socket для передачи даних вказавши версію IP TCP тип з'єднання
    with socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM) as server_socket:
        # зв'язуємо socket з IP та портом
        server_socket.bind(("192.168.1.12", 8081)) #той айпішнік, який не дома у Тимофія

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

        while True:  

            if number:
                shot2 = client_socket2.recv(20).decode()
                print("send 1 by 2")
                shot2 = shot2.strip("[]")
                print(type(shot2), shot2)
                shot2 = [int(num) for num in shot2.split(",")]
                number = int(not bool(shot2[4]))
                print(number)
                shot2 = ",".join(map(str, shot2))
                client_socket1.sendall(shot2.encode())
                print("sendall 1")  

            elif not number:
                shot1 = client_socket1.recv(20).decode()
                shot1 = shot1.strip("[]")
                print("send 2 by 1")
                print(type(shot1), shot1)
                shot1 = [int(num) for num in shot1.split(",")]
                number = int(not bool(shot2[4]))
                print(number)
                shot1 = ",".join(map(str, shot1))
                client_socket2.sendall(shot1.encode())
                print("sendall 2")     

server_thread = Thread(target = start_server) 
server_thread.start()
print("Работаю одновременно с запуском сервера")
