from _typeshed import Incomplete
from zope.publisher.browser import BrowserView

def uuidToURL(uuid):
    """Resolves a UUID to a URL via the UID index of portal_catalog."""

def uuidToObject(uuid):
    """Resolves a UUID to an object via the Physical Path"""

def uuidFor(obj): ...

class ResolveUIDView(BrowserView):
    """Resolve a URL like /resolveuid/<uuid> to a normalized URL."""

    uuid: Incomplete
    subpath: Incomplete
    def publishTraverse(self, request, name): ...
    def __call__(self): ...
