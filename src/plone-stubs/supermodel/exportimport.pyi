from _typeshed import Incomplete

import zope.schema

class OrderedDictField(zope.schema.Dict): ...

class BaseHandler:
    """Base class for import/export handlers.

    The read_field method is called to read one field of the known subtype
    from an XML element.

    The write_field method is called to write one field to a particular
    element.
    """

    filteredAttributes: Incomplete
    fieldTypeAttributes: Incomplete
    nonValidatedfieldTypeAttributes: Incomplete
    fieldInstanceAttributes: Incomplete
    forcedFields: Incomplete
    klass: Incomplete
    fieldAttributes: Incomplete
    def __init__(self, klass) -> None: ...
    def read(self, element):
        """Read a field from the element and return a new instance"""
    def write(self, field, name, type, elementName: str = "field"):
        """Create and return a new element representing the given field"""
    def readAttribute(self, element, attributeField):
        """Read a single attribute from the given element. The attribute is of
        a type described by the given Field object.
        """
    def writeAttribute(self, attributeField, field, ignoreDefault: bool = True):
        """Create and return a element that describes the given attribute
        field on the given field
        """

class DictHandler(BaseHandler):
    """Special handling for the Dict field, which uses Attribute instead of
    Field to describe its key_type and value_type.
    """
    def __init__(self, klass) -> None: ...

class ObjectHandler(BaseHandler):
    """Special handling for the Object field, which uses Attribute instead of
    Field to describe its schema
    """

    filteredAttributes: Incomplete
    def __init__(self, klass) -> None: ...

class ChoiceHandler(BaseHandler):
    """Special handling for the Choice field"""

    filteredAttributes: Incomplete
    def __init__(self, klass) -> None: ...
    def readAttribute(self, element, attributeField): ...
    def write(self, field, name, type, elementName: str = "field"): ...
