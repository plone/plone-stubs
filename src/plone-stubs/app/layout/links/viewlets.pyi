from _typeshed import Incomplete
from plone.app.layout.viewlets import ViewletBase
from plone.memoize import view
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from typing import NoReturn

def get_language(context, request): ...
def render_cachekey(fun, self): ...

class FaviconViewlet(ViewletBase):
    mimetype: str
    favicon_path: str
    def init_favicon(self) -> NoReturn: ...
    def render(self) -> ViewPageTemplateFile: ...

class SearchViewlet(ViewletBase):
    def render(self): ...

class AuthorViewlet(ViewletBase):
    tools: Incomplete
    def update(self) -> None: ...
    def show(self): ...
    def render(self): ...

class RSSViewlet(ViewletBase):
    def getRssLinks(self, obj): ...
    rsslinks: Incomplete
    def update(self) -> None: ...
    index: Incomplete

class CanonicalURL(ViewletBase):
    """Defines a canonical link relation viewlet to be displayed across the
    site. A canonical page is the preferred version of a set of pages with
    highly similar content. For more information, see:
    https://tools.ietf.org/html/rfc6596
    https://support.google.com/webmasters/answer/139394?hl=en
    """
    @view.memoize
    def render(self): ...
