from .FSObject import FSObject
from _typeshed import Incomplete
from Products.ZSQLMethods.SQL import SQL

logger: Incomplete

class FSZSQLMethod(SQL, FSObject):
    """FSZSQLMethods act like Z SQL Methods but are not directly
    modifiable from the management interface."""

    meta_type: str
    manage_options: Incomplete
    security: Incomplete
    manage: Incomplete
    manage_customise: Incomplete
    def __init__(self, id, filepath, fullname=None, properties=None) -> None: ...
    def __of__(self, parent): ...
