from _typeshed import Incomplete
from AccessControl.requestmethod import postonly
from Products.PluggableAuthService.plugins.BasePlugin import BasePlugin

OLD_JWT: bool
manage_addJWTAuthenticationPlugin: Incomplete

def addJWTAuthenticationPlugin(self, id_, title=None, REQUEST=None) -> None:
    """Add a JWT authentication plugin"""

class JWTAuthenticationPlugin(BasePlugin):
    """Plone PAS plugin for authentication with JSON web tokens (JWT)."""

    meta_type: str
    security: Incomplete
    token_timeout: Incomplete
    use_keyring: bool
    store_tokens: bool
    manage_options: Incomplete
    manage_config: Incomplete
    title: Incomplete
    def __init__(self, id_, title=None) -> None: ...
    @security.private
    def challenge(self, request, response, **kw): ...
    @security.private
    def extractCredentials(self, request):
        """
        Extract credentials either from a JSON POST request or an established JWT token.
        """
    @security.private
    def authenticateCredentials(self, credentials): ...
    @postonly
    def manage_updateConfig(self, REQUEST) -> None:
        """Update configuration of JWT Authentication Plugin."""
    def delete_token(self, token): ...
    def create_token(self, userid, timeout=None, data=None): ...
