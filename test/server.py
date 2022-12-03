from socket import socket


server = socket()
server.bind(('localhost', 8888))
server.listen(5)

count = 0
while True:
    c, _ = server.accept()
    count += 1
    print("NEW CONNECTION")
    recieved = c.recv(1024)
    print(f'RECIVED {count}: {recieved}')
    print(f"NUMBER OF CONNECTIONS: {count}")
    
