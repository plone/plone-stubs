from _typeshed import Incomplete
from plone.app.layout.viewlets import ViewletBase

class LeadImageViewlet(ViewletBase):
    """A simple viewlet which renders leadimage"""

    available: Incomplete
    def update(self) -> None: ...
