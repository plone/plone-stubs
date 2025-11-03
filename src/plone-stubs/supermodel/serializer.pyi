from _typeshed import Incomplete

__all__ = ["serialize"]

class DefaultFieldNameExtractor:
    """Extract a name"""

    context: Incomplete
    def __init__(self, context) -> None: ...
    def __call__(self): ...

def serialize(model): ...
