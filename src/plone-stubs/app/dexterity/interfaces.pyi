from _typeshed import Incomplete
from z3c.form import validator
from zope import schema
from zope.filerepresentation.interfaces import IFileFactory
from zope.interface import Interface
from zope.publisher.interfaces.browser import IBrowserPage

class ITypesContext(IBrowserPage):
    """A non-persistent traversable item corresponding to a Dexterity FTI"""

class ITypeSchemaContext(Interface):
    """Marker interface for plone.schemaeditor schema contexts that are
    associated with a Dexterity FTI"""

    fti: Incomplete
    schemaName: Incomplete

class InvalidIdError(schema.ValidationError):
    __doc__: Incomplete

ID_RE: Incomplete

def isValidId(value): ...

class ITypeSettings(Interface):
    """Define the fields for the content type add form"""

    title: Incomplete
    id: Incomplete
    description: Incomplete
    container: Incomplete
    filter_content_types: Incomplete
    allowed_content_types: Incomplete

class ITypeStats(Interface):
    item_count: Incomplete

class TypeIdValidator(validator.SimpleFieldValidator):
    def validate(self, value) -> None: ...

class TypeTitleValidator(validator.SimpleFieldValidator):
    def validate(self, value) -> None: ...

class IDXFileFactory(IFileFactory):
    """adapter factory for DX types"""
