from socket import socket
import json


class Message:
    def __init__(self, msg, type, status_code=200):
        self.msg = msg
        self.type = type
        self.status_code = status_code


class SendingMessage(Message):
    def __init__(self, msg, type: str, status_code: int = 200):
        super().__init__(msg, type, status_code)

    def dumps(self):
        sending = {
            'msg': self.msg,
            'type': self.type,
            'status_code': self.status_code
        }
        return json.dumps(sending).encode('utf-8')


class RecievingMessage(Message):
    def __init__(self, recieved_data: bytes):
        self.recieved_data = recieved_data.decode()
        try:
            loaded = json.loads(self.recieved_data)
            super().__init__(loaded['msg'],
                             loaded['type'], loaded['status_code'])
        except:
            super().__init__('None', 500)


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
        # self.socket.close()

    def send_message_and_get_response(self, msg, message_type: str, status_code: int):
        try:
            sending_message = SendingMessage(msg, message_type, status_code)

            self.socket.send(sending_message.dumps())

            response = self.socket.recv(1024)
            response = RecievingMessage(response)

            # self.socket.close()
            return response
        except:
            pass

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


while True:
    sender = SocketManager('localhost', 7777)
    sender.connect()
    sender.send_message_and_get_response("TEST FROM CLIENT 1", "TEST", 200)
# sender.close()
