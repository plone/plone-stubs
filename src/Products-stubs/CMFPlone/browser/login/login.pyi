from _typeshed import Incomplete
from functools import cached_property as cached_property
from plone.app.users.browser.passwordpanel import PasswordPanel
from Products.Five.browser import BrowserView
from z3c.form import form

logger: Incomplete
LOGIN_TEMPLATE_IDS: Incomplete

class LoginForm(form.EditForm):
    """Implementation of the login form"""

    fields: Incomplete
    id: str
    label: Incomplete
    ignoreContext: bool
    prefix: str
    def render(self): ...
    def updateWidgets(self) -> None: ...
    def get_came_from(self): ...
    status: Incomplete
    def handleLogin(self, action) -> None: ...
    def handle_initial_login(self) -> None: ...
    def force_password_change(self) -> None: ...
    @cached_property
    def portal_state(self):
        """Return the portal state."""
    def redirect_after_login(
        self, came_from=None, is_initial_login: bool = False
    ) -> None:
        """Handle redirect after successful login."""
    def self_registration_enabled(self): ...
    def use_email_as_login(self): ...

class FailsafeLoginForm(LoginForm):
    def render(self): ...

class RequireLoginView(BrowserView):
    def __call__(self) -> None: ...

class InsufficientPrivilegesView(BrowserView):
    def request_url(self): ...

class InitialLoginPasswordChange(PasswordPanel):
    def render(self): ...
    def action_reset_passwd(self, action) -> None: ...

class ForcedPasswordChange(PasswordPanel):
    def render(self): ...
    def action_reset_passwd(self, action) -> None: ...
