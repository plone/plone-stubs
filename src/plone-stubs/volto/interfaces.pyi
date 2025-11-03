from _typeshed import Incomplete
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer

class IPloneVoltoCoreLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""

class IThemeSpecific(IPloneVoltoCoreLayer):
    """bbb for collective.folderishtypes browser interface."""

class IVoltoSettings(Interface):
    """Volto settings necessary to store in the backend"""

    frontend_domain: Incomplete

class IFolderishType(Interface):
    """Marker interface"""

class IFolderishDocument(IFolderishType):
    """Marker interface"""

class IFolderishEvent(IFolderishType):
    """Marker interface"""

class IFolderishNewsItem(IFolderishType):
    """Marker interface"""
