from application.api import CustomAPI

class ServerImpl(CustomAPI):

    def print_message(self, msg: str):
        server_message = f"This Is A Message From ServerImpl: {msg}"
        print("---Start---")
        print(server_message)
        print("---End---")
        print()
        return server_message