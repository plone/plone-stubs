from _typeshed import Incomplete
from OFS.Folder import Folder
from Persistence import Persistent

LOG: Incomplete
manage_addBTreeFolderForm: Incomplete

def manage_addBTreeFolder(dispatcher, id, title: str = "", REQUEST=None):
    """Adds a new BTreeFolder object with id *id*."""

listtext0: str
listtext1: str
listtext2: str
MAX_UNIQUEID_ATTEMPTS: int

class ExhaustedUniqueIdsError(Exception): ...

class BTreeFolder2Base(Persistent):
    """Base for BTree-based folders."""

    security: Incomplete
    manage_options: Incomplete
    manage_main: Incomplete
    title: str
    id: Incomplete
    def __init__(self, id=None) -> None: ...
    def manage_fixCount(self):
        """Call self._fixCount() and reports the result as text."""
    def manage_cleanup(self):
        """Call self._cleanup() and reports the result as text."""
    def get(self, name, default=None): ...
    def __getitem__(self, name): ...
    def __getattr__(self, name): ...
    def getBatchObjectListing(self, REQUEST=None):
        """Return a structure for a page template to show the list of objects."""
    def manage_object_workspace(self, ids=(), REQUEST=None):
        """Redirect to the workspace of the first object in the list."""
    def manage_delAllObjects(self, REQUEST=None):
        """Delete all contained objects."""
    def tpValues(self):
        """Ensure the items don't show up in the left pane."""
    def objectCount(self):
        """Return the number of items in the folder."""
    def __len__(self) -> int: ...
    def __nonzero__(self): ...
    def has_key(self, id):
        """Indicate whether the folder has an item by ID."""
    hasObject = has_key
    def objectIds(self, spec=None): ...
    def __contains__(self, name) -> bool: ...
    def __iter__(self): ...
    def objectValues(self, spec=None): ...
    def objectItems(self, spec=None): ...
    keys = objectIds
    values = objectValues
    items = objectItems
    def objectMap(self): ...
    def objectIds_d(self, t=None): ...
    def objectMap_d(self, t=None): ...
    def __setitem__(self, key, value) -> None: ...
    def __delitem__(self, name) -> None: ...
    def generateId(
        self, prefix: str = "item", suffix: str = "", rand_ceiling: int = 999999999
    ):
        """Returns an ID not used yet by this folder.

        The ID is unlikely to collide with other threads and clients.
        The IDs are sequential to optimize access to objects
        that are likely to have some relation.
        """

class BTreeFolder2(BTreeFolder2Base, Folder):
    """BTreeFolder2 based on OFS.Folder."""

    meta_type: str
    zmi_icon: str
