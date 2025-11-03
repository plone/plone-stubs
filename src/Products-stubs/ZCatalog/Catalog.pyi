from _typeshed import Incomplete
from Persistence import Persistent
from Products.ZCatalog.CatalogBrains import AbstractCatalogBrain
from ZTUtils.Lazy import LazyMap

import Acquisition
import ExtensionClass

LOG: Incomplete

class CatalogError(Exception): ...

class Catalog(Persistent, Acquisition.Implicit, ExtensionClass.Base):
    """An Object Catalog

    An Object Catalog maintains a table of object metadata, and a
    series of manageable indexes to quickly search for objects
    (references in the metadata) that satisfy a search query.

    This class is not Zope specific, and can be used in any python
    program to build catalogs of objects.  Note that it does require
    the objects to be Persistent, and thus must be used with ZODB3.
    """

    schema: Incomplete
    names: Incomplete
    indexes: Incomplete
    def __init__(self, vocabulary=None, brains=None) -> None: ...
    def __len__(self) -> int: ...
    data: Incomplete
    uids: Incomplete
    paths: Incomplete
    def clear(self) -> None:
        """clear catalog"""
    def updateBrains(self) -> None: ...
    def __getitem__(self, index):
        """
        Returns instances of self._v_brains, or whatever is passed
        into self.useBrains.
        """
    def useBrains(self, brains) -> None:
        """Sets up the Catalog to return an object (ala ZTables) that
        is created on the fly from the tuple stored in the self.data
        Btree.
        """
    def addColumn(self, name, default_value=None, threshold: int = 10000) -> None:
        """Adds a row to the meta data schema"""
    def delColumn(self, name, threshold: int = 10000) -> None:
        """Deletes a row from the meta data schema"""
    def addIndex(self, name, index_type) -> None:
        """Create a new index, given a name and a index_type.

        Old format: index_type was a string, 'FieldIndex' 'TextIndex' or
        'KeywordIndex' is no longer valid; the actual index must be
        instantiated and passed in to addIndex.

        New format: index_type is the actual index object to be stored.
        """
    def delIndex(self, name) -> None:
        """deletes an index"""
    def getIndex(self, name):
        """get an index wrapped in the catalog"""
    def updateMetadata(self, object, uid, index):
        """Given an object and a uid, update the column data for the
        uid with the object data iff the object has changed"""
    def catalogObject(
        self, object, uid, threshold=None, idxs=None, update_metadata: bool = True
    ):
        """
        Adds an object to the Catalog by iteratively applying it to
        all indexes.

        'object' is the object to be cataloged

        'uid' is the unique Catalog identifier for this object

        If 'idxs' is specified (as a sequence), apply the object only
        to the named indexes.

        If 'update_metadata' is true (the default), also update metadata for
        the object.  If the object is new to the catalog, this flag has
        no effect (metadata is always created for new objects).
        """
    def uncatalogObject(self, uid) -> None:
        """
        Uncatalog and object from the Catalog.  and 'uid' is a unique
        Catalog identifier

        Note, the uid must be the same as when the object was
        catalogued, otherwise it will not get removed from the catalog

        This method should not raise an exception if the uid cannot
        be found in the catalog.
        """
    def uniqueValuesFor(self, name):
        """return unique values for FieldIndex name"""
    def hasuid(self, uid):
        """return the rid if catalog contains an object with uid"""
    def recordify(self, object):
        """turns an object into a record tuple"""
    def instantiate(self, record, score_data=None):
        """internal method: create and initialise search result object.
        record should be a tuple of (document RID, metadata columns tuple),
        score_data can be a tuple of (scode, normalized score) or be omitted"""
    def getMetadataForRID(self, rid): ...
    def getIndexDataForRID(self, rid): ...
    def merge_query_args(self, query=None, **kw): ...
    def make_query(self, query): ...
    def search(
        self,
        query,
        sort_index=None,
        reverse: bool = False,
        limit=None,
        merge: bool = True,
    ) -> LazyMap[AbstractCatalogBrain]:
        """Iterate through the indexes, applying the query to each one. If
        merge is true then return a lazy result set (sorted if appropriate)
        otherwise return the raw (possibly scored) results for later merging.
        Limit is used in conjunction with sorting or scored results to inform
        the catalog how many results you are really interested in. The catalog
        can then use optimizations to save time and memory. The number of
        results is not guaranteed to fall within the limit however, you should
        still slice or batch the results as usual."""
    def sortResults(
        self,
        rs,
        sort_index,
        reverse: bool = False,
        limit=None,
        merge: bool = True,
        actual_result_count=None,
        b_start: int = 0,
        b_size=None,
    ): ...
    def searchResults(self, query=None, _merge: bool = True, **kw): ...
    __call__ = searchResults
    def getCatalogPlan(self, query=None):
        """Query time reporting and planning."""

def mergeResults(results, has_sort_keys, reverse):
    """Sort/merge sub-results, generating a flat sequence.

    results is a list of result set sequences, all with or without sort keys
    """

def multisort(items, sort_spec):
    """Sort a list by multiple keys bidirectionally.

    sort_spec is a list of ones and minus ones, with 1 meaning sort normally
    and -1 meaning sort reversed.

    The length of sort_spec must match the length of the first value in each
    list entry given via `items`.
    """
