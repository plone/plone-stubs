from _typeshed import Incomplete
from zope.cachedescriptors.property import Lazy as lazy_property
from zope.publisher.browser import BrowserView

_: Incomplete
MULTISPACE: str
BAD_CHARS: Incomplete
EVER: Incomplete

def quote_chars(s): ...
def quote(term): ...
def munge_search_term(query): ...

class Search(BrowserView):
    valid_keys: Incomplete
    def results(
        self,
        query=None,
        batch: bool = True,
        b_size: int = 10,
        b_start: int = 0,
        use_content_listing: bool = True,
    ):
        """Get properly wrapped search results from the catalog.
        Everything in Plone that performs searches should go through this view.
        'query' should be a dictionary of catalog parameters.
        """
    @lazy_property
    def default_sort_on(self): ...
    def filter_query(self, query): ...
    def filter_types(self, types): ...
    def types_list(self): ...
    def sort_options(self):
        """Sorting options for search results view."""
    def show_advanced_search(self):
        """Whether we need to show advanced search options a.k.a. filters?"""
    def advanced_search_trigger(self):
        """URL builder for show/close advanced search filters."""
    def breadcrumbs(self, item): ...
    def navroot_url(self): ...
    @property
    def show_images(self): ...
    @property
    def search_image_scale(self): ...

class AjaxSearch(Search):
    image_scaling: Incomplete
    def __call__(self): ...
    def get_image_tag(self, item, image_scale): ...

class SortOption:
    request: Incomplete
    title: Incomplete
    sortkey: Incomplete
    reverse: Incomplete
    def __init__(
        self, request, title, sortkey: str = "", reverse: bool = False
    ) -> None: ...
    def selected(self): ...
    def url(self): ...
