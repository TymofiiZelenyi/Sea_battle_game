import socket
import io
import os
from threading import Thread


#def start_server():
#    #створили socket для передачі даних вказавши версію IP TCP тип з'єднання
#    with socket.socket(family = socket.AF_INET, type= socket.SOCK_STREAM) as server_socket:
#        #зв'язуємо socket з IP та портом
#        server_socket.bind(("0.0.0.0"), 8080)
#        #Переводить socket в режим очікування
#        server_socket.listen()
#        print("connecting ... ")
#
#        # Очікує та приймає підключення клієнту
#        client_socket, adress = server_socket.aceept()
#        print("Connected user - ", adress)
#
#        data = client_socket.recv(10).decode()
#        print(data)
#
#thread_server = Thread(target= start_server)
#thread_server.start()
#
#print("Create first thread")