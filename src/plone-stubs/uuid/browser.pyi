from zope.publisher.browser import BrowserView

class UUIDView(BrowserView):
    """A simple browser view that renders the UUID of its context"""
    def __call__(self): ...
