from _typeshed import Incomplete
from zope.interface import Interface

class ICookieCrumbler(Interface):
    """Reads cookies during traversal and simulates the HTTP auth headers."""

    __module__: str
    auth_cookie: Incomplete
    name_cookie: Incomplete
    pw_cookie: Incomplete
    persist_cookie: Incomplete
    local_cookie_path: Incomplete
    cache_header_value: Incomplete
    log_username: Incomplete
    def delRequestVar(req, name) -> None:
        """No errors of any sort may propagate, and we don't care *what*
        they are, even to log them."""
    def getCookiePath() -> None:
        """Get the path for the cookie
        the parent URL if local_cookie_path is True otherwise /"""
    def getCookieMethod(name, default) -> None:
        """Get the cookie handler.
        The cookie handler maybe overridden by acquisition."""
    def defaultSetAuthCookie(resp, cookie_name, cookie_value) -> None:
        """Set the authorisation cookie"""
    def defaultExpireAuthCookie(resp, cookie_name) -> None:
        """Expire the cookie"""
    def modifyRequest(req, resp) -> None:
        """Copies cookie-supplied credentials to the basic auth fields.

        Returns a flag indicating what the user is trying to do with
        cookies: ATTEMPT_NONE, ATTEMPT_LOGIN, or ATTEMPT_RESUME.  If
        cookie login is disabled for this request, raises
        CookieCrumblerDisabled.
        """
    def __call__(container, req) -> None:
        """The __before_publishing_traverse__ hook."""
    def credentialsChanged(user, name, pw, request) -> None:
        """
        Updates cookie credentials if user details are changed.
        """
    def propertyLabel(id) -> None:
        """Return a label for the given property id"""
    def logout(response) -> None:
        """
        Deprecated
        Log the user out"""
