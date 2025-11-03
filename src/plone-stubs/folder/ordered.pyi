from _typeshed import Incomplete
from Products.BTreeFolder2.BTreeFolder2 import BTreeFolder2Base
from Products.CMFCore.PortalFolder import PortalFolderBase

HAS_WEBDAV: bool

class OrderedBTreeFolderBase(BTreeFolder2Base):
    """BTree folder base class with ordering support. The ordering
    is done by a named adapter (to IOrdering), which makes the policy
    changeable."""

    security: Incomplete
    def __bool__(self) -> bool:
        """a folder is something, even if it's empty"""
    def getOrdering(self):
        """return the currently active ordering adapter for this folder"""
    def setOrdering(self, ordering: str = "") -> None:
        """(re)set ordering adapter to be used for this folder"""
    def objectIds(self, spec=None, ordered: bool = True): ...
    def objectValues(self, spec=None): ...
    def objectItems(self, spec=None): ...
    def getObjectPosition(self, id):
        """Get the position of an object by its id."""
    def moveObjectsUp(self, ids, delta: int = 1, subset_ids=None):
        """Move specified sub-objects up by delta in container."""
    def moveObjectsDown(self, ids, delta: int = 1, subset_ids=None):
        """Move specified sub-objects down by delta in container."""
    def moveObjectsToTop(self, ids, subset_ids=None):
        """Move specified sub-objects to top of container."""
    def moveObjectsToBottom(self, ids, subset_ids=None):
        """Move specified sub-objects to bottom of container."""
    def moveObject(self, id, position):
        """Move specified object to absolute position."""
    def moveObjectToPosition(self, id, position, suppress_events: bool = False):
        """Move specified object to absolute position."""
    def moveObjectsByDelta(
        self, ids, delta, subset_ids=None, suppress_events: bool = False
    ):
        """Move specified sub-objects by delta."""
    def orderObjects(self, key=None, reverse=None):
        """Order sub-objects by key and direction."""
    def iterkeys(self): ...
    def manage_renameObject(self, id, new_id, REQUEST=None):
        """Rename a particular sub-object without changing its position."""
    def __setitem__(self, key, value) -> None: ...
    def __contains__(self, key) -> bool: ...
    def __delitem__(self, key) -> None: ...
    def __getitem__(self, key): ...
    __iter__ = iterkeys
    keys = objectIds
    values = objectValues
    items = objectItems

class CMFOrderedBTreeFolderBase(OrderedBTreeFolderBase, PortalFolderBase):
    """BTree folder for CMF sites, with ordering support. The ordering
    is done by adapter (to IOrdering), which makes the policy
    changeable."""
    def __init__(self, id, title: str = "") -> None: ...
