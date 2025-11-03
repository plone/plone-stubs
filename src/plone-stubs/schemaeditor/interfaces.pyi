from _typeshed import Incomplete
from OFS.interfaces import IItem
from z3c.form.interfaces import IEditForm
from zope.interface import invariant
from zope.interface.interfaces import IInterface
from zope.interface.interfaces import Interface
from zope.interface.interfaces import IObjectEvent
from zope.publisher.interfaces.browser import IBrowserPage
from zope.schema.interfaces import IField

class ISchemaView(IBrowserPage):
    """A publishable view of a zope 3 schema"""

class ISchemaContext(IItem):
    """A publishable wrapper of a zope 3 schema"""

    schema: Incomplete
    schemaEditorView: Incomplete
    additionalSchemata: Incomplete
    allowedFields: Incomplete
    fieldsWhichCannotBeDeleted: Incomplete
    enableFieldsets: Incomplete

class ISchemaModifiedEvent(IObjectEvent):
    object: Incomplete

class IFieldContext(IItem):
    """A publishable wrapper of a zope 3 schema field"""

    field: Incomplete

class IFieldEditorExtender(IInterface):
    """An additional schema for use when editing a field."""

class IFieldFactory(IField):
    """A component that instantiates a field when called."""

    title: Incomplete
    def available(self) -> None:
        """field is addable in the current context"""
    def editable(self, field) -> None:
        """test whether a given instance of a field is editable"""
    def protected(self, field) -> None:
        """test whether a given instance of a field is protected"""

class IEditableSchema(Interface):
    """Interface for adding/removing fields to/from a schema."""
    def addField(field, name=None) -> None:
        """Add a field to a schema

        If not provided, the field's name will be taken from its __name__
        attribute.
        """
    def removeField(field_name) -> None:
        """Remove a field from a schema"""
    def moveField(field_name, new_pos) -> None:
        """Move a field to the (new_pos)th position in the schema's sort ç
        order (indexed beginning at 0).

        Schema fields are assigned an 'order' attribute that increments for
        each new field instance.
        We shuffle these around in case it matters anywhere that they're
        unique.
        """
    def changeFieldFieldset(field_name, next_fieldset) -> None:
        """Move a field from a fieldset to another,
        next_fieldset is a fieldset object, or None for default fieldset
        """

class IFieldEditForm(IEditForm):
    """Marker interface for field edit forms"""

class IFieldEditFormSchema(Interface):
    """The schema describing the form fields for a field."""

RESERVED_NAMES: Incomplete
ID_RE: Incomplete

def isValidFieldName(value): ...

class INewField(Interface):
    fieldset_id: Incomplete
    title: Incomplete
    description: Incomplete
    factory: Incomplete
    required: Incomplete
    @invariant
    def checkTitleAndDescriptionTypes(data) -> None: ...

class INewFieldset(Interface):
    label: Incomplete
    description: Incomplete
