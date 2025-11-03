from _typeshed import Incomplete

class NestedBlockLinkRetriever:
    """Retrieve internal links from nested blocks.

    Handles the same keys as the resolveuid transform
    (columns, hrefList, and slides)
    """

    order: int
    block_type: Incomplete
    context: Incomplete
    request: Incomplete
    def __init__(self, context, request) -> None: ...
    def __call__(self, block): ...
    def retrieveLinks(self, block): ...
