from _typeshed import Incomplete
from zope.interface.interface import InterfaceClass

logger: Incomplete

class Fieldset:
    label: Incomplete
    description: Incomplete
    order: Incomplete
    fields: Incomplete
    def __init__(
        self, __name__, label=None, description=None, fields=None, order=...
    ) -> None: ...

class Model:
    schemata: Incomplete
    def __init__(self, schemata=None) -> None: ...
    @property
    def schema(self): ...

class SchemaClass(InterfaceClass):
    def __init__(
        self, name, bases=(), attrs=None, __doc__=None, __module__=None
    ) -> None: ...

Schema: Incomplete

def finalizeSchemas(parent=...) -> None:
    """Configuration action called after plone.supermodel is configured."""
