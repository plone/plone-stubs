from _typeshed import Incomplete
from plone.app.layout.navigation.navtree import NavtreeStrategyBase

security: Incomplete

class NavtreeQueryBuilder:
    """Build a navtree query based on the settings in navtree_properties"""

    registry: Incomplete
    query: Incomplete
    def __init__(self, context) -> None: ...
    def __call__(self): ...

class SitemapQueryBuilder(NavtreeQueryBuilder):
    """Build a folder tree query suitable for a sitemap"""
    def __init__(self, context) -> None: ...

class SitemapNavtreeStrategy(NavtreeStrategyBase):
    """The navtree building strategy used by the sitemap, based on
    navtree_properties
    """

    context: Incomplete
    portal: Incomplete
    parentTypesNQ: Incomplete
    viewActionTypes: Incomplete
    showAllParents: bool
    rootPath: Incomplete
    memberId: Incomplete
    def __init__(self, context, view=None) -> None: ...
    def nodeFilter(self, node): ...
    def subtreeFilter(self, node): ...
    def decoratorFactory(self, node): ...
    def showChildrenOf(self, object): ...

class DefaultNavtreeStrategy(SitemapNavtreeStrategy):
    """The navtree strategy used for the default navigation portlet"""

    rootPath: Incomplete
    def __init__(self, context, view=None) -> None: ...
    def subtreeFilter(self, node): ...
