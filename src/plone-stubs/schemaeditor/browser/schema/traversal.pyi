from _typeshed import Incomplete
from OFS.SimpleItem import SimpleItem

class SchemaContext(SimpleItem):
    """This is a transient item that allows us to traverse through (a wrapper
    of) a zope 3 schema to (a wrapper of) a zope 3 schema field.
    """

    schemaEditorView: Incomplete
    additionalSchemata: Incomplete
    allowedFields: Incomplete
    fieldsWhichCannotBeDeleted: Incomplete
    enableFieldsets: bool
    schema: Incomplete
    request: Incomplete
    id: Incomplete
    Title: Incomplete
    def __init__(self, context, request, name: str = "schema", title=None) -> None: ...
    def publishTraverse(self, request, name):
        """Look up the field whose name matches the next URL path element,
        and wrap it.
        """
    def browserDefault(self, request):
        """If not traversing through the schema to a field,
        show the SchemaListingPage.
        """
