from _typeshed import Incomplete
from plone.supermodel import model
from zope.interface import Invalid
from zope.interface import invariant

def default_language(context): ...

class IBasic(model.Schema):
    title: Incomplete
    description: Incomplete

class ICategorization(model.Schema):
    subjects: Incomplete
    language: Incomplete

class EffectiveAfterExpires(Invalid):
    __doc__: Incomplete

class IPublication(model.Schema):
    effective: Incomplete
    expires: Incomplete
    @invariant
    def validate_start_end(data) -> None: ...

class IOwnership(model.Schema):
    creators: Incomplete
    contributors: Incomplete
    rights: Incomplete

def creatorsDefault(data): ...

CreatorsDefaultValue: Incomplete

class IDublinCore(IOwnership, IPublication, ICategorization, IBasic):
    """Metadata behavior providing all the DC fields"""

class MetadataBase:
    """This adapter uses DCFieldProperty to store metadata directly on an
    object using the standard CMF DefaultDublinCoreImpl getters and
    setters.
    """

    context: Incomplete
    def __init__(self, context) -> None: ...

class DCFieldProperty:
    """Computed attributes based on schema fields.
    Based on zope.schema.fieldproperty.FieldProperty.
    """
    def __init__(self, field, get_name=None, set_name=None) -> None: ...
    def __get__(self, inst, klass): ...
    def __set__(self, inst, value) -> None: ...
    def __getattr__(self, name): ...

class Basic(MetadataBase):
    title: Incomplete
    description: Incomplete

class Categorization(MetadataBase):
    subjects: Incomplete
    language: Incomplete

class Publication(MetadataBase):
    effective: Incomplete
    expires: Incomplete

class Ownership(MetadataBase):
    creators: Incomplete
    contributors: Incomplete
    rights: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class DublinCore(Basic, Categorization, Publication, Ownership): ...
