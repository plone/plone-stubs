from _typeshed import Incomplete
from zope.publisher import browser

class BrowserView(browser.BrowserView):
    context: Incomplete
    request: Incomplete
    def __init__(self, context, request) -> None: ...
    __parent__: Incomplete
