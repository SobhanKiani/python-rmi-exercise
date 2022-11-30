from abc import ABC
from socket import socket
from messages import SendingMessage, RecievingMessage, MessageTypes
from socket_manager import SocketManager

class StubBase(ABC):
    registry_ip = 'localhost'
    registry_port = 9090

    def __init__(self, ip, port) -> None:
        self.ip = ip
        self.port = port
        # self.lookup(
        #     'Test', "1.0.0")

    def lookup(self, class_name, class_version):
        findin_options = {
            'class_name': class_name,
            'class_version': class_version
        }

        sm = SocketManager(self.registry_ip, self.registry_port)
        sm.connect()
        response = sm.send_message_and_get_response(findin_options, MessageTypes.FIND_SERVER, 200)
        sm.close()

        if response.status_code == 200:
            self.skeleton_info = {
                'ip': response.msg['ip'],
                'port': response.msg['port'],
                'class_name': response.msg['class_name'],
                'class_version': response.msg['class_version'],
            }
        else:
            self.skeleton_info = None
        print(self.skeleton_info['ip'], self.skeleton_info['port'])
        return response
