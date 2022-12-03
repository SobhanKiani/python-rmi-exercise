from socket import socket
from messages import SendingMessage, RecievingMessage


# class SocketManager:
#     def __init__(self, ip, port, sending_message: SendingMessage=None) -> None:
#         self.ip = ip
#         self.port = port
#         self.sending_message = sending_message
#         s = socket()
#         self.socket = s

#     def connect(self):
#         self.socket.connect((self.ip, self.port))

#     def close(self):
#         self.socket.close()

#     def send_message_without_response(self):
#         self.socket.send(self)
#         self.socket.send(self.sending_message.dumps())
#         self.socket.close()


#     def send_message_and_get_response(self):
#         self.socket.send(self.sending_message.dumps())

#         response = self.socket.recv(1024)
#         response = RecievingMessage(response)

#         self.socket.close()
#         return response

#     def set_message(self, sending_message:SendingMessage):
#         self.sending_message = sending_message

class SocketManager:
    def __init__(self, dest_ip=None, dest_port=None) -> None:
        self.ip = dest_ip
        self.port = dest_port
        s = socket()
        self.socket = s

    def connect(self):
        self.socket.connect((self.ip, self.port))

    def close(self):
        self.socket.close()

    def send_message_without_response(self, msg, message_type: str, status_code: int):
        sending_message = SendingMessage(msg, message_type, status_code)
        self.socket.send(sending_message.dumps())
        self.socket.close()

    def send_message_and_get_response(self, msg, message_type: str, status_code: int):
        sending_message = SendingMessage(msg, message_type, status_code)

        self.socket.send(sending_message.dumps())

        response = self.socket.recv(1024)
        response = RecievingMessage(response)

        self.socket.close()
        return response

    def recieve_message(self):
        c, _ = self.socket.accept()
        recieved = c.recv(1024)
        recieved = RecievingMessage(recieved)

        # What recived from who
        return c, recieved

    def bind(self, ip: str, port: int, n_client: int):
        self.socket.bind((ip, port))
        self.socket.listen(n_client)

    def set_ip_and_port(self, ip: str, port: int):
        self.ip = ip
        self.port = port
