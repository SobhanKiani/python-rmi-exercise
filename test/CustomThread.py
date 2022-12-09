from threading import Thread
from typing import Any, Callable, Iterable, Mapping


class CustomThread(Thread):

    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, Verbose=None):
        Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None

    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args,
                                        **self._kwargs)

    def join(self, *args):
        Thread.join(self, *args)
        return self._return


# def hanlder():
#     return 125


# t = CustomThread(target=hanlder)
# t.start()
# t.join()
# print(t._return)
