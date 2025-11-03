from _typeshed import Incomplete

noNS_re: Incomplete

def ns(name, prefix=...):
    """Return the element or attribute name with the given prefix"""

def noNS(name):
    """Return the tag with no namespace"""

def indent(node, level: int = 0) -> None: ...
def prettyXML(tree): ...
def fieldTypecast(field, value): ...
def elementToValue(field, element, default=...):
    """Read the contents of an element that is assumed to represent a value
    allowable by the given field.

    If converter is given, it should be an IToUnicode instance.

    If not, the field will be adapted to this interface to obtain a converter.
    """

def valueToElement(field, value, name=None, force: bool = False):
    """Create and return an element that describes the given value, which is
    assumed to be valid for the given field.

    If name is given, this will be used as the new element name. Otherwise,
    the field's __name__ attribute is consulted.

    If force is True, the value will always be written. Otherwise, it is only
    written if it is not equal to field.missing_value.
    """

def relativeToCallingPackage(filename, callingFrame: int = 2):
    """If the filename is not an absolute path, make it into an absolute path
    by calculating the relative path from the module that called the function
    at 'callingFrame' steps down the stack.
    """

def sortedFields(schema):
    """Like getFieldsInOrder, but does not include fields from bases"""

def mergedTaggedValueDict(schema, name):
    """Look up the tagged value 'name' in schema and all its bases, assuming
    that the value under 'name' is a dict. Return a dict that consists of
    all dict items, with those from more-specific interfaces overriding those
    from more-general ones.
    """

def mergedTaggedValueList(schema, name):
    """Look up the tagged value 'name' in schema and all its bases, assuming
    that the value under 'name' is a list. Return a list that consists of
    all elements from all interfaces and base interfaces, with values from
    more-specific interfaces appearing at the end of the list.
    """

def syncSchema(source, dest, overwrite: bool = False, sync_bases: bool = False) -> None:
    """Copy attributes and tagged values from the source to the destination.
    If overwrite is False, do not overwrite attributes or tagged values that
    already exist or delete ones that don't exist in source.
    """
