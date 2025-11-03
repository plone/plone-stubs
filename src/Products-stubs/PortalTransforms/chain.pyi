from _typeshed import Incomplete
from Acquisition import Implicit
from collections import UserList
from OFS.role import RoleManager
from OFS.SimpleItem import Item
from Persistence import Persistent

class chain(UserList):
    """A chain of transforms used to transform data"""
    def __init__(self, name: str = "", *args) -> None: ...
    def name(self): ...
    def registerTransform(self, transform) -> None: ...
    def unregisterTransform(self, name) -> None: ...
    def convert(self, orig, data, **kwargs): ...
    def __setitem__(self, key, value) -> None: ...
    def append(self, value) -> None: ...
    def insert(self, *args) -> None: ...
    def remove(self, *args) -> None: ...
    def pop(self, *args) -> None: ...

class TransformsChain(Implicit, Item, RoleManager, Persistent):
    """a transforms chain is suite of transforms to apply in order.
    It follows the transform API so that a chain is itself a transform.
    """

    module: str
    meta_type: str
    meta_types: Incomplete
    all_meta_types: Incomplete
    manage_options: Incomplete
    manage_main: Incomplete
    manage_reloadTransform: Incomplete
    security: Incomplete
    id: Incomplete
    description: Incomplete
    inputs: Incomplete
    output: str
    def __init__(self, id, description, ids=()) -> None: ...
    @security.public
    def convert(self, *args, **kwargs):
        """return apply the transform and return the result"""
    @security.public
    def name(self):
        """return the name of the transform instance"""
    @security.private
    def manage_beforeDelete(self, item, container) -> None: ...
    def manage_addObject(self, id, REQUEST=None) -> None:
        """add a new transform or chain to the chain"""
    def manage_delObjects(self, ids, REQUEST=None) -> None:
        """delete the selected mime types"""
    def move_object_to_position(self, id, newpos):
        """Overridden from OrderedFolder to store id instead of objects"""
    def move_object_up(self, id, REQUEST=None) -> None:
        """move object with the given id up in the list"""
    def move_object_down(self, id, REQUEST=None) -> None:
        """move object with the given id down in the list"""
    def reload(self) -> None:
        """reload the module where the transformation class is defined"""
    def listAddableObjectIds(self):
        """return a list of addable transform"""
    def objectIds(self):
        """return a list of addable transform"""
    def objectValues(self):
        """return a list of addable transform"""
