from _typeshed import Incomplete
from zope.publisher.browser import BrowserView

class RedirectToUUIDView(BrowserView):
    """A browser view that will cause a redirect to a given UUID,
    given via sub-path traversal.
    """

    uuid: Incomplete
    def publishTraverse(self, request, name): ...
    def __call__(self): ...
