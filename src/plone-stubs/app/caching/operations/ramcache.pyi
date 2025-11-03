from _typeshed import Incomplete

GLOBAL_KEY: str

class Store:
    """Transform chain element which actually saves the page in RAM.

    This is registered for the ``IRAMCached`` request marker, which is set by
    the ``cacheInRAM()`` helper method. Thus, the transform is only used if
    the caching operation requested it.
    """

    order: int
    published: Incomplete
    request: Incomplete
    def __init__(self, published, request) -> None: ...
    def transformUnicode(self, result, encoding) -> None: ...
    def transformBytes(self, result, encoding) -> None: ...
    def transformIterable(self, result, encoding): ...
    def responseIsSuccess(self): ...
