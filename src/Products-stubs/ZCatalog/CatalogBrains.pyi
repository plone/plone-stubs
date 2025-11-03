from Acquisition import Implicit
from Record import Record

class AbstractCatalogBrain(Record, Implicit):
    """Abstract base brain that handles looking up attributes as
    required, and provides just enough smarts to let us get the URL, path,
    and cataloged object without having to ask the catalog directly.
    """
    def has_key(self, key): ...
    def __contains__(self, name) -> bool: ...
    def getPath(self):
        """Get the physical path for this record"""
    def getURL(self, relative: int = 0):
        """Generate a URL for this record"""
    def getObject(self, REQUEST=None):
        """Return the object for this record

        Will return None if the object cannot be found via its cataloged path
        (i.e., it was deleted or moved without recataloging), or if the user is
        not authorized to access the object.

        This method mimicks a subset of what publisher's traversal does,
        so it allows access if the final object can be accessed even
        if intermediate objects cannot.
        """
    def getRID(self):
        """Return the record ID for this object."""

class NoBrainer:
    """This is an empty class to use when no brain is specified."""
