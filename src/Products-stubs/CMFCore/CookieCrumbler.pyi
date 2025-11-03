from .utils import UniqueObject
from _typeshed import Incomplete
from AccessControl.Permissions import view_management_screens
from OFS.PropertyManager import PropertyManager
from OFS.SimpleItem import SimpleItem

ATTEMPT_NONE: int
ATTEMPT_LOGIN: int
ATTEMPT_RESUME: int
ModifyCookieCrumblers: str
ViewManagementScreens = view_management_screens

class CookieCrumblerDisabled(Exception):
    """Cookie crumbler should not be used for a certain request."""

class CookieCrumbler(UniqueObject, PropertyManager, SimpleItem):
    """Reads cookies during traversal and simulates the HTTP auth headers."""

    id: str
    manage_options: Incomplete
    meta_type: str
    zmi_icon: str
    security: Incomplete
    auth_cookie: str
    name_cookie: str
    pw_cookie: str
    persist_cookie: str
    local_cookie_path: bool
    cache_header_value: str
    log_username: bool
    @security.private
    def delRequestVar(self, req, name) -> None: ...
    @security.public
    def getCookiePath(self): ...
    @security.private
    def getCookieMethod(self, name, default=None): ...
    @security.private
    def defaultSetAuthCookie(self, resp, cookie_name, cookie_value) -> None: ...
    @security.private
    def defaultExpireAuthCookie(self, resp, cookie_name) -> None: ...
    @security.private
    def modifyRequest(self, req, resp):
        """Copies cookie-supplied credentials to the basic auth fields.

        Returns a flag indicating what the user is trying to do with
        cookies: ATTEMPT_NONE, ATTEMPT_LOGIN, or ATTEMPT_RESUME.  If
        cookie login is disabled for this request, raises
        CookieCrumblerDisabled.
        """
    def __call__(self, container, req) -> None:
        """The __before_publishing_traverse__ hook."""
    @security.public
    def credentialsChanged(self, user, name, pw, request=None) -> None:
        """
        Updates cookie credentials if user details are changed.
        """
    @security.public
    def logout(self, response=None) -> None:
        """
        Logs out the user
        """
    @security.public
    def propertyLabel(self, id):
        """Return a label for the given property id"""

def handleCookieCrumblerEvent(ob, event) -> None:
    """Event subscriber for (un)registering a CC as a before traverse hook."""

manage_addCCForm: Incomplete

def manage_addCC(dispatcher, id, title: str = "", REQUEST=None):
    """ """
