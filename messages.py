import json


# Base Message Properties
class Message:
    def __init__(self, msg, type, status_code=200):
        self.msg = msg
        self.type = type
        self.status_code = status_code

# Encasuplate Data Of Message That Are Being Sent By A Socket
class SendingMessage(Message):
    def __init__(self, msg, type:str, status_code:int=200):
        super().__init__(msg, type, status_code)
        

    def dumps(self):
        sending = {
            'msg': self.msg,
            'type': self.type,
            'status_code': self.status_code
        }
        return json.dumps(sending).encode('utf-8')

# Encapsulat Data Of Messages That Are Being Received By A Socket
class RecievingMessage(Message):
    def __init__(self, recieved_data:bytes):
        try:
            self.recieved_data = recieved_data.decode()
            loaded = json.loads(self.recieved_data)
            super().__init__(loaded['msg'], loaded['type'], loaded['status_code'])
        except:
            pass


# Different Message Types
class MessageTypes:
    REGISTER_SERVER = 'REGISTER_SERVER'
    FIND_SERVER = 'FIND_SERVER'
    REGISTERED = 'REGISTERED'
    SERVER_FOUND = "SERVER_FOUND"
    SERVER_NOT_FOUND = "SERVER_NOT_FOUND"
    FUNCTION_INVOCATION = "FUNCTION_INVOCATION"
    FUNCTION_INVOCATION_RESPONSE = "FUNCTION_INVOCATION_RESPONSE"


