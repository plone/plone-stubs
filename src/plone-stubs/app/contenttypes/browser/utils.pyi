from plone.memoize.view import memoize
from Products.Five.browser import BrowserView
from zope.interface import Interface

PREFIX: str

class IUtils(Interface):
    """ """
    def getMimeTypeIcon(content_file) -> None:
        """ """

class Utils(BrowserView):
    @memoize
    def getMimeTypeIcon(self, content_file): ...
