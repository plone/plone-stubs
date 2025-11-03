from _typeshed import Incomplete
from collections.abc import Generator
from plone.app.linkintegrity.retriever import DXGeneral

class BlocksRetriever(DXGeneral):
    """General retriever for Blocks enabled contents."""
    def retrieveLinks(self):
        """Finds all links from the object and return them."""

class TextBlockLinksRetriever:
    order: int
    block_type: str
    context: Incomplete
    request: Incomplete
    def __init__(self, context, request) -> None: ...
    def __call__(self, block):
        """
        Returns a list of internal links
        """

class SlateBlockLinksRetriever:
    order: int
    block_type: str
    field: str
    context: Incomplete
    request: Incomplete
    links: Incomplete
    def __init__(self, context, request) -> None: ...
    def __call__(self, block): ...
    def handle_a(self, child): ...
    def handle_link(self, child): ...

class GenericBlockLinksRetriever:
    """Retrieves links from the url and href fields of any block"""

    order: int
    block_type: Incomplete
    context: Incomplete
    request: Incomplete
    def __init__(self, context, request) -> None: ...
    def __call__(self, block):
        """
        Returns a list of internal links
        """

def get_urls_from_value(value) -> Generator[Incomplete, Incomplete]:
    """Generator of urls from a block field value

    Recognizes:
    - strings containing "resolveuid"
    - objects with an @id property containing "resolveuid"
    - lists of either of the above
    """
