from _typeshed import Incomplete
from plone.batching.browser import BatchView
from plone.memoize import instance
from zope.publisher.browser import BrowserView

_: Incomplete

class TableBatchView(BatchView):
    def make_link(self, pagenumber): ...

class Table:
    """
    The table renders a table with sortable columns etc.

    It is meant to be subclassed to provide methods for getting specific table
    info.
    """

    request: Incomplete
    context: Incomplete
    base_url: Incomplete
    view_url: Incomplete
    url: Incomplete
    items: Incomplete
    show_sort_column: Incomplete
    show_select_column: Incomplete
    show_size_column: Incomplete
    show_modified_column: Incomplete
    show_status_column: Incomplete
    buttons: Incomplete
    default_page_size: int
    pagesize: Incomplete
    show_all: Incomplete
    selectcurrentbatch: bool
    selectall: bool
    pagenumber: Incomplete
    def __init__(
        self,
        request,
        base_url,
        view_url,
        items,
        show_sort_column: bool = False,
        buttons=None,
        pagesize: int = 20,
        show_select_column: bool = True,
        show_size_column: bool = True,
        show_modified_column: bool = True,
        show_status_column: bool = True,
    ) -> None: ...
    def msg_select_item(self, item): ...
    @property
    def within_batch_size(self): ...
    def set_checked(self, item) -> None: ...
    @property
    @instance.memoize
    def batch(self): ...
    render: Incomplete
    def batching(self): ...
    @property
    def show_select_all_items(self): ...
    def get_nosort_class(self):
        """ """
    @property
    def selectall_url(self): ...
    @property
    def selectscreen_url(self): ...
    @property
    def selectnone_url(self): ...
    @property
    def show_all_url(self): ...
    def selected(self, item): ...
    @property
    def viewname(self): ...
    def quote_plus(self, string): ...

class TableBrowserView(BrowserView):
    """Base class which can be used from a AJAX view

    Subclasses only need to set the table property to a different
    class."""

    table: Incomplete
    def update_table(
        self,
        pagenumber: str = "1",
        sort_on: str = "getObjPositionInParent",
        show_all: bool = False,
    ): ...
