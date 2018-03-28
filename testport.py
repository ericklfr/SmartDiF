import socket
from random import randint

def check_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex(('127.0.0.1', port))
    if result == 0:
        return check_port(randint(26490,26494))
    else:
        return port
    s.close()


