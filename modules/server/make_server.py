import socket
import io
import os

from threading import Thread
from ..game import settings as st




def start_server(): 
    # створили socket для передачи даних вказавши версію IP TCP тип з'єднання
    with socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM) as server_socket:
        # зв'язуємо socket з IP та портом
        server_socket.bind(("0.0.0.0", 8081))
        #Переводить socket в режим очікування
        server_socket.listen()

        print("connecting ... ")
        # Очікує та приймає підключення клієнту
        client_socket, adress = server_socket.accept()

        print("connected", adress)
    if server_socket.listen(2):
       st.two_players_connected = True
       print("Two players join")

server_thred = Thread(target = start_server) 
server_thred.start()
print("Работаю одновременно с запуском сервера")
#import socket
#import io
#import os
#from threading import Thread
#
#
#def start_server():
#  #створили socket для передачі даних вказавши версію IP TCP тип з'єднання
#  with socket.socket(family = socket.AF_INET, type= socket.SOCK_STREAM) as server_socket:
#      #зв'язуємо socket з IP та портом
#      server_socket.bind(("0.0.0.0", 8081))
#      #Переводить socket в режим очікування
#      server_socket.listen(2)
#      if server_socket.listen(2):
#        print("Two players join")
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