from socket import socket
from messages import SendingMessage, RecievingMessage
from custome_thread import CustomThread


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
        try:
            sending_message = SendingMessage(msg, message_type, status_code)
            self.socket.send(sending_message.dumps())
            self.socket.close()
        except:
            pass

    def send_message_and_get_response(self, msg, message_type: str, status_code: int):
        try:
            sending_message = SendingMessage(msg, message_type, status_code)

            self.socket.send(sending_message.dumps())

            response = self.socket.recv(1024)
            response = RecievingMessage(response)

            self.socket.close()
            return response
        except:
            pass

    def recieve_message(self):
        conn, _ = self.socket.accept()

        thread = CustomThread(target=self.recieve_handler, args=(conn,))
        thread.start()
        thread.join()

        received = thread._return
        return conn, received

    def recieve_handler(self, conn):
        recieved = conn.recv(1024)
        recieved = RecievingMessage(recieved)

        return recieved

    def bind(self, ip: str, port: int, n_client: int):
        self.socket.bind((ip, port))
        self.socket.listen(n_client)

    def set_ip_and_port(self, ip: str, port: int):
        self.ip = ip
        self.port = port
