from ..plugins.BasePlugin import BasePlugin
from _typeshed import Incomplete
from OFS.Folder import Folder
from zope.interface import Interface

class IDelegatingMultiPlugin(Interface):
    """Marker interface."""

manage_addDelegatingMultiPluginForm: Incomplete

def manage_addDelegatingMultiPlugin(
    self, id, title: str = "", delegate_path: str = "", REQUEST=None
) -> None:
    """Factory method to instantiate a DelegatingMultiPlugin"""

class DelegatingMultiPlugin(Folder, BasePlugin):
    """The adapter that mediates between the PAS and the DelegatingUserFolder"""

    security: Incomplete
    meta_type: str
    zmi_icon: str
    manage_options: Incomplete
    id: Incomplete
    title: Incomplete
    delegate: Incomplete
    def __init__(self, id, title: str = "", delegate_path: str = "") -> None:
        """Initialize a new instance"""
    @security.private
    def authenticateCredentials(self, credentials):
        """Fulfill AuthenticationPlugin requirements"""
    @security.private
    def updateCredentials(self, request, response, login, new_password) -> None:
        """Fulfill CredentialsUpdatePlugin requirements"""
    @security.private
    def resetCredentials(self, request, response) -> None:
        """Fulfill CredentialsResetPlugin requirements"""
    @security.private
    def getPropertiesForUser(self, user, request=None):
        """Fullfill PropertiesPlugin requirements"""
    @security.private
    def getRolesForPrincipal(self, user, request=None):
        """Fullfill RolesPlugin requirements"""
    @security.private
    def enumerateUsers(
        self,
        id=None,
        login=None,
        exact_match: int = 0,
        sort_by=None,
        max_results=None,
        **kw,
    ):
        """Fulfill the EnumerationPlugin requirements"""
