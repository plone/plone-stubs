from _typeshed import Incomplete
from collections.abc import Generator

def iterDirectoriesOfType(
    type, filter_duplicates: bool = True
) -> Generator[Incomplete]:
    """
    Returns a generator which iterates over all resource directories of a
    particular resource type.

    If ``filter_duplicates`` is True and multiple resource directory trees
    contain resource directories with identical names, only the
    first one found will be returned for each name. The following sources are
    checked in order:
    - the persistent portal_resources tool
    - the global resource directory
    - resource directories in distributions
    """

def queryResourceDirectory(type, name):
    """Find the IResourceDirectory of the given name and type. Returns
    None if not found.
    """

def cloneResourceDirectory(source, target) -> None:
    """Copy all directories and files in the resource directory source to
    the writable resource directory target
    """
