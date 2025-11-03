from _typeshed import Incomplete
from Acquisition import Implicit
from OFS.PropertyManager import PropertyManager
from OFS.SimpleItem import SimpleItem
from Persistence import Persistent
from Products.CMFCore.utils import UniqueObject

class UniqueIdAnnotation(Persistent, Implicit):
    """Unique id object used as annotation on (content) objects."""

    id: Incomplete
    def __init__(self, obj, id) -> None:
        """See IUniqueIdAnnotation."""
    def __call__(self):
        """See IUniqueIdAnnotation."""
    def getId(self):
        """See IUniqueIdAnnotation."""
    def setUid(self, uid) -> None:
        """See IUniqueIdAnnotation."""

def handleUidAnnotationEvent(ob, event) -> None:
    """Event subscriber for (IContentish, IObjectEvent) events"""

class UniqueIdAnnotationTool(UniqueObject, SimpleItem, PropertyManager):
    __doc__ = __doc__
    manage_options: Incomplete
    id: str
    alternative_id: str
    meta_type: str
    security: Incomplete
    remove_on_add: bool
    remove_on_clone: bool
    assign_on_add: bool
    assign_on_clone: bool
    def __call__(self, obj, id):
        """See IUniqueIdAnnotationManagement."""
