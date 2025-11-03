from _typeshed import Incomplete
from collections import UserDict
from plone.memoize.instance import memoize
from plone.restapi.services import Service
from Products.CMFPlone.browser.navtree import SitemapNavtreeStrategy
from zope.interface import Interface

_: Incomplete

class INavigationPortlet(Interface):
    """A portlet which can render the navigation tree"""

    name: Incomplete
    root_path: Incomplete
    includeTop: Incomplete
    currentFolderOnly: Incomplete
    topLevel: Incomplete
    bottomLevel: Incomplete
    no_icons: Incomplete
    thumb_scale: Incomplete
    no_thumbs: Incomplete

class ContextNavigationGet(Service):
    def reply(self): ...

class ContextNavigation:
    context: Incomplete
    request: Incomplete
    def __init__(self, context, request) -> None: ...
    def __call__(
        self, expand: bool = False, prefix: str = "expand.contextnavigation."
    ): ...
    def getNavTree(self): ...

class NavigationPortletRenderer:
    context: Incomplete
    request: Incomplete
    data: Incomplete
    urltool: Incomplete
    def __init__(self, context, request, data) -> None: ...
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
    @memoize
    def thumb_scale(self):
        """Use override value or read thumb_scale from registry.
        Image sizes must fit to value in allowed image sizes.
        None will suppress thumb.
        """
    def getMimeTypeIcon(self, node): ...
    def render(self): ...
    def recurse(self, children, level, bottomLevel): ...

def get_url(item): ...
def get_id(item): ...
def get_view_url(context): ...
def getRootPath(context, currentFolderOnly, topLevel, root_path):
    """Helper function to calculate the real root path"""

class Data(UserDict):
    def __getattr__(self, name): ...

def extract_data(schema, raw_data, prefix): ...
def get_root(context, root_path): ...

class QueryBuilder:
    """Build a navtree query based on the settings in INavigationSchema
    and those set on the portlet.
    """

    context: Incomplete
    data: Incomplete
    query: Incomplete
    def __init__(self, context, data) -> None: ...
    def __call__(self): ...

class NavtreeStrategy(SitemapNavtreeStrategy):
    """The navtree strategy used for the default navigation portlet"""

    viewActionTypes: Incomplete
    bottomLevel: Incomplete
    rootPath: Incomplete
    def __init__(self, context, portlet) -> None: ...
    def subtreeFilter(self, node): ...
    def decoratorFactory(self, node): ...
