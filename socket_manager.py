from socket import socket
from messages import Message, SendingMessage, RecievingMessage


class SocketManager:
    def __init__(self, ip, port, sending_message: SendingMessage=None) -> None:
        self.ip = ip
        self.port = port
        self.sending_message = sending_message
        s = socket()
        self.socket = s

    def connect(self):
        self.socket.connect((self.ip, self.port))
    
    def close(self):
        self.socket.close()

    def send_message_without_response(self):
        self.socket.send(self)
        self.socket.send(self.sending_message.dumps())
        self.socket.close()
    
    
    def send_message_and_get_response(self):
        self.socket.send(self.sending_message.dumps())

        response = self.socket.recv(1024)
        response = RecievingMessage(response)

        self.socket.close()
        return response
    
    def set_message(self, sending_message:SendingMessage):
        self.sending_message = sending_message
