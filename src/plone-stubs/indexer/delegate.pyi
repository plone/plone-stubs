from _typeshed import Incomplete

class DelegatingIndexer:
    """An indexer that delegates to a given callable"""

    context: Incomplete
    catalog: Incomplete
    callable: Incomplete
    def __init__(self, context, catalog, callable) -> None: ...
    def __call__(self): ...

class DelegatingIndexerFactory:
    """An adapter factory for an IIndexer that works by calling a
    DelegatingIndexer.
    """

    callable: Incomplete
    __implemented__: Incomplete
    def __init__(self, callable) -> None: ...
    def __call__(self, object, catalog=None): ...
