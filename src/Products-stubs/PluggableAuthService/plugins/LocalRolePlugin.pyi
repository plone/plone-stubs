from .BasePlugin import BasePlugin
from _typeshed import Incomplete
from zope.interface import Interface

class ILocalRolePlugin(Interface):
    """Marker interface."""

manage_addLocalRolePluginForm: Incomplete

def addLocalRolePlugin(dispatcher, id, title: str = "", RESPONSE=None) -> None:
    """Add a Local Role Plugin to 'dispatcher'."""

class LocalRolePlugin(BasePlugin):
    """Provide roles during Authentication from local roles
    assignments made on the root object.
    """

    meta_type: str
    zmi_icon: str
    security: Incomplete
    title: Incomplete
    def __init__(self, id, title=None) -> None: ...
    @security.private
    def getRolesForPrincipal(self, principal, request=None):
        """See IRolesPlugin."""
