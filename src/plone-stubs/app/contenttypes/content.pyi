from _typeshed import Incomplete
from plone.dexterity.content import Container
from plone.dexterity.content import Item

class Collection(Item):
    """Convenience subclass for ``Collection`` portal type"""

    security: Incomplete
    def listMetaDataFields(self, exclude: bool = True):
        """Return a list of all metadata fields from portal_catalog.

        This is no longer used.  We use a vocabulary instead.
        """
    def selectedViewFields(self):
        """Returns a list of all metadata fields from the catalog that were
        selected.
        """
    query: Incomplete
    def setQuery(self, query) -> None: ...
    def getQuery(self):
        """Return the query as a list of dict; note that this method
        returns a list of CatalogContentListingObject in
        Products.ATContentTypes.
        """
    def getRawQuery(self): ...
    sort_on: Incomplete
    def setSort_on(self, sort_on) -> None: ...
    sort_reversed: Incomplete
    def setSort_reversed(self, sort_reversed) -> None: ...
    def queryCatalog(
        self, batch: bool = True, b_start: int = 0, b_size: int = 30, sort_on=None
    ): ...
    def results(self, **kwargs): ...

class Document(Item):
    """Convenience subclass for ``Document`` portal type"""

    security: Incomplete
    def Format(self):
        """Provide a proper accessor for the format attribute
        See https://github.com/plone/Products.CMFPlone/issues/2540
        """

class File(Item):
    """Convenience subclass for ``File`` portal type"""

    security: Incomplete
    file: Incomplete
    def PUT(self, REQUEST=None, RESPONSE=None):
        """DAV method to replace the file field with a new resource."""
    def get_size(self): ...
    def content_type(self): ...

class Folder(Container):
    """Convenience subclass for ``Folder`` portal type"""

class Image(Item):
    """Convenience subclass for ``Image`` portal type"""

    security: Incomplete
    image: Incomplete
    def PUT(self, REQUEST=None, RESPONSE=None):
        """DAV method to replace image field with a new resource."""
    def get_size(self): ...
    def content_type(self): ...

class Link(Item):
    """Convenience subclass for ``Link`` portal type"""

class NewsItem(Item):
    """Convenience subclass for ``News Item`` portal type"""

class Event(Item):
    """Convenience subclass for ``Event`` portal type"""
