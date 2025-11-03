from _typeshed import Incomplete
from collections.abc import Generator
from plone.batching.browser import PloneBatchView
from plone.memoize.view import memoize
from Products.Five.browser import BrowserView

_: Incomplete
logger: Incomplete

def absolutize_path(path, is_source: bool = True):
    """Create path including the path of the portal root.

    The path must be absolute, so starting with a slash.
    Or it can be a full url.

    If is_source is true, this is an alternative url
    that will point to a target (unknown here).

    If is_source is true, path is the path of a target.
    An object must exist at this path, unless it is a full url.

    Return a 2-tuple: (absolute redirection path,
    an error message if something goes wrong and otherwise '').
    """

class RedirectsView(BrowserView):
    def redirects(self) -> Generator[Incomplete]: ...
    def edit_for_navigation_root(self, redirection): ...
    def __call__(self): ...
    @memoize
    def view_url(self): ...

class RedirectionSet:
    supports_date_range_filtering: bool
    storage: Incomplete
    portal_path: Incomplete
    portal_path_len: Incomplete
    data: Incomplete
    def __init__(
        self,
        query: str = "",
        created: str = "",
        manual: str = "",
        start: str = "",
        end: str = "",
    ) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, item): ...

class RedirectsBatchView(PloneBatchView):
    def make_link(self, pagenumber=None, omit_params=None): ...

class RedirectsControlPanel(BrowserView):
    def batching(self): ...
    @memoize
    def redirects(self):
        """Get existing redirects from the redirection storage.
        Return dict with the strings redirect, path and redirect-to.
        Strip the id of the instance from path and redirect-to if
        it is present. (Seems to be always true)
        If id of instance is not present in path the var 'path' and
        'redirect' are equal.
        """
    csv_errors: Incomplete
    form_errors: Incomplete
    def __call__(self): ...
    def add(self, redirection, target, portal, storage, status):
        """Add the redirections from the form. If anything goes wrong, do nothing.

        Returns error message or nothing.
        """
    def upload(self, file, portal, storage, status) -> None:
        """Add the redirections from the CSV file `file`. If anything goes wrong, do nothing."""
    def download(self):
        """Download all redirects as CSV.

        We save to a temporary file and try to stream it as a blob:
        with one million redirects you easily get 30 MB, which is slow as non-blob.
        """
    @memoize
    def view_url(self): ...
