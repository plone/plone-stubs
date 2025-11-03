from _typeshed import Incomplete

class QueuePurge:
    """Manually initiate a purge"""

    context: Incomplete
    request: Incomplete
    def __init__(self, context, request) -> None: ...
    def __call__(self): ...

class PurgeImmediately:
    """Purge immediately"""

    context: Incomplete
    request: Incomplete
    def __init__(self, context, request) -> None: ...
    def write(self, msg) -> None: ...
    def __call__(self): ...
