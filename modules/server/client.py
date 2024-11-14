#import socket
#import io
#
#with socket.socket(family= socket.AF_INET, type= socket.SOCK_STREAM) as clint_socket:
#    clint_socket.connect(("", 8080))
#
#    hi = "Heeloo"
#
#    clint_socket.send(hi.encode())