from _typeshed import Incomplete
from Products.Five import BrowserView

class FolderView(BrowserView):
    plone_view: Incomplete
    portal_state: Incomplete
    pas_member: Incomplete
    b_size: Incomplete
    b_start: Incomplete
    def __init__(self, context, request) -> None: ...
    def results(self, **kwargs):
        """Return a content listing based result set with contents of the
        folder.

        :param **kwargs: Any keyword argument, which can be used for catalog
                         queries.
        :type  **kwargs: keyword argument

        :returns: plone.app.contentlisting based result set.
        :rtype: ``plone.app.contentlisting.interfaces.IContentListing`` based
                sequence.
        """
    def batch(self): ...
    def normalizeString(self, text): ...
    def toLocalizedTime(self, time, long_format=None, time_only=None): ...
    @property
    def friendly_types(self): ...
    @property
    def isAnon(self): ...
    @property
    def navigation_root_url(self): ...
    @property
    def use_view_action(self): ...
    @property
    def show_about(self): ...
    @property
    def no_items_message(self): ...
