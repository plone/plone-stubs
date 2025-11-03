from _typeshed import Incomplete
from zope.container.btree import BTreeContainer
from zope.container.contained import Contained
from zope.container.ordered import OrderedContainer

LOG: Incomplete

class PortletStorage(BTreeContainer):
    """The default portlet storage."""

class PortletCategoryMapping(BTreeContainer, Contained):
    """The default category/key mapping storage."""
    def __getitem__(self, key): ...
    def get(self, key, default=None):
        """See interface `IReadContainer`"""
    def __contains__(self, key) -> bool:
        """See interface `IReadContainer`"""
    has_key = __contains__
    def __setitem__(self, key, object) -> None:
        """See interface `IWriteContainer`"""
    def __delitem__(self, key) -> None:
        """See interface `IWriteContainer`"""

class PortletAssignmentMapping(OrderedContainer):
    """The default assignment mapping storage."""

    __manager__: str
    __category__: str
    def __init__(
        self, manager: str = "", category: str = "", name: str = ""
    ) -> None: ...
