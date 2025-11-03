from _typeshed import Incomplete
from plone.memoize.view import memoize
from Products.Five.browser import BrowserView

class ViewletBase(BrowserView):
    """Base class with common functions for link viewlets."""

    __parent__: Incomplete
    context: Incomplete
    request: Incomplete
    view: Incomplete
    manager: Incomplete
    def __init__(self, context, request, view, manager=None) -> None: ...
    def __hash__(self): ...
    portal_state: Incomplete
    site_url: Incomplete
    navigation_root_url: Incomplete
    def update(self) -> None: ...
    def render(self): ...
    def index(self) -> None: ...
    def __lt__(self, other):
        """Sort by name"""
    def __eq__(self, other):
        """Check for equality"""

class TitleViewlet(ViewletBase):
    index: Incomplete
    sep: str
    @property
    @memoize
    def site_title_setting(self): ...
    @property
    @memoize
    def page_title(self):
        """
        Get the page title. If we are in the portal_factory we want use the
        "Add $FTI_TITLE" form (see #12117).

        NOTE: other implementative options can be:
         - to use "Untitled" instead of "Add" or
         - to check the isTemporary method of the edit view instead of the
           creation_flag
        """
    site_title: Incomplete
    def update(self) -> None: ...

class DublinCoreViewlet(ViewletBase):
    index: Incomplete
    metatags: Incomplete
    def update(self) -> None: ...

class TableOfContentsViewlet(ViewletBase):
    index: Incomplete
    enabled: Incomplete
    def update(self) -> None: ...

class SiteActionsViewlet(ViewletBase):
    index: Incomplete
    site_actions: Incomplete
    def update(self) -> None: ...

class SearchBoxViewlet(ViewletBase):
    index: Incomplete
    livesearch: Incomplete
    show_images: Incomplete
    folder_path: Incomplete
    def update(self) -> None: ...

class LogoViewlet(ViewletBase):
    index: Incomplete
    navigation_root_title: Incomplete
    logo_title: Incomplete
    img_src: Incomplete
    def update(self) -> None: ...

class GlobalSectionsViewlet(ViewletBase):
    index: Incomplete
    registry: Incomplete
    def __init__(self, *args) -> None: ...
    @property
    def settings(self): ...
    @property
    def language_settings(self): ...
    @property
    def navtree_path(self): ...
    @property
    def current_language(self): ...
    @property
    def types_using_view(self): ...
    @property
    @memoize
    def navtree(self): ...
    def customize_query(self, query) -> None:
        """Helper to customize the catalog query."""
    def customize_tab(self, entry, tab) -> None:
        """Helper to add custom entry keys/values."""
    def customize_entry(self, entry, brain) -> None:
        """Helper to add custom entry keys/values."""
    def render_item(self, item, path): ...
    def build_tree(self, path, first_run: bool = True):
        """Non-template based recursive tree building.
        3-4 times faster than template based.
        """
    def render_globalnav(self): ...
    @property
    @memoize
    def portal_tabs(self): ...

class PersonalBarViewlet(ViewletBase):
    homelink_url: str
    user_name: str
    user_actions: Incomplete
    anonymous: Incomplete
    def update(self) -> None: ...

class ContentViewsViewlet(ViewletBase):
    index: Incomplete
    menu_template: Incomplete
    default_tab: str
    primary: Incomplete
    def update(self) -> None: ...
    @memoize
    def getTabSets(self): ...
    def locked_icon(self): ...

class PathBarViewlet(ViewletBase):
    index: Incomplete
    is_rtl: Incomplete
    breadcrumbs: Incomplete
    def update(self) -> None: ...

class TinyLogoViewlet(ViewletBase):
    index: Incomplete
