from ..plugins.BasePlugin import BasePlugin
from _typeshed import Incomplete
from zope.interface import Interface

class ISessionAuthHelper(Interface):
    """Marker interface."""

manage_addSessionAuthHelperForm: Incomplete

def manage_addSessionAuthHelper(dispatcher, id, title=None, REQUEST=None) -> None:
    """Add a Session Auth Helper to a Pluggable Auth Service."""

class SessionAuthHelper(BasePlugin):
    """Multi-plugin for managing details of Session Authentication."""

    meta_type: str
    zmi_icon: str
    security: Incomplete
    title: Incomplete
    def __init__(self, id, title=None) -> None: ...
    @security.private
    def extractCredentials(self, request):
        """Extract basic auth credentials from 'request'."""
    @security.private
    def updateCredentials(self, request, response, login, new_password) -> None:
        """Respond to change of credentials."""
    @security.private
    def resetCredentials(self, request, response) -> None:
        """Empty out the currently-stored session values"""
