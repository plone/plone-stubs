from _typeshed import Incomplete

log: Incomplete

class LazyCatalogResultSerializer:
    """Serializes a ZCatalog resultset (one of the subclasses of `Lazy`) to
    a Python data structure that can in turn be serialized to JSON.
    """

    lazy_resultset: Incomplete
    request: Incomplete
    def __init__(self, lazy_resultset, request) -> None: ...
    def __call__(self, fullobjects: bool = False): ...
