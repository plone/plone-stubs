from ..portlets import base
from _typeshed import Incomplete
from plone.memoize.instance import memoize
from plone.portlets.interfaces import IPortletDataProvider
from Products.CMFPlone.browser.navtree import SitemapNavtreeStrategy

class INavigationPortlet(IPortletDataProvider):
    """A portlet which can render the navigation tree"""

    name: Incomplete
    root_uid: Incomplete
    includeTop: Incomplete
    currentFolderOnly: Incomplete
    topLevel: Incomplete
    bottomLevel: Incomplete
    no_icons: Incomplete
    thumb_scale: Incomplete
    no_thumbs: Incomplete

class Assignment(base.Assignment):
    name: str
    root: Incomplete
    root_uid: Incomplete
    currentFolderOnly: bool
    includeTop: bool
    topLevel: int
    bottomLevel: int
    no_icons: bool
    thumb_scale: Incomplete
    no_thumbs: bool
    def __init__(
        self,
        name: str = "",
        root_uid=None,
        currentFolderOnly: bool = False,
        includeTop: bool = False,
        topLevel: int = 1,
        bottomLevel: int = 0,
        no_icons: bool = False,
        thumb_scale=None,
        no_thumbs: bool = False,
    ) -> None: ...
    @property
    def title(self):
        """
        Display the name in portlet mngmt interface
        """

class Renderer(base.Renderer):
    urltool: Incomplete
    def __init__(self, context, request, view, manager, data) -> None: ...
    def title(self): ...
    def hasName(self): ...
    @property
    def available(self): ...
    def include_top(self): ...
    def navigation_root(self): ...
    def heading_link_target(self):
        """
        Get the href target where clicking the portlet header will take you.

        If this is a customized portlet with a custom root item set,
        we probably want to take the user to the custom root item instead
        of the sitemap of the navigation root.

        Plone does not have subsection sitemaps so there is no point of
        displaying /sitemap links for anything besides nav root.
        """
    def root_type_name(self): ...
    def root_item_class(self): ...
    def root_is_portal(self): ...
    def createNavTree(self): ...
    @memoize
    def getNavRootPath(self): ...
    @memoize
    def getNavRoot(self, _marker=None): ...
    @memoize
    def getNavTree(self, _marker=None): ...
    recurse: Incomplete
    @memoize
    def thumb_scale(self):
        """Use override value or read thumb_scale from registry.
        Image sizes must fit to value in allowed image sizes.
        None will suppress thumb.
        """
    def update(self) -> None: ...
    def render(self): ...

class AddForm(base.AddForm):
    schema = INavigationPortlet
    label: Incomplete
    description: Incomplete
    def create(self, data): ...

class EditForm(base.EditForm):
    schema = INavigationPortlet
    label: Incomplete
    description: Incomplete

class QueryBuilder:
    """Build a navtree query based on the settings in INavigationSchema
    and those set on the portlet.
    """

    context: Incomplete
    portlet: Incomplete
    query: Incomplete
    def __init__(self, context, portlet) -> None: ...
    def __call__(self): ...

class NavtreeStrategy(SitemapNavtreeStrategy):
    """The navtree strategy used for the default navigation portlet"""

    bottomLevel: Incomplete
    rootPath: Incomplete
    def __init__(self, context, portlet) -> None: ...
    def subtreeFilter(self, node): ...

def getRootPath(context, currentFolderOnly, topLevel, root):
    """Helper function to calculate the real root path"""
