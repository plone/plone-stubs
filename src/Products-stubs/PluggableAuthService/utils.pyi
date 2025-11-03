from _typeshed import Incomplete
from AccessControl.requestmethod import postonly as postonly
from zope.publisher.interfaces.browser import IBrowserRequest as IBrowserRequest

logger: Incomplete

def directlyProvides(obj, *interfaces): ...
def classImplements(class_, *interfaces): ...

product_dir: Incomplete
product_prefix: Incomplete

def makestr(s):
    """Converts 's' to a non-Unicode string"""

def createViewName(method_name, user_handle=None):
    """
    Centralized place for creating the "View Name" that identifies
    a ZCacheable record in a RAMCacheManager
    """

def createKeywords(**kw):
    """
    Centralized place for creating the keywords that identify
    a ZCacheable record in a RAMCacheManager.

    Keywords are hashed so we don't accidentally expose sensitive
    information.
    """

def getCSRFToken(request): ...
def checkCSRFToken(request, token: str = "csrf_token", raises: bool = True):
    """Check CSRF token in session against token formdata.

    If the values don't match, and 'raises' is True, raise a Forbidden.

    If the values don't match, and 'raises' is False, return False.

    If the values match, return True.
    """

class CSRFToken:
    security: Incomplete
    context: Incomplete
    request: Incomplete
    def __init__(self, context, request) -> None: ...
    def __call__(self) -> None: ...
    def token(self): ...

def csrf_only(wrapped): ...
def url_local(url):
    """Helper to convert a URL into a site-local URL

    This function removes the protocol and host parts of a URL in order to
    prevent open redirect issues.
    """
