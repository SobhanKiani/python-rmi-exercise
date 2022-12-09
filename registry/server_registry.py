from socket_manager import SocketManager
from messages import SendingMessage, MessageTypes
import sys

parent_module = sys.modules['.'.join(__name__.split('.')[:-1]) or '__main__']
if __name__ == '__main__' or parent_module.__name__ == '__main__':
    from server_metadata import ServerMetaData
else:
    from .server_metadata import ServerMetaData


class ServerRegsitry:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.servers = []
        self.sm = None

    # handles add new server to servers
    def add_server(self, serverMetaData: dict):
        new_server_metadata = ServerMetaData(**serverMetaData)
        self.servers.append(new_server_metadata)
        print(
            f"Server Registred IP {new_server_metadata.ip} and PORT {new_server_metadata.port} For Class {new_server_metadata.class_name}:{new_server_metadata.class_version}")
        return "SERVER_ADDED_TO_REGISTRY", 200

    # find by class name and class version
    def find_server(self, class_name, class_version):
        found_server = None
        for server in self.servers:
            if server.class_name == class_name and server.class_version == class_version:
                found_server = server

        if found_server != None:
            server_data = {
                'ip': found_server.ip,
                'port': found_server.port,
                'class_name': found_server.class_name,
                'class_version': found_server.class_version
            }
            return server_data, MessageTypes.SERVER_FOUND, 200
        else:
            return 'SERVER_COULD_NOT_BE_FOUND', MessageTypes.SERVER_NOT_FOUND, 400

    # run Registry on the given port and ip address
    def start(self):

        sm = SocketManager()
        sm.bind(self.ip, self.port, 5)
        print("Server Registry Started...")
        
        while True:
            c, req = sm.recieve_message()

            if req.type == MessageTypes.REGISTER_SERVER:
                res_message, res_status = self.add_server(req.msg)
                res = SendingMessage(
                    res_message, MessageTypes.REGISTERED, res_status)
                c.send(res.dumps())

            elif req.type == MessageTypes.FIND_SERVER:
                res_message, res_type, res_status = self.find_server(
                    req.msg['class_name'], req.msg['class_version'])
                res = SendingMessage(res_message, res_type, res_status)
                c.send(res.dumps())
