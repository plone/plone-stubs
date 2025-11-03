from _typeshed import Incomplete
from plone.schemaeditor.browser.schema.listing import SchemaListing
from plone.schemaeditor.browser.schema.traversal import SchemaContext
from plone.z3cform.layout import FormWrapper
from zope.interface import Interface

USERS_NAMESPACE: str
USERS_PREFIX: str
SPLITTER: str
ALLOWED_FIELDS: Incomplete
field_type_mapping: Incomplete
DEFAULT_VALUES: Incomplete
re_flags: Incomplete

def log(
    message, level: str = "info", id: str = "plone.app.users.browser.schemaeditor"
) -> None: ...

class IMemberFieldValidator(Interface):
    """Base marker for field validators"""

class IMemberSchemaContext(Interface):
    """ """

class SchemaListingPage(FormWrapper):
    form = SchemaListing
    index: Incomplete

class MemberSchemaContext(SchemaContext):
    label: Incomplete
    fieldsWhichCannotBeDeleted: Incomplete
    showSaveDefaults: bool
    enableFieldsets: bool
    allowedFields: Incomplete
    def __init__(self, context, request) -> None: ...

def updateSchema(object, event) -> None: ...
def applySchema(snew_schema) -> None: ...
def get_ttw_edited_schema(): ...

class UsersMetadataSchemaExporter:
    """Support the security: namespace in model definitions."""

    namespace = USERS_NAMESPACE
    ns = USERS_NAMESPACE
    prefix = USERS_PREFIX
    if_attrs: Incomplete
    def read(self, fieldNode, schema, field) -> None: ...
    def write(self, fieldNode, schema, field) -> None: ...
    def load(self, value): ...
    def serialize(self, value): ...

def is_serialisable_field(field): ...
def serialize_ttw_schema(schema=None): ...
def load_ttw_schema(string=None): ...
def get_schema(site=None): ...
def set_schema(string, site=None) -> None: ...
def invalidateSchemasInCache(portal) -> None: ...
def getFromBaseSchema(baseSchema, form_name=None): ...
def copySchemaAttrs(schema, form_name): ...

default_fields: Incomplete

def field_in_form(field, form_name=None): ...
