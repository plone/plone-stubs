from .BasePlugin import BasePlugin
from _typeshed import Incomplete
from zope.interface import Interface

class IRecursiveGroupsPlugin(Interface):
    """Marker interface."""

manage_addRecursiveGroupsPluginForm: Incomplete

def addRecursiveGroupsPlugin(dispatcher, id, title=None, REQUEST=None) -> None:
    """Add a RecursiveGroupsPlugin to a Pluggable Auth Service."""

class SimpleGroup:
    def __init__(self, id) -> None: ...
    def getId(self): ...
    def getGroups(self): ...

class RecursiveGroupsPlugin(BasePlugin):
    """PAS plugin for recursively flattening a collection of groups"""

    meta_type: str
    zmi_icon: str
    security: Incomplete
    title: Incomplete
    def __init__(self, id, title=None) -> None: ...
    @security.private
    def getGroupsForPrincipal(self, user, request=None): ...
