from _typeshed import Incomplete

DEFAULT_STX_LEVEL: int
STX_LEVEL = DEFAULT_STX_LEVEL

class st:
    inputs: Incomplete
    output: str
    def name(self): ...
    def convert(self, orig, data, level=None, **kwargs): ...

def register(): ...
