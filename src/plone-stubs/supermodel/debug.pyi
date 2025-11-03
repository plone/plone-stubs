from _typeshed import Incomplete

import threading

class SupermodelParseInfo(threading.local):
    stack: Incomplete
    def __getattr__(self, name): ...

parseinfo: Incomplete
