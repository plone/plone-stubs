import ExtensionClass

def findSite(obj, iface=...):
    """Find a site by walking up the object hierarchy, supporting both
    the ``ILocation`` API and Zope 2 Acquisition."""

def siteManagerAdapter(ob):
    """Look-up a site manager/component registry for local component
    lookup.  This is registered in place of the one in zope.site so that
    we lookup using acquisition in addition to the ``ILocation`` API.
    """

class LocalSiteHook(ExtensionClass.Base):
    def __call__(self, container, request) -> None: ...

HOOK_NAME: str

def enableSite(obj, iface=...) -> None:
    """Install __before_traverse__ hook for Local Site"""

def disableSite(obj, iface=...) -> None:
    """Remove __before_traverse__ hook for Local Site"""
