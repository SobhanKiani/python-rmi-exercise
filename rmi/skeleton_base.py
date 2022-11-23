from abc import ABC, abstractmethod
from socket import socket
from messages import SendingMessage, RecievingMessage, MessageTypes
from socket_manager import SocketManager

class SkeletonBase(ABC):
    registry_ip = 'localhost'
    registry_port = 9090

    # *** class name and version change to be static
    def __init__(self, ip, port, class_name, class_version):
        self.port = port
        self.ip = ip
        self.class_name = class_name
        self.class_version = class_version
        self.socket = None

    def start(self,):
        sm = SocketManager(self.registry_ip, self.registry_port)
        sm.connect()
        self.sm = sm 
        self.register()
        # s.connect((self.registry_ip, self.registry_port))
        # self.socket = s
        # self.register()

        # ACCEPT REQUESTS FROM STUBS
        while True:
            self.stub_message_handler()

    def register(self):
        register_message = {
            'ip': self.ip,
            'port': self.port,
            'class_name': self.class_name,
            'class_version': self.class_version
        }
        register = SendingMessage(
            register_message, MessageTypes.REGISTER_SERVER, 200)
        
        self.sm.set_message(register)
        response = self.sm.send_message_and_get_response()
        # self.socket.send(register.dumps())

        # msg = self.socket.recv(1024)
        # response = RecievingMessage(msg)
        print(response.status_code, response.msg)

    @abstractmethod
    def stub_message_handler(self):
        pass
