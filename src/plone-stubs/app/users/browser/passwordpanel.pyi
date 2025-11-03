from _typeshed import Incomplete
from plone.app.users.browser.account import AccountPanelForm
from zope.interface import Interface

class IPasswordSchema(Interface):
    """Provide schema for password form"""

    current_password: Incomplete
    new_password: Incomplete
    new_password_ctl: Incomplete

class PasswordPanelAdapter:
    context: Incomplete
    def __init__(self, context) -> None: ...
    def get_dummy(self):
        """We don't actually need to 'get' anything ..."""
    current_password: Incomplete
    new_password: Incomplete
    new_password_ctl: Incomplete

class PasswordPanel(AccountPanelForm):
    """Implementation of password reset form that uses z3c.form."""

    description: Incomplete
    form_name: Incomplete
    schema = IPasswordSchema
    def updateFields(self) -> None: ...
    def validate_password(self, action, data) -> None: ...
    status: Incomplete
    def action_reset_passwd(self, action) -> None: ...
    def handleSave(self, action) -> None: ...
    def cancel(self, action) -> None: ...
