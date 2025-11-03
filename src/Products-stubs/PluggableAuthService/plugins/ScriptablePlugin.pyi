from .BasePlugin import BasePlugin
from _typeshed import Incomplete
from OFS.Folder import Folder
from zope.interface import Interface

class IScriptablePlugin(Interface):
    """Marker interface."""

manage_addScriptablePluginForm: Incomplete

def addScriptablePlugin(dispatcher, id, title=None, REQUEST=None) -> None:
    """Add a Scriptable Plugin to a Pluggable Auth Service."""

class ScriptablePlugin(Folder, BasePlugin):
    """Allow users to implement plugin interfaces using script objects.

    o Allowable types include ExternalMethods, Python Scripts, ZSQL Methods,
      and DTML methods.

    o Provide UI for creating scripts for known plugin types.
    """

    security: Incomplete
    meta_type: str
    zmi_icon: str
    manage_options: Incomplete
    manage_editInterfacesForm: Incomplete
    def __creatable_by_emergency_user__(self): ...
    title: Incomplete
    def __init__(self, id, title=None) -> None: ...
    def hasMethod(self, method_name):
        """Do we implement this method directly?"""
    @security.public
    def all_meta_types(self):
        """What objects can be contained here?"""
    def manage_updateInterfaces(self, interfaces, RESPONSE=None) -> None:
        """For ZMI update of interfaces."""
