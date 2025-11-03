from _typeshed import Incomplete
from collections.abc import Generator

manage_CloneNamedFileBlobsAddForm: Incomplete

def getCallbacks(values):
    """Return persistent callbacks.

    Register the provided values in a mapping object and return a set
    of persistent callbacks that effectively replace the values with
    ``None``.
    """

def getFieldValues(obj, *ifaces) -> Generator[Incomplete]: ...
def manage_addCloneNamedFileBlobs(self, id, title=None, REQUEST=None) -> None:
    """Add a clone namedfile blobs modifier."""

manage_SkipRelationsAddForm: Incomplete

def manage_addSkipRelations(self, id, title=None, REQUEST=None) -> None:
    """Add a skip relations modifier."""

class CloneNamedFileBlobs:
    """Modifier to store an un-cloned reference to blobs.

    Without this, the Blob instance is cloned
    without also copying its connected file.

    (The name of the class is misleading; it remains for backwards
    compatibility with persistent objects but it's left over from
    a time when the implementation cloned the Blob. Now the whole
    point of this modifier is to avoid cloning the Blob,
    because it's unnecessary and slow.)
    """

    id: Incomplete
    title: Incomplete
    def __init__(self, id_, title) -> None: ...
    def getReferencedAttributes(self, obj): ...
    def reattachReferencedAttributes(self, obj, attrs_dict) -> None: ...
    def getOnCloneModifiers(self, obj):
        """Removes references to blobs in the cloned object."""

class SkipRelations:
    """Standard modifier to avoid cloning of relations and
    restore them from the working copy.
    """

    id: Incomplete
    title: Incomplete
    def __init__(self, id_, title) -> None: ...
    def getOnCloneModifiers(self, obj):
        """Removes relations."""
    def beforeSaveModifier(self, obj, clone):
        """Does nothing, the pickler does the work."""
    def afterRetrieveModifier(self, obj, repo_clone, preserve=()):
        """Restore relations from the working copy."""

modifiers: Incomplete
