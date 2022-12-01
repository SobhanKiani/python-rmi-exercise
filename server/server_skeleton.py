from .server_impl import ServerImpl
from application.api import CustomAPI
from server.skeleton_base import SkeletonBase
from messages import SendingMessage, MessageTypes

class ServerSkeleton(SkeletonBase, CustomAPI):
    def __init__(self, port, ip, obj: ServerImpl):
        super().__init__(port, ip, 'Test', '1.0.0')
        self.server_impl = obj

    def print_message(self, msg: str):
        # server_message should be sent back to the client
        server_message = self.server_impl.print_message(msg)
        return server_message

    # This Message Handler Calls The Functions By Correct Params
    def stub_message_handler(self):
        while True:
            c, req = self.sm.recieve_message()
            function = eval('self.'+req.msg['method_name'])
            params = {}
            print(req.msg['params'])
            for param in req.msg['params']:
                if param['type'] == 'ref':
                    pass
                else:
                    param_type = eval(param['type'])
                    params[param['name']] = param_type(param['value'])
            res = function(**params)

            s = SendingMessage({"response": res},
                               MessageTypes.FUNCTION_INVOCATION_RESPONSE, 200)
            c.send(s.dumps())
