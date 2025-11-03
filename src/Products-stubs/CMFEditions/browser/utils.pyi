from _typeshed import Incomplete
from Products.Five.browser import BrowserView

logger: Incomplete

class GetMacros(BrowserView):
    """Get macros.

    This is the former 'get_macros' python skin script.  It was moved
    to a browser view to avoid an Unauthorized exception when using
    five.pt.  Browser views are recommended anyway.
    """
    def get_macros(self, vdata): ...
