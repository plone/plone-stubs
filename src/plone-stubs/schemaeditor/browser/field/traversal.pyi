from _typeshed import Incomplete
from OFS.SimpleItem import SimpleItem

class FieldContext(SimpleItem):
    """wrapper for published zope 3 schema fields"""

    field: Incomplete
    request: Incomplete
    id: Incomplete
    def __init__(self, context, request) -> None: ...
    def publishTraverse(self, request, name):
        """It's not valid to traverse to anything below a field context."""
    def browserDefault(self, request):
        """Really we want to show the field EditView."""
