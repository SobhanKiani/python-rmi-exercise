from .server_impl import ServerImpl
from application.api import CustomAPI
from server.skeleton_base import SkeletonBase
from messages import SendingMessage, MessageTypes

### Should i remove server_impl and impletment methods here
### Or I can remove CustomAPI and Implement evrything in server_impl
### Implementation should be a service for skeleton
### Implementation should be seperated from skeleton
### 1.So ServerSkeleton Can Change It's name to Server and implement methods here 
### (Couples Implmentation With Skeleton Functionalities)
### 2.ServerSkeleton Can Utilize ServerImpl As It's Object. 
### It may or may not extend CustomAPI
### * 3. The Other Approach Is That ServerSkeleton Can Extend ServerImpl Beside SkeletonBase
### Then The Name Can Change To Server

### Result: ServerSkeleton is NOT responsible for implementation and should consider ServerImplementation

class ServerSkeleton(SkeletonBase, CustomAPI):
    def __init__(self, port, ip):
        super().__init__(port, ip, 'Test', '1.0.0')
        self.server_impl = ServerImpl()

    def print_message(self, msg: str):
        # server_message should be sent back to the client
        server_message = self.server_impl.print_message(msg)
        return server_message

    # This Message Handler Calls The Functions By Correct Params
    def stub_message_handler(self):
        c, req = self.sm.recieve_message()
        function = eval('self.'+req.msg['method_name'])
        params = {}
        print(req.msg['params'])
        for param in req.msg['params']:
            param_type = eval(param['type'])
            params[param['name']] = param_type(param['value'])
        res = function(**params)

        s = SendingMessage({"response": res},
                           MessageTypes.FUNCTION_INVOCATION_RESPONSE, 200)
        c.send(s.dumps())
