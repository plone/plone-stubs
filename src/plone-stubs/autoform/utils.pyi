def resolveDottedName(dottedName):
    """Resolve a dotted name to a real object"""

def mergedTaggedValuesForIRO(schema, name, iro):
    """Finds a list of (interface, fieldName, value) 3-ples from the tagged
    value named 'name', on 'schema' and all of its bases.  Returns a dict of
    fieldName => value, where the value is from the tuple for that fieldName
    whose interface is highest in the interface resolution order, among the
    interfaces actually provided by 'form'.
    """

def mergedTaggedValuesForForm(schema, name, form): ...
def processFields(
    form, schema, prefix: str = "", defaultGroup=None, permissionChecks: bool = True
) -> None:
    """Add the fields from the schema to the form, taking into account
    the hints in the various tagged values as well as fieldsets. If prefix
    is given, the fields will be prefixed with this prefix. If
    defaultGroup is given (as a Fieldset instance), any field not explicitly
    placed into a particular fieldset, will be added to the given group,
    which must exist already. If permissionChecks is false,
    permission checks are ignored.
    """

def processFieldMoves(form, schema, prefix: str = "") -> None:
    """Process all field moves stored under ORDER_KEY in the schema tagged
    value. This should be run after all schemata have been processed with
    processFields().
    """
