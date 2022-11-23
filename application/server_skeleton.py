from .server_impl import ServerImpl
from .api import CustomAPI
from rmi.skeleton_base import SkeletonBase


class ServerSkeleton(SkeletonBase, CustomAPI):
    def __init__(self, port, ip):
        super().__init__(port, ip, 'Test', '1.0.0')
        self.server_impl = ServerImpl()

    def print_message(self, msg: str):
        # server_message should be sent back to the client
        server_message = self.server_impl.print_message(msg)

    # ** A method is needed to get messages from stub
    # stub send invocation request
    # this message handler should determine which method to call
    def stub_message_handler(self):
        pass
