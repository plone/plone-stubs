from _typeshed import Incomplete
from collections.abc import Generator

FIELD_PROPERTIES_MAPPING: Incomplete

class FakeDXContext:
    """Fake DX content class, so we can reuse the DX field deserializers"""

def create_form(context, request, base_schema, additional_schemata=None):
    """Create a minimal, standalone z3c form and run the field processing
    logic of plone.autoform on it.
    """

def iter_fields(fieldsets) -> Generator[Incomplete, Incomplete]:
    """Iterate over a flat list of fields, given a list of fieldset dicts
    as returned by `get_fieldsets`.
    """

def get_form_fieldsets(form):
    """Get fieldsets from form"""

def get_fieldsets(context, request, schema, additional_schemata=None):
    """Given a base schema, and optionally some additional schemata,
    build a list of fieldsets with the corresponding z3c.form fields in them.
    """

def get_fieldset_infos(fieldsets):
    """Given a list of fieldset dicts as returned by `get_fieldsets()`,
    return a list of fieldset info dicts that contain the (short) field name
    instead of the actual field instance.
    """

def get_jsonschema_properties(
    context, request, fieldsets, prefix: str = "", excluded_fields=None
):
    """Build a JSON schema 'properties' list, based on a list of fieldset
    dicts as returned by `get_fieldsets()`.
    """

def get_widget_params(schemas): ...
def get_multilingual_directives(schemas): ...
def get_jsonschema_for_fti(fti, context, request, excluded_fields=None):
    """Build a complete JSON schema for the given FTI."""

def get_jsonschema_for_portal_type(portal_type, context, request, excluded_fields=None):
    """Build a complete JSON schema for the given portal_type."""

def get_vocab_like_url(endpoint, locator, context, request): ...
def get_vocabulary_url(vocab_name, context, request): ...
def get_querysource_url(field, context, request): ...
def get_source_url(field, context, request): ...
def serializeSchema(schema) -> None:
    """Taken from plone.app.dexterity.serialize
    Finds the FTI and model associated with a schema, and synchronizes
    the schema to the FTI model_source attribute.
    """

def get_info_for_type(context, request, name):
    """Get JSON info for the given portal type"""

def get_info_for_field(context, request, name):
    """Get JSON info for the given field name."""

def get_info_for_fieldset(context, request, name):
    """Get JSON info for the given fieldset name."""

def delete_field(context, request, name) -> None: ...
def delete_fieldset(context, request, name) -> None:
    """Taken from plone.schemaeditor 2.x `DeleteFieldset`"""

def add_fieldset(context, request, data): ...
def add_field(context, request, data): ...
def update_fieldset(context, request, data) -> None: ...
def update_field(context, request, data) -> None: ...
