from _typeshed import Incomplete

WARNING: int

class BrokenTransform:
    inputs: Incomplete
    output: str
    id: Incomplete
    module: Incomplete
    error: Incomplete
    def __init__(self, id, module, error) -> None: ...
    def name(self): ...
    def convert(self, orig, data, **kwargs): ...

def register() -> None: ...
