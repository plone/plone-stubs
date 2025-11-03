from zope.browsermenu.menu import BrowserMenu

class DisplayViewsMenu(BrowserMenu):
    def getMenuItemByAction(self, context, request, action): ...
