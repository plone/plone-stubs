from _typeshed import Incomplete
from Acquisition import Implicit
from OFS.Folder import Folder
from OFS.ObjectManager import IFAwareObjectManager
from OFS.SimpleItem import SimpleItem
from Persistence import Persistent

class ZCatalogIndexes(IFAwareObjectManager, Folder, Persistent, Implicit):
    """A mapping object, responding to getattr requests by looking up
    the requested indexes in an object manager."""

    meta_type: str
    zmi_icon: str
    manage_options: Incomplete
    security: Incomplete
    addIndexForm: Incomplete
    def manage_main(self, REQUEST, RESPONSE) -> None:
        """Redirect to the parent where the management screen now lives"""
    manage_workspace = manage_main
    def manage_get_sortedObjects(self, sortkey, revkey):
        """We need to wrap the index objects because some of them
        can have security which does not work if they are unwrapped.
        This happened to ZCTextIndex objects in Plone."""
    def objectIds(self, spec=None): ...
    def __contains__(self, name) -> bool: ...
    def __bobo_traverse__(self, REQUEST, name): ...

class OldCatalogWrapperObject(SimpleItem, Implicit):
    manage_options: Incomplete
    manage_main: Incomplete
    manage_workspace = manage_main
    index: Incomplete
    def __init__(self, o) -> None: ...
