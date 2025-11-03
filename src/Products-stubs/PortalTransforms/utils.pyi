from _typeshed import Incomplete

class TransformException(Exception): ...

FB_REGISTRY: Incomplete
logger: Incomplete

def log(message, severity=...) -> None: ...
def safeToInt(value):
    """Convert value to integer or just return 0 if we can't"""
