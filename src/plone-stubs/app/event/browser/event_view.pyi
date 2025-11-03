from _typeshed import Incomplete
from Products.Five.browser import BrowserView

class EventView(BrowserView):
    context: Incomplete
    request: Incomplete
    data: Incomplete
    def __init__(self, context, request) -> None: ...
    def __call__(self): ...
