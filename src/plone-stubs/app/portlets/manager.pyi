from _typeshed import Incomplete
from Acquisition import Explicit
from plone.portlets.manager import PortletManagerRenderer as BasePortletManagerRenderer

logger: Incomplete

class PortletManagerRenderer(BasePortletManagerRenderer, Explicit):
    """A Zope 2 implementation of the default PortletManagerRenderer"""

class ColumnPortletManagerRenderer(PortletManagerRenderer):
    """A renderer for the column portlets"""

    template: Incomplete
    error_message: Incomplete
    def base_url(self):
        """If context is a default-page, return URL of folder, else
        return URL of context.
        """
    def safe_render(self, portlet_renderer): ...

class DashboardPortletManagerRenderer(ColumnPortletManagerRenderer):
    """Render a column of the dashboard"""

    template: Incomplete
