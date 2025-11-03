from zope.browsermenu.interfaces import IBrowserMenu
from zope.browsermenu.interfaces import IBrowserSubMenuItem
from zope.contentprovider.interfaces import IContentProvider
from zope.interface import Interface

class IContentMenuView(IContentProvider):
    """The view that powers the content menu in the toolbar.

    This will construct a menu by finding an adapter to IContentMenu.
    """
    def available() -> None:
        """Determine whether the menu should be displayed at all."""
    def menu() -> None:
        """Create a list of dicts that can be used to render a menu.

        The keys in this dict are: title, description, action (a URL),
        selected (a boolean), icon (a URI), extra (a random payload), and
        submenu
        """

class IContentMenuItem(Interface):
    """Special menu item type for Plone's content menu."""

class IActionsSubMenuItem(IBrowserSubMenuItem):
    """The menu item linking to the actions menu."""

class IActionsMenu(IBrowserMenu):
    """The actions menu.

    This gets its menu items from portal_actions.
    """

class IDisplaySubMenuItem(IBrowserSubMenuItem):
    """The menu item linking to the display menu."""
    def disabled(self) -> None:
        """Find out if the menu is visible but disabled."""

class IDisplayMenu(IBrowserMenu):
    """The display menu.

    This gets its menu items from an IBrowserDefault (see CMFDynamicViewFTI).
    """

class IFactoriesSubMenuItem(IBrowserSubMenuItem):
    """The menu item linking to the factories menu."""

class IFactoriesMenu(IBrowserMenu):
    """The factories menu.

    This gets its menu items from portal_types' list of addable types in
    the context.
    """

class IWorkflowSubMenuItem(IBrowserSubMenuItem):
    """The menu item linking to the workflow menu."""

class IWorkflowMenu(IBrowserMenu):
    """The workflow menu.

    This gets its menu items from the list of possible transitions in
    portal_workflow.
    """

class IPortletManagerSubMenuItem(IBrowserSubMenuItem):
    """The menu item linking to the portlet manager menu."""

class IPortletManagerMenu(IBrowserMenu):
    """The portlet manager menu.

    This gets its menu items from the list of possible portlet managers.
    """

class IDisplayViewsMenu(IBrowserMenu):
    """A menu listing Zope3 views registered as content views

    Currently used only to register user-visible titles.
    """
    def getMenuItemByAction(object, request, action) -> None:
        """Return the first IBrowserMenuItem for the given action"""
