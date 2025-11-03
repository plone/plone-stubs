from _typeshed import Incomplete
from OFS.SimpleItem import SimpleItem
from Persistence import Persistent
from Products.CMFCore.utils import UniqueObject
from Products.CMFEditions.interfaces.IStorage import StorageError
from Products.CMFEditions.interfaces.IStorage import StorageRetrieveError

__version__: str
logger: Incomplete

def deepCopy(obj): ...
def getSize(obj):
    """Calculate the size as cheap as possible"""

class ZVCStorageTool(UniqueObject, SimpleItem):
    """Zope Version Control Based Version Storage

    There exist two selector schemas:

    - the one that counts removed versions also
    - the one that counts non removed version only

    Intended Usage:

    For different use cases different numbering schemas are used:

    - When iterating over the history the removed versions (usually)
      aren't of interest. Thus the next valid version may be accessed
      by incrementing the selector and vice versa.
    - When retrieving a version being able to access removed version
      or correctly spoken a substitute (pretending to be the removed
      version) is important when reconstructing relations between
      objects.
    """

    id: str
    alternative_id: str
    meta_type: str
    storageStatistics: Incomplete
    manage_options: Incomplete
    StorageError = StorageError
    StorageRetrieveError = StorageRetrieveError
    zvc_repo: Incomplete
    security: Incomplete
    def isRegistered(self, history_id):
        """See IStorage."""
    def register(self, history_id, object, referenced_data={}, metadata=None):
        """See IStorage."""
    def save(self, history_id, object, referenced_data={}, metadata=None):
        """See IStorage."""
    def retrieve(
        self,
        history_id,
        selector=None,
        countPurged: bool = True,
        substitute: bool = True,
    ):
        """See ``IStorage`` and Comments in ``IPurgePolicy``"""
    def getHistory(self, history_id, countPurged: bool = True, substitute: bool = True):
        """See IStorage."""
    def getModificationDate(
        self,
        history_id,
        selector=None,
        countPurged: bool = True,
        substitute: bool = True,
    ):
        """See IStorage."""
    def purge(
        self, history_id, selector, metadata={}, countPurged: bool = True
    ) -> None:
        """See ``IPurgeSupport``"""
    def getHistoryMetadata(self, history_id):
        """Return the metadata blob from ShadowHistory for presenting
        summary information, etc.
        """
    def zmi_getStorageStatistics(self):
        """ """

class ShadowStorage(Persistent):
    """Container for Shadow Histories

    Only cares about containerish operations.
    """
    def __init__(self) -> None: ...
    def isRegistered(self, history_id):
        """Returns True if a History With the Given History id Exists"""
    def getHistory(self, history_id, autoAdd: bool = False):
        """Returns the History Object of the Given ``history_id``.

        Returns None if ``autoAdd`` is False and the history
        does not exist. Else prepares and returns an empty history.
        """

class ShadowHistory(Persistent):
    """Purge Aware History for Storage Related Metadata"""

    security: Incomplete
    nextVersionId: int
    def __init__(self) -> None: ...
    def save(self, data):
        """Saves data in the history

        Returns the version id of the saved version.
        """
    def retrieve(self, selector, countPurged: bool = True):
        """Retrieves the Selected Data From the History

        The caller has to make a copy if he passed the data to another
        caller.

        Returns None if the selected version does not exist.
        """
    def purge(self, selector, data, countPurged) -> None:
        """Purge selected version from the history"""
    def getLength(self, countPurged):
        """Length of the History Either Counting Purged Versions or Not"""
    def __len__(self) -> int: ...
    def getSize(self):
        """Returns the size including the quality of the size"""
    def getVersionId(self, selector, countPurged):
        """Returns the Effective Version id depending the selector type

        Returns ``None`` if the selected version does not exist.
        """

class ZVCAwareWrapper(Persistent):
    """ZVC assumes the stored object has a getPhysicalPath method.

    ZVC, arghh ...
    """

    __vc_info__: Incomplete
    def __init__(self, object, metadata, vc_info=None) -> None: ...
    def getWrappedObject(self): ...
    def getPhysicalPath(self): ...

class Removed(Persistent):
    """Indicates that removement of data"""

    reason: Incomplete
    metadata: Incomplete
    def __init__(self, reason, metadata) -> None:
        """Store Removed Info"""

class VersionData:
    object: Incomplete
    referenced_data: Incomplete
    metadata: Incomplete
    def __init__(self, object, referenced_data, metadata) -> None: ...
    def isValid(self):
        """Returns True if Valid (not Purged)"""

class LazyHistory:
    """Lazy history adapter."""
    def __init__(
        self, storage, history_id, countPurged: bool = True, substitute: bool = True
    ) -> None:
        """See IHistory."""
    def __len__(self) -> int:
        """See IHistory."""
    def __getitem__(self, selector):
        """See IHistory."""
    def __iter__(self):
        """See IHistory."""

class GetItemIterator:
    """Iterator object using a getitem implementation to iterate over."""

    next: Incomplete
    def __init__(self, getItem, stopExceptions) -> None: ...
    def __iter__(self): ...
    def __next__(self): ...
