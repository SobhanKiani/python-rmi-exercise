from socket import socket

c2 = socket()
c2.connect(('localhost', 8888))
c2.send("c2".encode())