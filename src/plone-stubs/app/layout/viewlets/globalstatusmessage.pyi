from _typeshed import Incomplete
from plone.app.layout.viewlets.common import ViewletBase

_: Incomplete
MTYPES_DISPLAY: Incomplete

class GlobalStatusMessage(ViewletBase):
    """Display messages to the current user"""

    index: Incomplete
    status: Incomplete
    messages: Incomplete
    def update(self) -> None: ...
    def display_info_for_mtype(self, mtype):
        """get info for display of an mtype"""
