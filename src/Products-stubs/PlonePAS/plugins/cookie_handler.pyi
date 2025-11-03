from _typeshed import Incomplete
from Products.PluggableAuthService.plugins.CookieAuthHelper import (
    CookieAuthHelper as BasePlugin,
)

def manage_addExtendedCookieAuthHelper(
    self, id, title: str = "", RESPONSE=None, **kw
) -> None:
    """Create an instance of a extended cookie auth helper."""

manage_addExtendedCookieAuthHelperForm: Incomplete

class ExtendedCookieAuthHelper(BasePlugin):
    """Multi-plugin which adds ability to override the updating of cookie via
    a setAuthCookie method/script.
    """

    meta_type: str
    security: Incomplete
    @security.private
    def updateCredentials(self, request, response, login, new_password) -> None:
        """Override standard updateCredentials method"""
    @security.public
    def login(self) -> None:
        """Set a cookie and redirect to the url that we tried to
        authenticate against originally.

        Override standard login method to avoid calling
        'return response.redirect(came_from)' as there is additional
        processing to ignore known bad come_from templates at
        login_next.cpy script.
        """
