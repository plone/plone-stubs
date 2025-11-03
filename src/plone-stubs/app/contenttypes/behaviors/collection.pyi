from _typeshed import Incomplete
from plone.base.interfaces.syndication import ISyndicatable
from plone.supermodel import model
from Products.CMFPlone.browser.syndication.adapters import (
    CollectionFeed as BaseCollectionFeed,
)

class ICollection(model.Schema):
    query: Incomplete
    sort_on: Incomplete
    sort_reversed: Incomplete
    limit: Incomplete
    item_count: Incomplete
    customViewFields: Incomplete

class ISyndicatableCollection(ISyndicatable):
    """Marker interface for syndicatable collections."""

class Collection:
    context: Incomplete
    def __init__(self, context) -> None: ...
    def results(
        self,
        batch: bool = True,
        b_start: int = 0,
        b_size=None,
        sort_on=None,
        limit=None,
        brains: bool = False,
        custom_query=None,
    ): ...
    def selectedViewFields(self):
        """Returns a list of all metadata fields from the catalog that were
           selected.

        The template expects a tuple/list of (id, title) of the field.

        """
    @property
    def sort_reversed(self): ...
    @sort_reversed.setter
    def sort_reversed(self, value) -> None: ...
    @property
    def item_count(self): ...
    @item_count.setter
    def item_count(self, value) -> None: ...
    @property
    def sort_on(self): ...
    @sort_on.setter
    def sort_on(self, value) -> None: ...
    @property
    def limit(self): ...
    @limit.setter
    def limit(self, value) -> None: ...
    @property
    def query(self): ...
    @query.setter
    def query(self, value) -> None: ...
    @property
    def customViewFields(self): ...
    @customViewFields.setter
    def customViewFields(self, value) -> None: ...

class CollectionFeed(BaseCollectionFeed): ...
