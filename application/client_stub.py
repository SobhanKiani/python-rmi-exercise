from rmi.stub_base import StubBase
from .api import CustomAPI

# Client should use an object of this class 
# Client May And May Not Extend CustomAPI 
# But Client Stub Needs To Extends As It Needs To Implement The Remote Invocation For Each Method 
class ClientStub(StubBase, CustomAPI):

    # implement sending invocation to server skeleton
    def print_message(self, msg: str) -> None:
        pass
        
