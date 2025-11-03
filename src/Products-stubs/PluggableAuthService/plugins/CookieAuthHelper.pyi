from ..plugins.BasePlugin import BasePlugin
from _typeshed import Incomplete
from OFS.Folder import Folder
from zope.interface import Interface

class ICookieAuthHelper(Interface):
    """Marker interface."""

manage_addCookieAuthHelperForm: Incomplete

def addCookieAuthHelper(
    dispatcher, id, title=None, cookie_name: str = "", REQUEST=None
) -> None:
    """Add a Cookie Auth Helper to a Pluggable Auth Service."""

def decode_cookie(raw): ...
def decode_hex(raw): ...

class CookieAuthHelper(Folder, BasePlugin):
    """Multi-plugin for managing details of Cookie Authentication."""

    meta_type: str
    zmi_icon: str
    cookie_name: str
    login_path: str
    cookie_same_site: str
    cookie_same_site_choices: Incomplete
    cookie_secure: bool
    security: Incomplete
    manage_options: Incomplete
    title: Incomplete
    def __init__(self, id, title=None, cookie_name: str = "") -> None: ...
    @security.private
    def extractCredentials(self, request):
        """Extract credentials from cookie or 'request'."""
    @security.private
    def challenge(self, request, response, **kw):
        """Challenge the user for credentials."""
    @security.private
    def get_cookie_value(self, login, new_password): ...
    @security.private
    def updateCredentials(self, request, response, login, new_password) -> None:
        """Respond to change of credentials (NOOP for basic auth)."""
    @security.private
    def resetCredentials(self, request, response) -> None:
        """Raise unauthorized to tell browser to clear credentials."""
    @security.private
    def manage_afterAdd(self, item, container) -> None:
        """Setup tasks upon instantiation"""
    @security.private
    def unauthorized(self): ...
    @security.private
    def getLoginURL(self):
        """Where to send people for logging in"""
    @security.public
    def login(self):
        """Set a cookie and redirect to the url that we tried to
        authenticate against originally.
        """

BASIC_LOGIN_FORM: str
