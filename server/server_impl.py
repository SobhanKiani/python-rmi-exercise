from application.api import CustomAPI

class ServerImpl(CustomAPI):

    def print_message(self, msg: str, obj):
        server_message = f"This Is A Message From ServerImpl: {msg}"
        print("---Start---")
        print(server_message)
        print(f"And This is the data {obj.data}")
        print("---End---")
        print()
        return server_message