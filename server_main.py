import sys

parent_module = sys.modules['.'.join(__name__.split('.')[:-1]) or '__main__']
if __name__ == '__main__' or parent_module.__name__ == '__main__':
    from application.server_skeleton import ServerSkeleton
    from server_registry.server_registry import ServerRegsitry
else:
    from .application.server_skeleton import ServerSkeleton
    from .server_registry.server_registry import ServerRegsitry

if __name__ == '__main__':
    skeleton = ServerSkeleton('localhost', 9091)
    skeleton.start()
    



    
