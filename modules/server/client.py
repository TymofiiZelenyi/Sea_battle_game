import socket
import io



with socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM) as client_socket:
    #підключаємо клієнта до серверу
    client_socket.connect(("192.168.1.12", 8081))