from .server_metadata import ServerMetaData
from socket import socket
from messages import RecievingMessage, SendingMessage, MessageTypes
from socket_manager import SocketManager


class ServerRegsitry:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.servers = []
        self.sm = None

    def add_server(self, serverMetaData: dict):
        new_server_metadata = ServerMetaData(**serverMetaData)
        self.servers.append(new_server_metadata)
        print("SERVER_ADDED_TO_REGISTRY")
        return "SERVER_ADDED_TO_REGISTRY", 200

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
