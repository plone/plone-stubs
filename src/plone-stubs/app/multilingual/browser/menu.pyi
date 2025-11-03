from _typeshed import Incomplete
from plone.memoize import view
from zope.browsermenu.menu import BrowserMenu
from zope.browsermenu.menu import BrowserSubMenuItem

class TranslateMenu(BrowserMenu):
    def getMenuItems(self, context, request):
        """Return menu item entries in a TAL-friendly form."""

class TranslateSubMenuItem(BrowserSubMenuItem):
    title: Incomplete
    description: Incomplete
    submenuId: str
    order: int
    icon: str
    @property
    def action(self): ...
    @property
    def extra(self): ...
    @view.memoize
    def available(self): ...
    def selected(self): ...
