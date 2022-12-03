from socket import socket

c1 = socket()
c1.connect(('localhost', 8888))
c1.send("c1".encode())

c2 = socket()
c2.connect(('localhost', 8888))
c2.send("c2".encode())
