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
        self.sm = None

    def start(self,):
        sm = SocketManager()
        sm.bind(self.ip, self.port, 5)
        print("Skeleton Started To Listen...")
        self.sm = sm 
        self.register()

        # ACCEPT REQUESTS FROM STUBS
        while True:
            self.stub_message_handler()

    def register(self):
        register_sm = SocketManager(self.registry_ip, self.registry_port)
        register_sm.connect()
        # self.sm.set_ip_and_port(self.registry_ip, self.registry_port)
        # self.sm.connect()
        register_message = {
            'ip': self.ip,
            'port': self.port,
            'class_name': self.class_name,
            'class_version': self.class_version
        }
        response = register_sm.send_message_and_get_response(register_message, MessageTypes.REGISTER_SERVER, 200)
        register_sm.close()
        print(response.status_code, response.msg)

    @abstractmethod
    def stub_message_handler(self):
        pass
