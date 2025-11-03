from _typeshed import Incomplete
from plone.app.layout.viewlets import ViewletBase
from Products.Five.browser import BrowserView

class NextPreviousView(BrowserView):
    """Information about next/previous navigation"""
    def next(self): ...
    def previous(self): ...
    def enabled(self): ...
    def isViewTemplate(self): ...

class NextPreviousViewlet(ViewletBase, NextPreviousView):
    index: Incomplete

class NextPreviousLinksViewlet(ViewletBase, NextPreviousView):
    index: Incomplete
