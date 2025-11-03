from _typeshed import Incomplete

import zope.viewlet.viewlet

class ViewletBase(zope.viewlet.viewlet.ViewletBase): ...
class SimpleAttributeViewlet(zope.viewlet.viewlet.SimpleAttributeViewlet): ...

class simple(zope.viewlet.viewlet.simple):
    __init__: Incomplete

def SimpleViewletClass(template, bases=(), attributes=None, name: str = ""):
    """A function that can be used to generate a viewlet from a set of
    information.
    """

class ResourceViewletBase(zope.viewlet.viewlet.ResourceViewletBase): ...

def JavaScriptViewlet(path):
    """Create a viewlet that can simply insert a javascript link."""

class CSSResourceViewletBase(zope.viewlet.viewlet.CSSResourceViewletBase): ...

def CSSViewlet(path, media: str = "all", rel: str = "stylesheet"):
    """Create a viewlet that can simply insert a javascript link."""
