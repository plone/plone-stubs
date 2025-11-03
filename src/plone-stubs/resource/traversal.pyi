from _typeshed import Incomplete
from zope.traversing.namespace import SimpleHandler

class ResourceTraverser(SimpleHandler):
    name: Incomplete
    context: Incomplete
    def __init__(self, context, request=None) -> None: ...
    def traverse(self, name, remaining): ...

class UniqueResourceTraverser(SimpleHandler):
    """A traverser to allow unique URLs for caching"""

    context: Incomplete
    request: Incomplete
    def __init__(self, context, request) -> None: ...
    def traverse(self, name, remaining): ...
