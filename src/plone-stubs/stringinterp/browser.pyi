from _typeshed import Incomplete
from collections.abc import Generator
from Products.Five import BrowserView

def find_adapters(reg) -> Generator[Incomplete]: ...

class SubstitutionInfo(BrowserView):
    """
    Browser view support for listing IStringSubstitution
    adapters.
    """

    context: Incomplete
    request: Incomplete
    def __init__(self, context, request) -> None: ...
    def substitutionList(self):
        """
        returns sequence:
        [ {'category':categoryTitle,
           'items':[{'id':subId, 'description':subDescription}, ...]), ...  ]
        """
