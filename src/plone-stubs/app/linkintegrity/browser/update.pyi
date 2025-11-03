from _typeshed import Incomplete
from Products.Five import BrowserView

logger: Incomplete

class UpdateView(BrowserView):
    """Iterate over all catalogued items and update linkintegrity-information."""
    def __call__(self): ...
    def update(self): ...
