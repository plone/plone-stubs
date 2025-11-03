from .PortalFolder import PortalFolder
from .Skinnable import SkinnableObjectManager
from _typeshed import Incomplete

class PortalObjectBase(PortalFolder, SkinnableObjectManager):
    meta_type: str
    __getattr__: Incomplete
    __ac_permissions__: Incomplete
    def __init__(self, id, title: str = "", description: str = "") -> None: ...
    def __before_publishing_traverse__(self, arg1, arg2=None) -> None:
        """Pre-traversal hook."""
