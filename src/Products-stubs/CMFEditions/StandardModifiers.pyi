from _typeshed import Incomplete
from Products.CMFEditions.Modifiers import ConditionalTalesModifier

def initialize(context) -> None:
    """Registers modifiers with zope (on zope startup)."""

def install(portal_modifier, ids=None) -> None:
    """Registers modifiers in the modifier registry (at tool install time)."""

manage_OMOutsideChildrensModifierAddForm: Incomplete

def manage_addOMOutsideChildrensModifier(self, id, title=None, REQUEST=None) -> None:
    """Add an object manager modifier treating children as outside refs"""

manage_OMInsideChildrensModifierAddForm: Incomplete

def manage_addOMInsideChildrensModifier(self, id, title=None, REQUEST=None) -> None:
    """Add an object manager modifier treating children as inside refs"""

manage_RetainUIDsModifierAddForm: Incomplete

def manage_addRetainUIDs(self, id, title=None, REQUEST=None) -> None:
    """Add a modifier retaining UIDs upon retrieve."""

manage_RetainWorkflowStateAndHistoryModifierAddForm: Incomplete

def manage_addRetainWorkflowStateAndHistory(self, id, title=None, REQUEST=None) -> None:
    """Add a modifier retaining workflow state upon retrieve."""

manage_RetainPermissionsSettingsAddForm: Incomplete

def manage_addRetainPermissionsSettings(self, id, title=None, REQUEST=None) -> None:
    """Add a modifier retaining permissions upon retrieve."""

manage_SaveFileDataInFileTypeByReferenceModifierAddForm: Incomplete

def manage_addSaveFileDataInFileTypeByReference(
    self, id, title=None, REQUEST=None
) -> None:
    """Add a modifier avoiding unnecessary cloning of file data."""

manage_SillyDemoRetrieveModifierAddForm: Incomplete

def manage_addSillyDemoRetrieveModifier(self, id, title=None, REQUEST=None) -> None:
    """Add a silly demo retrieve modifier"""

manage_AbortVersioningOfLargeFilesAndImagesAddForm: Incomplete

def manage_addAbortVersioningOfLargeFilesAndImages(
    self, id, title=None, REQUEST=None
) -> None:
    """Add a silly demo retrieve modifier"""

manage_SkipVersioningOfLargeFilesAndImagesAddForm: Incomplete

def manage_addSkipVersioningOfLargeFilesAndImages(
    self, id, title=None, REQUEST=None
) -> None:
    """Add a silly demo retrieve modifier"""

manage_SkipParentPointersAddForm: Incomplete

def manage_addSkipParentPointers(self, id, title=None, REQUEST=None) -> None:
    """Add a skip parent pointers modifier"""

manage_SkipRegistryBasesPointersAddForm: Incomplete

def manage_addSkipRegistryBasesPointers(self, id, title=None, REQUEST=None) -> None:
    """Add a skip component registry bases modifier"""

manage_Skip_z3c_blobfileAddForm: Incomplete

def manage_addSkip_z3c_blobfile(self, id, title=None, REQUEST=None) -> None:
    """Add a skip z3c.blobfile modifier"""

class RetainAttributeAnnotationItemsBase:
    """Standard modifier retaining values of specific annotations from
    the working copy
    """

    PRESERVE_ANNOTATION_KEYS: Incomplete
    def afterRetrieveModifier(self, obj, repo_clone, preserve=()): ...

class OMBaseModifier(RetainAttributeAnnotationItemsBase):
    """Base class for ObjectManager modifiers."""

    PRESERVE_ANNOTATION_KEYS: Incomplete

class OMOutsideChildrensModifier(OMBaseModifier):
    """ObjectManager modifier treating all children as outside refs

    Treats all children as outside references (the repository layer
    knows what to do with that fact).
    """
    def getOnCloneModifiers(self, obj):
        """Removes all children and returns them as references."""
    def beforeSaveModifier(self, obj, clone):
        """Returns all uninitialized 'IVersionAwareReference' objects.

        This always goes in conjunction with 'getOnCloneModifiers'.
        """
    def afterRetrieveModifier(self, obj, repo_clone, preserve=()): ...

class OMInsideChildrensModifier(OMBaseModifier):
    """ObjectManager modifier treating all children as inside refs

    Treats all children as inside references (the repository layer
    knows what to do with that fact).
    """
    def getOnCloneModifiers(self, obj):
        """Removes all children and returns them as references."""
    def beforeSaveModifier(self, obj, clone):
        """Returns all uninitialized 'IVersionAwareReference' objects.

        This always goes in conjunction with 'getOnCloneModifiers'.
        """
    def afterRetrieveModifier(self, obj, repo_clone, preserve=()): ...

