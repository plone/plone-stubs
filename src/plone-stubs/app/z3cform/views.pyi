from _typeshed import Incomplete
from Products.Five.browser import BrowserView
from Products.Five.browser.metaconfigure import ViewMixinForTemplates

def path(filepart): ...

layout_factory: Incomplete
form_factory: Incomplete

class Macros(BrowserView):
    def __getitem__(self, key): ...

class RenderWidget(ViewMixinForTemplates, BrowserView):
    index: Incomplete

class RenderContentProvider(ViewMixinForTemplates, BrowserView):
    index: Incomplete

ErrorViewTemplate: Incomplete
