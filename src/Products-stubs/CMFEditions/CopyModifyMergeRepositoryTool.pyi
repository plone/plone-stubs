from _typeshed import Incomplete
from OFS.SimpleItem import SimpleItem
from Products.CMFCore.utils import UniqueObject

logger: Incomplete
VERSIONABLE_CONTENT_TYPES: Incomplete
VERSION_POLICY_MAPPING: Incomplete
VERSION_POLICY_DEFS: Incomplete
HOOKS: Incomplete

class CopyModifyMergeRepositoryTool(UniqueObject, SimpleItem):
    """See ICopyModifyMergeRepository"""

    id: str
    alternative_id: str
    meta_type: str
    autoapply: bool
    security: Incomplete
    manage_options: Incomplete
    @security.public
    def isVersionable(self, obj):
        """See interface."""
    @security.public
    def getVersionableContentTypes(self): ...
    def setVersionableContentTypes(self, new_content_types) -> None: ...
    setVersionableContentType = setVersionableContentTypes
    def addPolicyForContentType(self, content_type, policy_id, **kw) -> None: ...
    def removePolicyFromContentType(self, content_type, policy_id, **kw) -> None: ...
    @security.public
    def supportsPolicy(self, obj, policy): ...
    @security.public
    def hasPolicy(self, obj): ...
    def manage_setTypePolicies(self, policy_map, **kw) -> None: ...
    @security.public
    def listPolicies(self): ...
    def addPolicy(self, policy_id, policy_title, policy_class=..., **kw) -> None: ...
    def removePolicy(self, policy_id, **kw) -> None: ...
    def manage_changePolicyDefs(self, policy_list, **kwargs) -> None: ...
    def getPolicyMap(self): ...
    def setAutoApplyMode(self, autoapply) -> None:
        """See ICopyModifyMergeRepository."""
    @security.public
    def applyVersionControl(self, obj, comment: str = "", metadata={}) -> None:
        """See ICopyModifyMergeRepository."""
    @security.public
    def save(self, obj, comment: str = "", metadata={}) -> None:
        """See ICopyModifyMergeRepository."""
    @security.public
    def purge(
        self, obj, selector, comment: str = "", metadata={}, countPurged: bool = True
    ) -> None:
        """See IPurgeSupport."""
    @security.public
    def revert(self, obj, selector=None, countPurged: bool = True) -> None:
        """See IPurgeSupport."""
    @security.public
    def retrieve(self, obj, selector=None, preserve=(), countPurged: bool = True):
        """See IPurgeSupport."""
    @security.public
    def restore(
        self, history_id, selector, container, new_id=None, countPurged: bool = True
    ) -> None:
        """See IPurgeSupport."""
    @security.public
    def getHistory(
        self, obj, oldestFirst: bool = False, preserve=(), countPurged: bool = True
    ):
        """See IPurgeSupport."""
    @security.public
    def getHistoryMetadata(self, obj):
        """Returns the versioning metadata history."""
    @security.public
    def isUpToDate(self, obj, selector=None, countPurged: bool = True):
        """See IPurgeSupport."""

class VersionData:
    """ """

    security: Incomplete
    __allow_access_to_unprotected_subobjects__: int
    object: Incomplete
    preserved_data: Incomplete
    comment: Incomplete
    metadata: Incomplete
    sys_metadata: Incomplete
    version_id: Incomplete
    def __init__(self, object, preserved_data, sys_metadata, app_metadata) -> None: ...

class LazyHistory:
    """Lazy history."""

    __allow_access_to_unprotected_subobjects__: int
    def __init__(self, repository, obj, oldestFirst, preserve, countPurged) -> None: ...
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
