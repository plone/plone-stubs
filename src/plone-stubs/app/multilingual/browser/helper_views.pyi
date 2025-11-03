from _typeshed import Incomplete
from Products.Five import BrowserView

class universal_link(BrowserView):
    """Redirects the user to the negotiated translated page
    based on the user preferences in the user's browser.
    """

    tg: Incomplete
    lang: Incomplete
    def __init__(self, context, request) -> None: ...
    def publishTraverse(self, request, name): ...
    def getDestination(self): ...
    def __call__(self) -> None: ...

class selector_view(universal_link):
    def getDialogDestination(self):
        """Get the "not translated yet" dialog URL.
        It\'s located on the root and shows the translated objects of that TG
        """
    def getParentChain(self, context): ...
    def getClosestDestination(self):
        """Get the "closest translated object" URL."""
    def wrapDestination(self, url, postpath: bool = True):
        """Fix the translation url appending the query
        and the eventual append path.
        """
    def __call__(self) -> None: ...

class not_translated_yet(BrowserView):
    """View to inform user that the view requested is not translated yet,
    and shows the already translated related content.
    """

    __call__: Incomplete
    tg: Incomplete
    def __init__(self, context, request) -> None: ...
    def publishTraverse(self, request, name): ...
    def already_translated(self): ...
    def has_any_translation(self): ...
    def language_name(self, lang=None):
        """Get the current language native name"""

class TGView(BrowserView):
    """A simple browser view that renders the TG of its context"""
    def __call__(self): ...
