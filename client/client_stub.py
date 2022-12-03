from client.stub_base import StubBase
from application.api import CustomAPI
from socket_manager import SocketManager
from messages import MessageTypes
import json
# Client should use an object of this class
# Client May And May Not Extend CustomAPI
# But Client Stub Needs To Extends As It Needs To Implement The Remote Invocation For Each Method


class TestObj:
    def __init__(self, data) -> None:
        self.data = data


class ClientStub(StubBase, CustomAPI):

    # implement sending invocation to server skeleton
    def print_message(self, msg: str) -> None:
        sm = SocketManager(
            self.skeleton_info['ip'], self.skeleton_info['port'])

        invocation_msg = {
            'method_name': 'print_message',
            'params': [
                {'name': 'msg', 'value': msg, 'type': 'str'},
                {'name': 'obj', 'value': json.dumps(
                    TestObj(data='Test Data').__dict__), 'type': 'ref', 'instanceof': 'TestObj'}
            ],
        }
        sm.connect()
        response = sm.send_message_and_get_response(
            invocation_msg, MessageTypes.FUNCTION_INVOCATION, 200)
        print(response.msg)
        if response.status_code == 200:
            return response.msg
        sm.close()
