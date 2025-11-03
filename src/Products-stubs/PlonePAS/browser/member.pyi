from plone.memoize.instance import memoize
from zope.publisher.browser import BrowserView

class PASMemberView(BrowserView):
    @memoize
    def info(self, userid=None): ...
    def __call__(self) -> None: ...
