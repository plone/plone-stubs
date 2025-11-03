from _typeshed import Incomplete
from Products.Five.browser import BrowserView

class DiffView(BrowserView):
    baseline: Incomplete
    working_copy: Incomplete
    def __call__(self): ...
    def diffs(self): ...
