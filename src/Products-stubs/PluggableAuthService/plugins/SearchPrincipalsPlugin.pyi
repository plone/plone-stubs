from ..plugins.BasePlugin import BasePlugin
from _typeshed import Incomplete
from zope.interface import Interface

class ISearchPrincipalsPlugin(Interface):
    """Marker interface."""

addSearchPrincipalsPluginForm: Incomplete

def addSearchPrincipalsPlugin(
    dispatcher, id, title: str = "", delegate_path: str = "", REQUEST=None
) -> None:
    """Factory method to instantiate a SearchPrincipalsPlugin"""

class SearchPrincipalsPlugin(BasePlugin):
    """SearchPrincipalsPlugin delegates its enumerateUsers
    and enumerateGroups methods to a delegate object
    """

    security: Incomplete
    meta_type: str
    zmi_icon: str
    id: Incomplete
    title: Incomplete
    delegate: Incomplete
    def __init__(self, id, title: str = "", delegate_path: str = "") -> None:
        """Initialize a new instance"""
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
        """see IUserEnumerationPlugin"""
    @security.private
    def enumerateGroups(
        self, id=None, exact_match: int = 0, sort_by=None, max_results=None, **kw
    ):
        """see IGroupEnumerationPlugin"""
