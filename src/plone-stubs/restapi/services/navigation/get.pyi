from _typeshed import Incomplete
from plone.memoize.view import memoize
from plone.memoize.view import memoize_contextless
from plone.restapi.services import Service

class Navigation:
    context: Incomplete
    request: Incomplete
    portal: Incomplete
    def __init__(self, context, request) -> None: ...
    depth: Incomplete
    def __call__(self, expand: bool = False): ...
    @property
    @memoize_contextless
    def settings(self): ...
    @property
    def default_language(self): ...
    @property
    def navtree_path(self): ...
    @property
    def current_language(self): ...
    @property
    @memoize
    def navtree(self): ...
    def customize_entry(self, entry, brain) -> None:
        """a little helper to add custom entry keys/values."""
    def render_item(self, item, path): ...
    def build_tree(self, path, first_run: bool = True):
        """Non-template based recursive tree building.
        3-4 times faster than template based.
        """
    @property
    @memoize
    def portal_tabs(self): ...

class NavigationGet(Service):
    def reply(self): ...
