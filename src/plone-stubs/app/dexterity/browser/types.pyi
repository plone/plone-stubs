from _typeshed import Incomplete
from OFS.SimpleItem import SimpleItem
from plone.schemaeditor.browser.schema.traversal import SchemaContext
from plone.z3cform.crud import crud
from plone.z3cform.layout import FormWrapper
from zope.cachedescriptors.property import Lazy as lazy_property

ALLOWED_FIELDS: Incomplete

class TypeEditSubForm(crud.EditSubForm):
    """Content type edit subform. Just here to use a custom template."""

    template: Incomplete

class TypeEditForm(crud.EditForm):
    """Content type edit form.

    Just a normal CRUD form without the form title or edit button.
    """

    label: Incomplete
    editsubform_factory = TypeEditSubForm
    buttons: Incomplete
    handlers: Incomplete
    status: Incomplete
    def handleClone(self, action) -> None: ...
    def handleExport(self, action) -> None: ...
    def handleExportModels(self, action) -> None: ...

class TypesEditFormWrapper(FormWrapper):
    """Render Plone frame around our form with little modifications"""

    form = TypeEditForm
    index: Incomplete

class TypeSettingsAdapter:
    context: Incomplete
    def __init__(self, context) -> None: ...
    @property
    def id(self): ...
    title: Incomplete
    description: Incomplete
    @property
    def container(self): ...
    allowed_content_types: Incomplete
    filter_content_types: Incomplete

class TypeStatsAdapter:
    context: Incomplete
    def __init__(self, context) -> None: ...
    @property
    def item_count(self): ...

class TypesListing(crud.CrudForm):
    """The combined content type edit + add forms."""
    @lazy_property
    def description(self): ...
    template: Incomplete
    view_schema: Incomplete
    addform_factory: Incomplete
    editform_factory = TypeEditForm
    def get_items(self):
        """Look up all Dexterity FTIs via the component registry.

        (These utilities are created via an IObjectCreated handler for the
        DexterityFTI class, configured in plone.dexterity.)
        """
    def remove(self, id_and_item) -> None:
        """Remove a content type."""
    def link(self, item, field):
        """Generate links to the edit page for each type.

        (But only for types with schemata that can be edited through the web.)
        """

TypesListingPage: Incomplete

class TypeSchemaContext(SchemaContext):
    fti: Incomplete
    schemaName: str
    schemaEditorView: str
    allowedFields = ALLOWED_FIELDS
    def browserDefault(self, request): ...
    @property
    def additionalSchemata(self): ...

class TypesContext(SimpleItem):
    """This class represents the types configlet.

    It allows us to traverse through it to (a wrapper of) the schema
    of a particular type.
    """

    id: Incomplete
    Title: Incomplete
    def __init__(self, context, request) -> None: ...
    def publishTraverse(self, request, name):
        """Traverse to a schema context.

        1. Try to find a content type whose name matches the next URL path
           element.
        2. Look up its schema.
        3. Return a schema context (an acquisition-aware wrapper of the
           schema).
        """
    def browserDefault(self, request):
        """Show the 'edit' view by default.

        If we aren't traversing to a schema beneath the types configlet,
        we actually want to see the TypesListingPage.
        """
