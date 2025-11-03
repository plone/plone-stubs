from _typeshed import Incomplete
from Acquisition import Implicit
from App.Management import Tabs
from OFS.owner import Owned
from OFS.role import RoleManager
from OFS.SimpleItem import Item
from Persistence import Persistent

badidnamecharsin: Incomplete
badcookiecharsin: Incomplete
twodotsin: Incomplete
constructBrowserIdManagerForm: Incomplete
BROWSERID_MANAGER_NAME: str
ALLOWED_BID_NAMESPACES: Incomplete
TRAVERSAL_APPHANDLE: str
LOG: Incomplete
using_sysrandom: bool

def constructBrowserIdManager(
    self,
    id=...,
    title: str = "",
    idname: str = "_ZopeId",
    location=("cookies", "form"),
    cookiepath: str = "/",
    cookiedomain: str = "",
    cookielifedays: int = 0,
    cookiesecure: int = 0,
    cookiehttponly: int = 0,
    auto_url_encoding: int = 0,
    cookiesamesite: str = "Lax",
    REQUEST=None,
):
    """ """

class BrowserIdManager(Item, Persistent, Implicit, RoleManager, Owned, Tabs):
    """browser id management class"""

    meta_type: str
    zmi_icon: str
    security: Incomplete
    ok: Incomplete
    auto_url_encoding: int
    cookie_http_only: int
    cookie_same_site: Incomplete
    id: Incomplete
    title: Incomplete
    def __init__(
        self,
        id,
        title: str = "",
        idname: str = "_ZopeId",
        location=("cookies", "form"),
        cookiepath: str = "/",
        cookiedomain: str = "",
        cookielifedays: int = 0,
        cookiesecure: int = 0,
        cookiehttponly: int = 0,
        auto_url_encoding: int = 0,
        cookiesamesite: str = "Lax",
    ) -> None: ...
    def hasBrowserId(self):
        """See IBrowserIdManager."""
    def getBrowserId(self, create: int = 1):
        """See IBrowserIdManager."""
    def getBrowserIdName(self):
        """See IBrowserIdManager."""
    def isBrowserIdNew(self):
        """See IBrowserIdManager."""
    def isBrowserIdFromCookie(self):
        """See IBrowserIdManager."""
    def isBrowserIdFromForm(self):
        """See IBrowserIdManager."""
    def isBrowserIdFromUrl(self):
        """See IBrowserIdManager."""
    def flushBrowserIdCookie(self) -> None:
        """See IBrowserIdManager."""
    def setBrowserIdCookieByForce(self, bid) -> None:
        """See IBrowserIdManager."""
    def getHiddenFormField(self):
        """See IBrowserIdManager."""
    def encodeUrl(self, url, style: str = "querystring", create: int = 1): ...
    browserid_name: Incomplete
    def setBrowserIdName(self, k) -> None:
        """Set browser id name string

        o Enforce "valid" values.
        """
    browserid_namespaces: Incomplete
    def setBrowserIdNamespaces(self, ns) -> None:
        """
        accepts list of allowable browser id namespaces
        """
    def getBrowserIdNamespaces(self):
        """ """
    cookie_path: Incomplete
    def setCookiePath(self, path: str = "") -> None:
        """sets cookie 'path' element for id cookie"""
    def getCookiePath(self):
        """ """
    cookie_life_days: Incomplete
    def setCookieLifeDays(self, days) -> None:
        """offset for id cookie 'expires' element"""
    def getCookieLifeDays(self):
        """ """
    cookie_domain: str
    def setCookieDomain(self, domain) -> None:
        """sets cookie 'domain' element for id cookie"""
    def getCookieDomain(self):
        """ """
    def setCookieHTTPOnly(self, http_only) -> None:
        """sets cookie 'HTTPOnly' on or off"""
    def getCookieHTTPOnly(self):
        """retrieve the 'HTTPOnly' flag"""
    cookie_secure: Incomplete
    def setCookieSecure(self, secure) -> None:
        """sets cookie 'secure' element for id cookie"""
    def getCookieSecure(self):
        """ """
    def setCookieSameSite(self, same_site: str = "Lax") -> None:
        """sets cookie 'SameSite' flag"""
    def getCookieSameSite(self):
        """retrieve the cookie 'SameSite' flag value"""
    def setAutoUrlEncoding(self, auto_url_encoding) -> None:
        """sets 'auto url encoding' on or off"""
    def getAutoUrlEncoding(self):
        """ """
    def isUrlInBidNamespaces(self):
        """Returns true if 'url' is in the browser id namespaces
        for this browser id"""
    @security.private
    def hasTraversalHook(self, parent): ...
    @security.private
    def updateTraversalData(self) -> None: ...
    @security.private
    def unregisterTraversalHook(self) -> None: ...
    @security.private
    def registerTraversalHook(self) -> None: ...
    manage_options: Incomplete
    def manage_afterAdd(self, item, container) -> None:
        """Maybe add our traversal hook"""
    def manage_beforeDelete(self, item, container) -> None:
        """Remove our traversal hook if it exists"""
    manage_browseridmgr: Incomplete
    def manage_changeBrowserIdManager(
        self,
        title: str = "",
        idname: str = "_ZopeId",
        location=("cookies", "form"),
        cookiepath: str = "/",
        cookiedomain: str = "",
        cookielifedays: int = 0,
        cookiesecure: int = 0,
        cookiehttponly: int = 0,
        auto_url_encoding: int = 0,
        cookiesamesite=None,
        REQUEST=None,
    ) -> None:
        """ """

class BrowserIdManagerTraverser(Persistent):
    def __call__(
        self,
        container,
        request,
        browser_id=None,
        browser_id_ns=None,
        BROWSERID_MANAGER_NAME=...,
    ) -> None:
        """
        Registered hook to set and get a browser id in the URL.  If
        a browser id is found in the URL of an  incoming request, we put it
        into a place where it can be found later by the browser id manager.
        If our browser id manager's auto-url-encoding feature is on, cause
        Zope-generated URLs to contain the browser id by rewriting the
        request._script list.
        """

def getB64TStamp(b2a=..., gmtime=..., time=..., TimeStamp=...): ...
def getB64TStampToInt(ts, TimeStamp=..., a2b=...): ...
def getBrowserIdPieces(bid):
    """returns browser id parts in a tuple consisting of rand_id,
    timestamp
    """

def isAWellFormedBrowserId(bid, binerr=...): ...
def getNewBrowserId(randint=..., maxint: int = 99999999):
    """Returns 19-character string browser id
    'AAAAAAAABBBBBBBB'
    where:

    A == leading-0-padded 8-char string-rep'd random integer
    B == modified base64-encoded 11-char timestamp

    To be URL-compatible, base64 encoding is modified as follows:
      '=' end-padding is stripped off
      '+' is translated to '-'
      '/' is translated to '.'

    An example is: 89972317A0C3EHnUi90w
    """
