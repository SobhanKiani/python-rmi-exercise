from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
import json
from CustomThread import CustomThread
from time import sleep


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
        try:
            self.recieved_data = recieved_data.decode()
            loaded = json.loads(self.recieved_data)
            super().__init__(loaded['msg'], loaded['type'], loaded['status_code'])
        except:
            pass


class SocketManager:
    def __init__(self, dest_ip=None, dest_port=None) -> None:
        self.ip = dest_ip
        self.port = dest_port
        s = socket(AF_INET, SOCK_STREAM)
        s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        
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

    def recieve_message(self, conn, addr):
        # c, _ = self.socket.accept()
        recieved = conn.recv(1024)
        recieved = RecievingMessage(recieved)
        for i in range(20):
            sleep(0.1)
        # What recived from who
        
        return recieved

    def bind(self, ip: str, port: int, n_client: int):
        self.socket.bind((ip, port))
        self.socket.listen(n_client)

        while True:
            conn, addr = self.socket.accept()
            print("CLIENT CONNECTED")

            # print('ADDR', addr)
            t = CustomThread(target=self.recieve_message, args=(conn, addr))
            t.start()
            t.join()

            rec = t._return
            if rec != None:
                print(rec.msg)
            else:
                print("REC IS NONE")

    def set_ip_and_port(self, ip: str, port: int):
        self.ip = ip
        self.port = port



reciever = SocketManager()
reciever.bind('localhost', 7777, 10)
