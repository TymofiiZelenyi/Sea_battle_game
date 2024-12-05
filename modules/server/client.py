#import socket
#import io
#
#with socket.socket(family= socket.AF_INET, type= socket.SOCK_STREAM) as clint_socket:
#  clint_socket.connect(("192.168.1.1", 8080))
#
#  hi = "Heeloo matha faka!"
#
#  clint_socket.send(hi.encode())