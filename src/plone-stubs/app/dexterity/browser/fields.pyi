from _typeshed import Incomplete
from plone.app.dexterity.browser.layout import TypeFormLayout
from plone.schemaeditor.browser.schema.listing import SchemaListing

HAS_RESOURCEEDITOR: bool

class EnhancedSchemaListing(SchemaListing):
    def handleModelEdit(self, action) -> None: ...

but: Incomplete
handler: Incomplete

class TypeFieldsPage(TypeFormLayout):
    label: Incomplete
    @property
    def form(self): ...
