from _typeshed import Incomplete
from Acquisition import Implicit
from OFS.SimpleItem import Item
from Persistence import Persistent
from ZPublisher import zpublish

class VirtualHostMonster(Persistent, Item, Implicit):
    """Provide a simple drop-in solution for virtual hosting."""

    meta_type: str
    zmi_icon: str
    zmi_show_add_dialog: bool
    priority: int
    id: str
    title: str
    lines: Incomplete
    have_map: int
    security: Incomplete
    manage_options: Incomplete
    manage_main: Incomplete
    manage_edit: Incomplete
    fixed_map: Incomplete
    sub_map: Incomplete
    @zpublish
    def set_map(self, map_text, RESPONSE=None) -> None:
        """Set domain to path mappings."""
    def addToContainer(self, container) -> None: ...
    def manage_addToContainer(self, container, nextURL: str = "") -> None: ...
    def manage_beforeDelete(self, item, container) -> None: ...
    def manage_afterAdd(self, item, container) -> None: ...
    def __call__(self, client, request, response=None) -> None:
        """Traversing at home"""
    def __bobo_traverse__(self, request, name):
        """Traversing away"""

def manage_addVirtualHostMonster(self, id=None, REQUEST=None, **ignored) -> None:
    """ """

constructors: Incomplete
