from _typeshed import Incomplete
from plone.app.theming.interfaces import THEME_RESOURCE_NAME
from plone.resource.traversal import ResourceTraverser

class ThemeTraverser(ResourceTraverser):
    """The theme traverser.

    Allows traversal to /++theme++<name> using ``plone.resource`` to fetch
    things stored either on the filesystem or in the ZODB.
    """

    name = THEME_RESOURCE_NAME
    context: Incomplete
    def __init__(self, context, request=None) -> None: ...
    def current_theme(self): ...
    def traverse(self, name, remaining): ...
