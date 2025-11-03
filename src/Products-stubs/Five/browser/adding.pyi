from _typeshed import Incomplete
from OFS.SimpleItem import SimpleItem
from Products.Five import BrowserView

class Adding(BrowserView):
    contentName: Incomplete
    def add(self, content):
        """See zope.browser.interfaces.IAdding"""
    def nextURL(self):
        """See zope.browser.interfaces.IAdding"""
    request: Incomplete
    context: Incomplete
    def publishTraverse(self, request, name):
        """See zope.publisher.interfaces.IPublishTraverse"""
    def action(self, type_name: str = "", id: str = "") -> None: ...
    def nameAllowed(self):
        """Return whether names can be input by the user."""
    menu_id: Incomplete
    index: Incomplete
    def addingInfo(self):
        """Return menu data.

        This is sorted by title.
        """
    def isSingleMenuItem(self):
        """Return whether there is single menu item or not."""
    def hasCustomAddView(self):
        """This should be called only if there is `singleMenuItem` else return 0"""

class ContentAdding(Adding, SimpleItem):
    menu_id: str

class ObjectManagerNameChooser:
    """A name chooser for a Zope object manager."""

    context: Incomplete
    def __init__(self, context) -> None: ...
    def checkName(self, name, object) -> None: ...
    def chooseName(self, name, object): ...
