from _typeshed import Incomplete
from zope.viewlet.manager import ViewletManagerBase as origManagerBase

class ViewletManagerBase(origManagerBase):
    """A base class for Viewlet managers to work in Zope2"""

    template: Incomplete
    def __getitem__(self, name):
        """See zope.interface.common.mapping.IReadMapping"""
    def filter(self, viewlets):
        """Sort out all content providers

        ``viewlets`` is a list of tuples of the form (name, viewlet).
        """
    def sort(self, viewlets):
        """Sort the viewlets.

        ``viewlets`` is a list of tuples of the form (name, viewlet).
        """

def ViewletManager(name, interface, template=None, bases=()): ...
