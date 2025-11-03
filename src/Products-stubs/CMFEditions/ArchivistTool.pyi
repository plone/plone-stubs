from _typeshed import Incomplete
from OFS.SimpleItem import SimpleItem
from Persistence import Persistent
from Products.CMFCore.utils import UniqueObject

RETRIEVING_UNREGISTERED_FAILED: str

def deepcopy(obj):
    """Makes a deep copy of the object using the pickle mechanism."""

class VersionData:
    """ """

    data: Incomplete
    refs_to_be_deleted: Incomplete
    attr_handling_references: Incomplete
    preserved_data: Incomplete
    sys_metadata: Incomplete
    app_metadata: Incomplete
    def __init__(
        self,
        data,
        refs_to_be_deleted,
        attr_handling_references,
        preserved_data,
        metadata,
    ) -> None: ...

class AttributeAdapter(Persistent):
    def __init__(self, parent, attr_name, type=None) -> None: ...
    def setAttribute(self, obj) -> None: ...
    def getAttribute(self, alternate=None): ...
    def getAttributeName(self): ...
    def getType(self): ...

class ObjectManagerStorageAdapter(Persistent):
    def __init__(self, parent, attr_name, type=None) -> None: ...
    def setAttribute(self, obj) -> None: ...
    def getAttribute(self, alternate=None): ...
    def getAttributeName(self): ...
    def getType(self): ...

class VersionAwareReference(Persistent):
    """A Reference that is version aware (and in future also location aware)."""

    history_id: Incomplete
    version_id: Incomplete
    location_id: Incomplete
    info: Incomplete
    def __init__(self, **info) -> None: ...
    def setReference(self, target_obj, remove_info: bool = True) -> None:
        """See IVersionAwareReference"""
    def __of__(self, obj):
        """Fake some acquisition stuff that may be needed in retrieval"""

class ArchivistTool(UniqueObject, SimpleItem):
    """ """

    id: str
    alternative_id: str
    meta_type: str
    interfaces: Incomplete
    exceptions: Incomplete
    classes: Incomplete
    security: Incomplete
    def prepare(self, obj, app_metadata=None, sys_metadata={}):
        """See IArchivist."""
    def register(self, prepared_obj):
        """See IArchivist."""
    def save(self, prepared_obj, autoregister=None):
        """See IArchivist."""
    def purge(
        self,
        obj=None,
        history_id=None,
        selector=None,
        metadata={},
        countPurged: bool = True,
    ) -> None:
        """See IPurgeSupport."""
    def retrieve(
        self,
        obj=None,
        history_id=None,
        selector=None,
        preserve=(),
        countPurged: bool = True,
    ):
        """See IPurgeSupport."""
    def getHistory(
        self, obj=None, history_id=None, preserve=(), countPurged: bool = True
    ):
        """See IPurgeSupport."""
    def getHistoryMetadata(self, obj=None, history_id=None):
        """Return the metadata blob for presenting summary
        information, etc. If obj is not supplied, history is found
        by history_id, if history_id is not supplied, history is
        found by obj. If neither, return None.
        """
    def queryHistory(
        self,
        obj=None,
        history_id=None,
        preserve=(),
        default=None,
        countPurged: bool = True,
    ):
        """See IPurgeSupport."""
    def isUpToDate(
        self, obj=None, history_id=None, selector=None, countPurged: bool = True
    ):
        """See IPurgeSupport."""

def getUserId(): ...

class ObjectData(Persistent):
    """ """

    object: Incomplete
    inside_refs: Incomplete
    outside_refs: Incomplete
    def __init__(self, obj, inside_refs=(), outside_refs=()) -> None: ...

class PreparedObject:
    """ """

    history_id: Incomplete
    original: Incomplete
    clone: Incomplete
    referenced_data: Incomplete
    metadata: Incomplete
    is_registered: Incomplete
    def __init__(
        self,
        history_id,
        original,
        clone,
        referenced_data,
        app_metadata,
        sys_metadata,
        is_registered,
        approxSize,
    ) -> None: ...
    def copyVersionIdFromClone(self) -> None: ...

class LazyHistory:
    """Lazy history."""
    def __init__(self, archivist, obj, history_id, preserve, countPurged) -> None:
        """Sets up a lazy history.

        Takes an object which should be the original object in the portal,
        and a history_id for the storage lookup. If the history id is
        omitted then the history_id will be determined by dereferencing
        the obj. If the obj is omitted, then the obj will be obtained by
        dereferencing the history_id.
        """
    def __len__(self) -> int:
        """See IHistory"""
    def __getitem__(self, selector):
        """See IHistory"""
    def __iter__(self):
        """See IHistory."""

class GetItemIterator:
    """Iterator object using a getitem implementation to iterate over."""

    next: Incomplete
    def __init__(self, getItem, stopExceptions) -> None: ...
    def __iter__(self): ...
    def __next__(self): ...

def object_copied(obj, event) -> None: ...
