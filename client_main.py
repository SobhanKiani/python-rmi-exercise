import sys

parent_module = sys.modules['.'.join(__name__.split('.')[:-1]) or '__main__']
if __name__ == '__main__' or parent_module.__name__ == '__main__':
    from client.client_stub import ClientStub
else:
    from .client.client_stub import ClientStub


if __name__ == '__main__':
    client_stub = ClientStub('localhost', 9992)
    client_stub.lookup("Test", '1.0.0')
    client_stub.print_message('HELLO')