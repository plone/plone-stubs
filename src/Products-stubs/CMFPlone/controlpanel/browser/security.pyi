from _typeshed import Incomplete
from plone.app.registry.browser import controlpanel
from plone.base.interfaces import ISecuritySchema
from Products.Five.browser import BrowserView

logger: Incomplete

class SecurityControlPanelForm(controlpanel.RegistryEditForm):
    id: str
    label: Incomplete
    schema = ISecuritySchema
    schema_prefix: str

class SecurityControlPanel(controlpanel.ControlPanelFormWrapper):
    form = SecurityControlPanelForm

class EmailLogin(BrowserView):
    """View to help in migrating to or from using email as login.

    We used to change the login name of existing users here, but that
    is now done by checking or unchecking the option in the security
    control panel.  Here you can only search for duplicates.
    """

    duplicates: Incomplete
    def __call__(self): ...
    def check_email(self): ...
    def check_userid(self): ...
    def switch_to_email(self) -> None: ...
    def switch_to_userid(self) -> None: ...
