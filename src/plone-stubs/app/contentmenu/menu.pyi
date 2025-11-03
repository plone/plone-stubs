from _typeshed import Incomplete
from plone.app.contentmenu import PloneMessageFactory as _
from plone.memoize.instance import memoize
from zope.browsermenu.menu import BrowserMenu
from zope.browsermenu.menu import BrowserSubMenuItem

PMF = _

class ActionsSubMenuItem(BrowserSubMenuItem):
    title: Incomplete
    description: Incomplete
    submenuId: str
    icon: str
    order: int
    extra: Incomplete
    context_state: Incomplete
    def __init__(self, context, request) -> None: ...
    @property
    def action(self): ...
    @memoize
    def available(self): ...
    def selected(self): ...

class ActionsMenu(BrowserMenu):
    def getMenuItems(self, context, request):
        """Return menu item entries in a TAL-friendly form."""

class DisplaySubMenuItem(BrowserSubMenuItem):
    title: Incomplete
    submenuId: str
    icon: str
    order: int
    context_state: Incomplete
    def __init__(self, context, request) -> None: ...
    @property
    def extra(self): ...
    @property
    def description(self): ...
    @property
    def action(self): ...
    @memoize
    def available(self): ...
    def selected(self): ...
    @memoize
    def disabled(self): ...

class DisplayMenu(BrowserMenu):
    def getMenuItems(self, obj, request):
        """Return menu item entries in a TAL-friendly form."""

class FactoriesSubMenuItem(BrowserSubMenuItem):
    title: Incomplete
    submenuId: str
    icon: str
    order: int
    description: Incomplete
    context_state: Incomplete
    def __init__(self, context, request) -> None: ...
    @property
    def extra(self): ...
    @property
    def action(self): ...
    def available(self): ...
    def selected(self): ...

class FactoriesMenu(BrowserMenu):
    def getMenuItems(self, context, request):
        """Return menu item entries in a TAL-friendly form."""

class WorkflowSubMenuItem(BrowserSubMenuItem):
    MANAGE_SETTINGS_PERMISSION: str
    title: Incomplete
    short_title: Incomplete
    icon: str
    submenuId: str
    order: int
    tools: Incomplete
    context: Incomplete
    context_state: Incomplete
    def __init__(self, context, request) -> None: ...
    @property
    def extra(self): ...
    @property
    def description(self): ...
    @property
    def action(self): ...
    @memoize
    def available(self): ...
    def selected(self): ...

class WorkflowMenu(BrowserMenu):
    BOGUS_WORKFLOW_ACTIONS: Incomplete
    def getMenuItems(self, context, request):
        """Return menu item entries in a TAL-friendly form."""

class PortletManagerSubMenuItem(BrowserSubMenuItem):
    MANAGE_SETTINGS_PERMISSION: str
    title: Incomplete
    submenuId: str
    icon: str
    order: int
    context: Incomplete
    context_state: Incomplete
    def __init__(self, context, request) -> None: ...
    @property
    def extra(self): ...
    @property
    def description(self): ...
    @property
    def action(self): ...
    @memoize
    def available(self): ...
    def selected(self): ...

class PortletManagerMenu(BrowserMenu):
    def getMenuItems(self, context, request):
        """Return menu item entries in a TAL-friendly form."""
