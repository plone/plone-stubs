from _typeshed import Incomplete
from plone.memoize.view import memoize
from Products.Five import BrowserView

class ExceptionView(BrowserView):
    basic_template: Incomplete
    def is_manager(self): ...
    @property
    @memoize
    def plone_redirector_view(self): ...
    context: Incomplete
    def __call__(self): ...
