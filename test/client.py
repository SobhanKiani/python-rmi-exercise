from socket import socket

c1 = socket()
c1.connect(('localhost', 8888))
c1.send("c1".encode())


