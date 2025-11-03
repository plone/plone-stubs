from ..plugins.BasePlugin import BasePlugin
from _typeshed import Incomplete
from zope.interface import Interface

manage_addHTTPBasicAuthHelperForm: Incomplete

class IHTTPBasicAuthHelper(Interface):
    """Marker interface."""

def addHTTPBasicAuthHelper(dispatcher, id, title=None, REQUEST=None) -> None:
    """Add a HTTP Basic Auth Helper to a Pluggable Auth Service."""

class HTTPBasicAuthHelper(BasePlugin):
    """Multi-plugin for managing details of HTTP Basic Authentication."""

    meta_type: str
    zmi_icon: str
    security: Incomplete
    protocol: str
    title: Incomplete
    def __init__(self, id, title=None) -> None: ...
    @security.private
    def extractCredentials(self, request):
        """Extract basic auth credentials from 'request'."""
    @security.private
    def challenge(self, request, response, **kw):
        """Challenge the user for credentials."""
    @security.private
    def resetCredentials(self, request, response) -> None:
        """Raise unauthorized to tell browser to clear credentials."""
