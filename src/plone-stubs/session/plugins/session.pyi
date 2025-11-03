from _typeshed import Incomplete
from AccessControl.requestmethod import postonly
from Products.PluggableAuthService.plugins.BasePlugin import BasePlugin

EMPTY_GIF: str
manage_addSessionPluginForm: Incomplete

def manage_addSessionPlugin(
    dispatcher, id, title=None, path: str = "/", REQUEST=None
) -> None:
    """Add a session plugin."""

def cookie_expiration_date(days): ...

class SessionPlugin(BasePlugin):
    """Session authentication plugin."""

    meta_type: str
    security: Incomplete
    cookie_name: str
    cookie_lifetime: int
    cookie_domain: str
    mod_auth_tkt: bool
    timeout: Incomplete
    refresh_interval: Incomplete
    external_ticket_name: str
    secure: bool
    secret_prefix: str
    per_user_keyring: bool
    manage_options: Incomplete
    title: Incomplete
    path: Incomplete
    def __init__(self, id, title=None, path: str = "/") -> None: ...
    def extractCredentials(self, request): ...
    def authenticateCredentials(self, credentials): ...
    def updateCredentials(self, request, response, login, new_password) -> None: ...
    def resetCredentials(self, request, response) -> None: ...
    manage_secret: Incomplete
    @postonly
    def manage_clearSecrets(self, REQUEST) -> None:
        """Clear all secrets from this source. This invalidates all current
        sessions and requires users to login again.
        """
    @postonly
    def manage_createNewSecret(self, REQUEST) -> None:
        """Create a new (signing) secret."""
    @postonly
    def manage_togglePerUserKeyring(self, REQUEST) -> None:
        """Toggle per-user keyrings."""
    def haveSharedSecret(self): ...
    @postonly
    def manage_removeSharedSecret(self, REQUEST) -> None:
        """Clear the shared secret. This invalidates all current sessions and
        requires users to login again.
        """
    @postonly
    def manage_setSharedSecret(self, REQUEST) -> None:
        """Set the shared secret."""
    @security.public
    def refresh(self, REQUEST):
        """Refresh the cookie"""
    @security.public
    def remove(self, REQUEST):
        """Remove the cookie"""
