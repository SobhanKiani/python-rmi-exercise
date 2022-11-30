import sys

parent_module = sys.modules['.'.join(__name__.split('.')[:-1]) or '__main__']
if __name__ == '__main__' or parent_module.__name__ == '__main__':
    from server_registry.server_registry import ServerRegsitry
else:
    from .server_registry import ServerRegsitry

if __name__ == '__main__':
    registry = ServerRegsitry('localhost', 9090)
    registry.start()
    
    



    
