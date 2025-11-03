from _typeshed import Incomplete

class DXGeneral:
    """General retriever for DX that extracts URLs from (rich) text fields."""

    context: Incomplete
    def __init__(self, context) -> None: ...
    def retrieveLinks(self):
        """Finds all links from the object and return them."""
