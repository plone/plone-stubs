from _typeshed import Incomplete
from plone.app.users.browser.schemaeditor import USERS_NAMESPACE
from plone.app.users.browser.schemaeditor import USERS_PREFIX
from zope.interface import Interface

form_vocab: Incomplete

class IUserFormSelection(Interface):
    forms: Incomplete

def get_user_form_selection(schema_context, field): ...
def get_user_addform_selection(schema_context): ...

class UserFormSelectionAdapter:
    field: Incomplete
    def __init__(self, field) -> None: ...
    forms: Incomplete

class UserFormSelectionMetadata:
    namespace = USERS_NAMESPACE
    prefix = USERS_PREFIX
    def read(self, fieldNode, schema, field) -> None: ...
    def write(self, fieldNode, schema, field) -> None: ...
