from _typeshed import Incomplete

class HomeFolderLocator:
    """Locate the current user's home folder, if possible."""

    context: Incomplete
    def __init__(self, context) -> None: ...
    title: Incomplete
    @property
    def available(self): ...
    def __call__(self): ...

class ParentFolderLocator:
    """Locate the parent of the context, if the user has the
    Add portal content permission.
    """

    context: Incomplete
    def __init__(self, context) -> None: ...
    title: Incomplete
    @property
    def available(self): ...
    def __call__(self): ...
