from plone.memoize.instance import memoize
from zope.publisher.browser import BrowserView

class FolderFactoriesView(BrowserView):
    """The folder_factories view - show addable types"""
    def __call__(self): ...
    def can_constrain_types(self): ...
    @memoize
    def add_context(self): ...
    def addable_types(self, include=None):
        """Return menu item entries in a TAL-friendly form.

        Pass a list of type ids to 'include' to explicitly allow a list of
        types.
        """
