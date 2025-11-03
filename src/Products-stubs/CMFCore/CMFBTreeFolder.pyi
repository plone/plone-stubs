from .PortalFolder import PortalFolderBase
from _typeshed import Incomplete
from Products.BTreeFolder2.BTreeFolder2 import BTreeFolder2Base

def manage_addCMFBTreeFolder(dispatcher, id, title: str = "", REQUEST=None) -> None:
    """Adds a new BTreeFolder object with id *id*."""

class CMFBTreeFolder(BTreeFolder2Base, PortalFolderBase):
    """BTree folder for CMF sites."""

    security: Incomplete
    def __init__(self, id, title: str = "") -> None: ...
    def manage_addPortalFolder(self, id, title: str = "", REQUEST=None):
        """Add a new PortalFolder object with id *id*."""

CMFBTreeFolderFactory: Incomplete
