from _typeshed import Incomplete
from Products.Five import BrowserView

class GlobalStatusMessage(BrowserView):
    """Display messages to the current user"""

    index: Incomplete
    def __call__(self): ...
    @property
    def macros(self): ...
