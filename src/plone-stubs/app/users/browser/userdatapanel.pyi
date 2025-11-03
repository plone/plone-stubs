from _typeshed import Incomplete
from plone.app.users.browser.account import AccountPanelForm
from plone.app.users.browser.account import AccountPanelSchemaAdapter

class UserDataPanelAdapter(AccountPanelSchemaAdapter):
    """One does not simply set portrait, email might be used to login with."""
    @property
    def schema(self): ...
    @schema.setter
    def schema(self, value) -> None: ...
    def get_email(self): ...
    def set_email(self, value): ...
    email: Incomplete

class UserDataPanel(AccountPanelForm):
    form_name: Incomplete
    enableCSRFProtection: bool
    @property
    def schema(self): ...
    @property
    def description(self): ...
    def __call__(self): ...

def getUserDataSchema(): ...

class UserDataConfiglet(UserDataPanel):
    """Control panel version of the userdata panel"""

    template: Incomplete
    tab: str
