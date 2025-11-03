from _typeshed import Incomplete
from zope.interface.interfaces import ObjectEvent

def sortedFields(schema):
    """Like getFieldsInOrder, but does not include fields from bases

    This is verbatim from plone.supermodel's utils.py but I didn't
    want to create a dependency.
    """

def non_fieldset_fields(schema): ...
def get_field_fieldset(schema, field_name): ...
def get_fieldset_from_index(schema, index):
    """Return a fieldset from a schema according to it's index."""

def new_field_position(schema, fieldset_id=None, new_field: bool = False):
    """Get the position for a new field in a schema's fieldset.
    If fieldset_id is ``None`` or ``0``, the default fieldset is used.
    """

class EditableSchema:
    """Zope 3 schema adapter to allow addition/removal of schema fields

    XXX this needs to be made threadsafe
    """

    schema: Incomplete
    def __init__(self, schema) -> None: ...
    def addField(self, field, name=None) -> None:
        """Add a field"""
    def removeField(self, field_name) -> None:
        """Remove a field"""
    def moveField(self, field_name, new_pos):
        """Move a field to the (new_pos)th position in the schema's sort
        order (indexed beginning at 0).

        Schema fields are assigned an 'order' attribute that increments for
        each new field instance.
        We shuffle these around in case it matters anywhere that they're
        unique.
        """
    def changeFieldFieldset(self, field_name, next_fieldset) -> None:
        """Move a field from a fieldset to another,
        next_fieldset is a fieldset object, or None for default fieldset
        """

class SchemaModifiedEvent(ObjectEvent): ...

class FieldModifiedEvent(SchemaModifiedEvent):
    field: Incomplete
    def __init__(self, obj, field) -> None: ...

class FieldAddedEvent(FieldModifiedEvent): ...
class FieldRemovedEvent(FieldModifiedEvent): ...
