from _typeshed import Incomplete

class DefaultRewriter:
    """Default rewriter, which is aware of virtual hosting"""

    request: Incomplete
    def __init__(self, request) -> None: ...
    def __call__(self, path): ...
