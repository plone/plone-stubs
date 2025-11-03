from _typeshed import Incomplete
from plone.portlets.storage import PortletStorage

logger: Incomplete

class PortletManagerRenderer:
    """Default renderer for portlet managers.

    When the zope.contentprovider handler for the provider: expression looks up
    a name, context, it will find an adapter factory that in turn finds an
    instance of this class, by doing an adapter lookup for (context, request,
    view, manager).
    """

    template: Incomplete
    error_message: Incomplete
    __parent__: Incomplete
    manager: Incomplete
    context: Incomplete
    request: Incomplete
    def __init__(self, context, request, view, manager) -> None: ...
    @property
    def visible(self): ...
    def filter(self, portlets): ...
    def portletsToShow(self): ...
    def allPortlets(self): ...
    def update(self) -> None: ...
    def render(self): ...
    def safe_render(self, portlet_renderer): ...

class PortletManager(PortletStorage):
    """Default implementation of the portlet manager.

    Provides the functionality that allows the portlet manager to act as an
    adapter factory.
    """

    __parent__: Incomplete
    def __call__(self, context, request, view): ...
    def getAddablePortletTypes(self): ...
