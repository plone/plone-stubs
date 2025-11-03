from ..plugins.BasePlugin import BasePlugin
from _typeshed import Incomplete
from OFS.Folder import Folder
from zope.interface import Interface

class IInlineAuthHelper(Interface):
    """Marker interface."""

manage_addInlineAuthHelperForm: Incomplete

def addInlineAuthHelper(dispatcher, id, title=None, REQUEST=None) -> None:
    """Add an Inline Auth Helper to a Pluggable Auth Service."""

class InlineAuthHelper(Folder, BasePlugin):
    """Multi-plugin for managing details of Inline Authentication."""

    meta_type: str
    zmi_icon: str
    security: Incomplete
    manage_options: Incomplete
    id: Incomplete
    title: Incomplete
    body: Incomplete
    def __init__(self, id, title=None) -> None: ...
    @security.private
    def extractCredentials(self, request):
        """Extract credentials from cookie or 'request'."""
    @security.private
    def challenge(self, request, response, **kw):
        """Challenge the user for credentials."""

BASIC_LOGIN_FORM: str
