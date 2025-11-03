from _typeshed import Incomplete
from Acquisition import Implicit
from collections.abc import Generator
from DocumentTemplate._DocumentTemplate import TemplateDict
from DocumentTemplate.security import RestrictedDTML
from OFS.Folder import Folder
from Persistence import Persistent

LOG: Incomplete
manage_addZCatalogForm: Incomplete

def manage_addZCatalog(self, id, title, vocab_id=None, REQUEST=None):
    """Add a ZCatalog object. The vocab_id argument is ignored."""

class ZCatalog(Folder, Persistent, Implicit):
    """ZCatalog object

    A ZCatalog contains arbirary index like references to Zope
    objects.  ZCatalog's can index either 'Field' values of object, or
    'Text' values.

    ZCatalog does not store references to the objects themselves, but
    rather to a unique identifier that defines how to get to the
    object.  In Zope, this unique idenfier is the object's relative
    path to the ZCatalog (since two Zope object's cannot have the same
    URL, this is an excellent unique qualifier in Zope).

    Most of the dirty work is done in the _catalog object, which is an
    instance of the Catalog class.  An interesting feature of this
    class is that it is not Zope specific.  You can use it in any
    Python program to catalog objects.
    """

    security: Incomplete
    meta_type: str
    zmi_icon: str
    manage_options: Incomplete
    manage_catalogView: Incomplete
    manage_catalogIndexes: Incomplete
    manage_catalogSchema: Incomplete
    manage_catalogFind: Incomplete
    manage_catalogAdvanced: Incomplete
    manage_catalogReport: Incomplete
    manage_catalogPlan: Incomplete
    manage_objectInformation: Incomplete
    meta_types: Incomplete
    Indexes: Incomplete
    threshold: int
    long_query_time: float
    vocabulary: Incomplete
    vocab_id: str
    id: Incomplete
    title: Incomplete
    def __init__(self, id, title: str = "", vocab_id=None, container=None) -> None: ...
    def __len__(self) -> int: ...
    def manage_edit(self, RESPONSE, URL1, threshold: int = 1000, REQUEST=None) -> None:
        """edit the catalog"""
    def manage_subbingToggle(self, REQUEST, RESPONSE, URL1) -> None:
        """toggle subtransactions"""
    def manage_catalogObject(self, REQUEST, RESPONSE, URL1, urls=None) -> None:
        """index Zope object(s) that 'urls' point to"""
    def manage_uncatalogObject(self, REQUEST, RESPONSE, URL1, urls=None) -> None:
        """removes Zope object(s) 'urls' from catalog"""
    def manage_catalogReindex(self, REQUEST, RESPONSE, URL1) -> None:
        """clear the catalog, then re-index everything"""
    def refreshCatalog(self, clear: int = 0, pghandler=None) -> None:
        """re-index everything we can find"""
    def manage_catalogClear(self, REQUEST=None, RESPONSE=None, URL1=None) -> None:
        """clears the whole enchilada"""
    def manage_catalogFoundItems(
        self,
        REQUEST,
        RESPONSE,
        URL2,
        URL1,
        obj_metatypes=None,
        obj_ids=None,
        obj_searchterm=None,
        obj_expr=None,
        obj_mtime=None,
        obj_mspec=None,
        obj_roles=None,
        obj_permission=None,
    ) -> None:
        """Find object according to search criteria and Catalog them"""
    def manage_addColumn(self, name, REQUEST=None, RESPONSE=None, URL1=None) -> None:
        """add a column"""
    def manage_delColumn(self, names, REQUEST=None, RESPONSE=None, URL1=None) -> None:
        """delete a column or some columns"""
    def manage_addIndex(
        self, name, type, extra=None, REQUEST=None, RESPONSE=None, URL1=None
    ) -> None:
        """add an index"""
    def manage_delIndex(self, ids=None, REQUEST=None, RESPONSE=None, URL1=None) -> None:
        """delete an index or some indexes"""
    def manage_clearIndex(
        self, ids=None, REQUEST=None, RESPONSE=None, URL1=None
    ) -> None:
        """clear an index or some indexes"""
    def reindexIndex(self, name, REQUEST, pghandler=None) -> None: ...
    def manage_reindexIndex(
        self, ids=None, REQUEST=None, RESPONSE=None, URL1=None
    ) -> None:
        """Reindex index(es) from a ZCatalog"""
    @security.private
    def maintain_zodb_cache(self): ...
    def catalog_object(
        self, obj, uid=None, idxs=None, update_metadata: int = 1, pghandler=None
    ) -> None: ...
    def uncatalog_object(self, uid) -> None: ...
    def uniqueValuesFor(self, name): ...
    def getpath(self, rid): ...
    def getrid(self, path, default=None): ...
    def getobject(self, rid, REQUEST=None): ...
    def getMetadataForUID(self, uid): ...
    def getIndexDataForUID(self, uid): ...
    def getMetadataForRID(self, rid): ...
    def getIndexDataForRID(self, rid): ...
    def getAllBrains(self) -> Generator[Incomplete]: ...
    def searchAll(self): ...
    def schema(self): ...
    def indexes(self): ...
    def index_objects(self): ...
    def getIndexObjects(self): ...
    def searchResults(self, query=None, **kw):
        """Search the catalog.

        Search terms can be passed as a query or as keyword arguments.
        """
    __call__ = searchResults
    def search(
        self, query, sort_index=None, reverse: int = 0, limit=None, merge: int = 1
    ):
        """Programmatic search interface, use for searching the catalog from
        scripts.

        query:      Dictionary containing catalog query
        sort_index: Name of sort index
        reverse:    Reverse sort order?
        limit:      Limit sorted result count (optimization hint)
        merge:      Return merged results (like searchResults) or raw
                    results for later merging.
        """
    def valid_roles(self): ...
    def ZopeFindAndApply(
        self,
        obj,
        obj_ids=None,
        obj_metatypes=None,
        obj_searchterm=None,
        obj_expr=None,
        obj_mtime=None,
        obj_mspec=None,
        obj_permission=None,
        obj_roles=None,
        search_sub: int = 0,
        REQUEST=None,
        result=None,
        pre: str = "",
        apply_func=None,
        apply_path: str = "",
    ):
        """Zope Find interface and apply

        This is a *great* hack.  Zope find just doesn't do what we
        need here; the ability to apply a method to all the objects
        *as they're found* and the need to pass the object's path into
        that method.
        """
    def resolve_url(self, path, REQUEST): ...
    def resolve_path(self, path): ...
    def manage_normalize_paths(self, REQUEST) -> None:
        """Ensure that all catalog paths are full physical paths

        This should only be used with ZCatalogs in which all paths can
        be resolved with unrestrictedTraverse."""
    pgthreshold: Incomplete
    def manage_setProgress(
        self, pgthreshold: int = 0, RESPONSE=None, URL1=None
    ) -> None:
        """Set parameter to perform logging of reindexing operations very
        'pgthreshold' objects
        """
    def addIndex(self, name, type, extra=None) -> None: ...
    def availableIndexes(self):
        """Return a sorted list of indexes.

        Only indexes get returned for which the user has adequate
        permission to add them.
        """
    def delIndex(self, name) -> None: ...
    def clearIndex(self, name) -> None: ...
    def addColumn(self, name, default_value=None): ...
    def delColumn(self, name): ...
    def getCatalogPlan(self):
        """Get a string representation of a query plan"""
    def getCatalogReport(self):
        """Query time reporting."""
    def manage_resetCatalogReport(self, REQUEST=None) -> None:
        """Resets the catalog report."""
    def manage_editCatalogReport(
        self, long_query_time: float = 0.1, REQUEST=None
    ) -> None:
        """Edit the long query time."""

def absattr(attr): ...

class td(RestrictedDTML, TemplateDict): ...

def expr_match(ob, ed): ...
def mtime_match(ob, t, q): ...
def role_match(ob, permission, roles): ...
