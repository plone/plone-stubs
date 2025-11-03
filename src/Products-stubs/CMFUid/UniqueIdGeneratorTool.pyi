from _typeshed import Incomplete
from OFS.SimpleItem import SimpleItem
from Products.CMFCore.utils import UniqueObject

class UniqueIdGeneratorTool(UniqueObject, SimpleItem):
    """Generator of unique ids.

    This is a dead simple implementation using a counter. May cause
    ConflictErrors under high load and the values are predictable.
    """

    id: str
    alternative_id: str
    meta_type: str
    security: Incomplete
    def __init__(self) -> None:
        """Initialize the generator"""
    def __call__(self):
        """See IUniqueIdGenerator."""
    def convert(self, uid):
        """See IUniqueIdGenerator."""
