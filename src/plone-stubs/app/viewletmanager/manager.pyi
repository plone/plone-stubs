from _typeshed import Incomplete
from Products.Five import BrowserView

logger: Incomplete

class BaseOrderedViewletManager:
    def filter(self, viewlets):
        """Filter the viewlets.

        ``viewlets`` is a list of tuples of the form (name, viewlet).

        This filters the viewlets just like Five, but also filters out
        viewlets by name from the local utility which implements the
        IViewletSettingsStorage interface.
        """
    def sort(self, viewlets):
        """Sort the viewlets.

        ``viewlets`` is a list of tuples of the form (name, viewlet).

        This sorts the viewlets by the order looked up from the local utility
        which implements the IViewletSettingsStorage interface. The remaining
        ones are sorted just like Five does it.
        """
    def render(self): ...

class OrderedViewletManager(BaseOrderedViewletManager):
    manager_template: Incomplete
    name: Incomplete
    normalized_name: Incomplete
    interface: Incomplete
    def render(self):
        """See zope.contentprovider.interfaces.IContentProvider"""

class ManageViewlets(BrowserView):
    def show(self, manager, viewlet) -> None: ...
    def hide(self, manager, viewlet) -> None: ...
    def moveAbove(self, manager, viewlet, dest) -> None: ...
    def moveBelow(self, manager, viewlet, dest) -> None: ...
    def __call__(self): ...
