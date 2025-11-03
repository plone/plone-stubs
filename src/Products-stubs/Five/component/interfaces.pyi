from OFS.interfaces import IObjectManager
from zope.component.interfaces import ISite

class IObjectManagerSite(IObjectManager, ISite):
    """Object manager that is also a site."""
