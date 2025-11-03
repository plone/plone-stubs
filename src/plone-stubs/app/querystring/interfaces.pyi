from _typeshed import Incomplete
from zope.interface import Interface

class IQuerystringRegistryReader(Interface):
    """Adapts a registry object to parse the querystring data"""
    def __call__() -> None:
        """Return query string in dict-format."""

class IQueryOperation(Interface):
    title: Incomplete
    description: Incomplete
    operation: Incomplete
    widget: Incomplete

class IQueryField(Interface):
    title: Incomplete
    description: Incomplete
    enabled: Incomplete
    sortable: Incomplete
    fetch_vocabulary: Incomplete
    operations: Incomplete
    vocabulary: Incomplete
    group: Incomplete

class IParsedQueryIndexModifier(Interface):
    """Transform a parsed query index in something different"""
    def __call__(value) -> None:
        """
        Return a tuple with a new index name and a new value.
        if the index name returned is different from the native one, caller
        must replace treated index with the new ones.
        """

class IQueryModifier(Interface):
    """Modifies a query in order to inject specific or change given criteria."""
    def __call__(query) -> None:
        """
        modify the query and return an new one.
        """
