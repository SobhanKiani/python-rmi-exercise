import sys

parent_module = sys.modules['.'.join(__name__.split('.')[:-1]) or '__main__']
if __name__ == '__main__' or parent_module.__name__ == '__main__':
    from server.server_skeleton import ServerSkeleton
    from server.server_impl import ServerImpl
    from registry.server_registry import ServerRegsitry
else:
    from .server.server_skeleton import ServerSkeleton
    from .server.server_impl import ServerImpl
    from .registry.server_registry import ServerRegsitry

if __name__ == '__main__':
    obj = ServerImpl()
    skeleton = ServerSkeleton('localhost', 9091, obj)
    skeleton.bind()
    



    
