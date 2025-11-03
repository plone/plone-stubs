from _typeshed import Incomplete
from collections.abc import Generator
from plone.supermodel.interfaces import FIELDSETS_KEY
from plone.supermodel.interfaces import PRIMARY_FIELDS_KEY

class DirectiveClass(type):
    """A Directive is used to apply tagged values to a Schema"""
    def __init__(self, name, bases, attrs) -> None: ...
    def __call__(self, *args, **kw) -> None: ...

Directive: Incomplete

class MetadataListDirective(Directive):
    """Store a list value in the tagged value under the key."""

    key: Incomplete
    def store(self, tags, value) -> None: ...

class MetadataDictDirective(Directive):
    """Store a dict value in the tagged value under the key."""

    key: Incomplete
    def store(self, tags, value) -> None: ...

class CheckerPlugin:
    key: Incomplete
    schema: Incomplete
    value: Incomplete
    def __init__(self, schema) -> None: ...
    def fieldNames(self) -> None: ...
    def check(self) -> Generator[Incomplete]: ...
    def __call__(self) -> None: ...

class DictCheckerPlugin(CheckerPlugin):
    def fieldNames(self): ...

class ListCheckerPlugin(CheckerPlugin):
    def fieldNames(self) -> Generator[Incomplete, Incomplete]: ...

class ListPositionCheckerPlugin(CheckerPlugin):
    position: Incomplete
    def fieldNames(self) -> Generator[Incomplete]: ...

class load(Directive):
    """Directive used to specify the XML model file"""
    def store(self, tags, value) -> None: ...
    def factory(self, filename, schema: str = ""): ...

class SupermodelSchemaPlugin:
    order: int
    interface: Incomplete
    def __init__(self, interface) -> None: ...
    def __call__(self) -> None: ...

class fieldset(MetadataListDirective):
    """Directive used to create fieldsets"""

    key = FIELDSETS_KEY
    def factory(
        self, name, label=None, description=None, fields=None, order=..., **kw
    ): ...

class FieldsetCheckerPlugin(CheckerPlugin):
    key = FIELDSETS_KEY
    def fieldNames(self) -> Generator[Incomplete, Incomplete]: ...

class primary(MetadataListDirective):
    """Directive used to mark one or more fields as 'primary'"""

    key = PRIMARY_FIELDS_KEY
    def factory(self, *args): ...

class PrimaryFieldsPlugin(ListCheckerPlugin):
    key = PRIMARY_FIELDS_KEY
    def __call__(self) -> None: ...