class OMSubObjectAdapter:
    """Adapter to an object manager children."""
    def __init__(self, obj, name) -> None:
        """Initialize the adapter."""
    def save(self, dict) -> None:
        """See interface"""
    def remove(self, permanent: bool = False) -> None:
        """See interface"""

class RetainWorkflowStateAndHistory:
    """Standard modifier retaining the working copies workflow state

    Avoids the objects workflow state from being retrieved also.
    """
    def beforeSaveModifier(self, obj, clone): ...
    def afterRetrieveModifier(self, obj, repo_clone, preserve=()): ...

class RetainPermissionsSettings:
    """Standard modifier retaining permissions settings

    This is nearly essential if we are going to be retaining workflow.
    """
    def beforeSaveModifier(self, obj, clone): ...
    def afterRetrieveModifier(self, obj, repo_clone, preserve=()): ...

class RetainUIDs:
    """Modifier which ensures uid consistency by retaining the uid from the working copy.  Ensuring
    that newly created objects are assigned an appropriate uid is a job for the repository tool.
    """
    def beforeSaveModifier(self, obj, clone): ...
    def afterRetrieveModifier(self, obj, repo_clone, preserve=()): ...

class SaveFileDataInFileTypeByReference:
    """Standard modifier avoiding unnecessary cloning of the file data.

    Called on 'Portal File' objects.
    """
    def getReferencedAttributes(self, obj): ...
    def reattachReferencedAttributes(self, obj, attrs_dict) -> None: ...

class SkipParentPointers:
    """Standard modifier to avoid cloning of __parent__ pointers and
    restore them from context
    """
    def getOnCloneModifiers(self, obj):
        """Removes parent pointers and stores a marker"""
    def beforeSaveModifier(self, obj, clone):
        """Does nothing, the pickler does the work"""
    def afterRetrieveModifier(self, obj, repo_clone, preserve=()):
        """Install the parent from the working copy"""

class SkipRegistryBasesPointers:
    """Standard modifier to avoid cloning of component registry
    __bases__ and restore them from context
    """
    def querySiteManager(self, obj): ...
    def getOnCloneModifiers(self, obj):
        """Removes component registry bases pointers and stores a marker"""
    def beforeSaveModifier(self, obj, clone):
        """Don't save the bases."""
    def afterRetrieveModifier(self, obj, repo_clone, preserve=()):
        """Does nothing, the pickler does the work"""

class SillyDemoRetrieveModifier:
    """Silly Retrieve Modifier for Demos

    Disabled by default and if enabled only effective if the
    username is ``gregweb``.

    This is really just as silly example though for demo purposes!!!
    """
    def beforeSaveModifier(self, obj, clone): ...
    def afterRetrieveModifier(self, obj, repo_clone, preserve=()): ...

class AbortVersioningOfLargeFilesAndImages(ConditionalTalesModifier):
    """Raises an error if a file or image attribute stored on the
    object in a specified field is larger than a fixed default"""

    field_names: Incomplete
    max_size: int
    modifierEditForm: Incomplete
    id: Incomplete
    title: Incomplete
    meta_type: Incomplete
    def __init__(
        self,
        id: str = "AbortVersioningOfLargeFilesAndImages",
        modifier=None,
        title: str = "",
    ) -> None: ...
    def edit(
        self,
        enabled=None,
        condition=None,
        title: str = "",
        field_names=None,
        max_size=None,
        REQUEST=None,
    ):
        """See IConditionalTalesModifier."""
    def getFieldNames(self):
        """For the edit form"""
    def getModifier(self):
        """We are the modifier, not some silly wrapper."""
    def getOnCloneModifiers(self, obj) -> None:
        """Detects large file objects and raises an error"""

class LargeFilePlaceHolder:
    """PlaceHolder for a large object"""
    @staticmethod
    def getSize(): ...

class SkipVersioningOfLargeFilesAndImages(AbortVersioningOfLargeFilesAndImages):
    """Replaces any excessively large file and images stored as
    annotations or attributes on the object with a marker.  On
    retrieve, the marker will be replaced with the current value.."""
    def getOnCloneModifiers(self, obj):
        """Removes large file objects and returns them as references"""
    def beforeSaveModifier(self, obj, clone):
        """Does nothing, the pickler does the work"""
    def afterRetrieveModifier(self, obj, repo_clone, preserve=()):
        """If we find any LargeFilePlaceHolders, replace them with the
        values from the current working copy.  If the values are missing
        from the working copy, remove them from the retrieved object."""

class Skip_z3c_blobfile:
    """Standard avoid storing blob data, may be useful for extremely
    large files where versioning the non-file metadata is important but
    the cost of versioning the file data is too high.
    """
    def getOnCloneModifiers(self, obj):
        """Removes z3c.blobfile fields"""
    def beforeSaveModifier(self, obj, clone): ...
    def afterRetrieveModifier(self, obj, repo_clone, preserve=()): ...

modifiers: Incomplete
