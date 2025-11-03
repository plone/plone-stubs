from _typeshed import Incomplete
from plone.autoform.form import AutoExtensibleForm
from plone.z3cform.layout import FormWrapper
from z3c.form import form

class SchemaListing(AutoExtensibleForm, form.Form):
    ignoreContext: bool
    ignoreRequest: bool
    showEmptyGroups: bool
    template: Incomplete
    ignoreRequiredOnExtract: bool
    @property
    def schema(self): ...
    @property
    def additionalSchemata(self): ...
    def render(self): ...
    def field_type(self, field): ...
    def protected_field(self, field): ...
    def edit_url(self, field): ...
    def can_delete_fieldset(self, fieldset): ...
    def delete_url(self, field): ...
    def handleDone(self, action): ...
    status: Incomplete
    def handleSaveDefaults(self, action) -> None: ...
    def updateActions(self) -> None: ...

class ReadOnlySchemaListing(SchemaListing):
    buttons: Incomplete
    def edit_url(self, field) -> None: ...
    delete_url = edit_url

class SchemaListingPage(FormWrapper):
    """Form wrapper so we can get a form with layout.

    We define an explicit subclass rather than using the wrap_form method
    from plone.z3cform.layout so that we can inject the schema name into
    the form label.
    """

    form = SchemaListing
    @property
    def label(self):
        """In a dexterity schema editing context, we need to
        construct a label that will specify the field being
        edited. Outside that context (e.g., plone.app.users),
        we should respect the label if specified.
        """
