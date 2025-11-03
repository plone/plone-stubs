from _typeshed import Incomplete
from plone.app.layout.viewlets import ViewletBase

class LeadImageViewlet(ViewletBase):
    """plone.app.contenttypes LeadImageViewlet for Occurrence contexts, where
    the image might be defined on the parent object.
    """

    available: Incomplete
    def update(self) -> None: ...
