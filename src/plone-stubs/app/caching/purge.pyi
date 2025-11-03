from _typeshed import Incomplete
from collections.abc import Generator

HAS_RESTAPI: bool
CONTENT_PATHS_POSTFIXES: Incomplete

class ContentPurgePaths:
    """Paths to purge for content items

    Includes:

    * ${object_path}/ (e.g. for folders)
    * ${object_path}/view
    * ${object_path}/${object_default_view}
    * a bunch of restapi endpoints

    If the object is the default view of its parent, also purge:

    * ${parent_path}
    * ${parent_path}/
    """

    context: Incomplete
    def __init__(self, context) -> None: ...
    def getRelativePaths(self): ...
    def getAbsolutePaths(self): ...

class DiscussionItemPurgePaths:
    """Paths to purge for Discussion Item.

    Looks up paths for the ultimate parent.
    """

    context: Incomplete
    def __init__(self, context) -> None: ...
    def getRelativePaths(self) -> Generator[Incomplete, Incomplete]: ...
    def getAbsolutePaths(self) -> Generator[Incomplete, Incomplete]: ...

class ScalesPurgePaths:
    """Paths to purge for Dexterity object fields"""

    context: Incomplete
    def __init__(self, context) -> None: ...
    def getScales(self): ...
    def getRelativePaths(self) -> Generator[Incomplete]: ...
    def getAbsolutePaths(self): ...

def purgeOnModified(object, event) -> None: ...
def purgeOnMoved(object, event) -> None:
    """Purge after object was moved."""

def purgeOnRemoved(object, event) -> None:
    """Purge after object was deleted."""

def purgeOnWorkflow(object, event) -> None: ...
