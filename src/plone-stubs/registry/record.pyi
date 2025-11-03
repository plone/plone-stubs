from _typeshed import Incomplete
from persistent import Persistent

class Record(Persistent):
    """A record that is stored in the registry.

    If __parent__ is set, consider this a "bound" record. In this case, the
    field and value are read from and written to the parent registry.

    BBB: The current storage implementation does not actually store Record
    objects directly. However, we keep the Persistent base class so that old
    values may be loaded during automated migration.
    """

    __parent__: Incomplete
    def __init__(self, field, value=..., _validate: bool = True) -> None: ...
    field: Incomplete
    value: Incomplete
    @property
    def interfaceName(self): ...
    @property
    def fieldName(self): ...
    @property
    def interface(self): ...
