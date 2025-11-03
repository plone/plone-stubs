from _typeshed import Incomplete
from OFS.Cache import Cache
from OFS.Cache import CacheManager
from OFS.SimpleItem import SimpleItem

caches: Incomplete
PRODUCT_DIR: Incomplete

class CacheException(Exception):
    """
    A cache-related exception.
    """

class CacheEntry:
    """
    Represents a cached value.
    """

    size: Incomplete
    created: Incomplete
    data: Incomplete
    view_name: Incomplete
    access_count: int
    def __init__(self, index, data, view_name) -> None: ...

class ObjectCacheEntries:
    """
    Represents the cache for one Zope object.
    """

    hits: int
    misses: int
    physical_path: Incomplete
    lastmod: int
    entries: Incomplete
    def __init__(self, path) -> None: ...
    def aggregateIndex(self, view_name, req, req_names, local_keys):
        """
        Returns the index to be used when looking for or inserting
        a cache entry.
        view_name is a string.
        local_keys is a mapping or None.
        """
    def getEntry(self, lastmod, index): ...
    def setEntry(self, lastmod, index, data, view_name) -> None: ...
    def delEntry(self, index) -> None: ...

class RAMCache(Cache):
    max_age: int
    cache: Incomplete
    writelock: Incomplete
    next_cleanup: int
    def __init__(self) -> None: ...
    def initSettings(self, kw) -> None: ...
    def getObjectCacheEntries(self, ob, create: int = 0):
        """
        Finds or creates the associated ObjectCacheEntries object.
        Remember to lock writelock when calling with the 'create' flag.
        """
    def countAllEntries(self):
        """
        Returns the count of all cache entries.
        """
    def countAccesses(self):
        """
        Returns a mapping of
        (n) -> number of entries accessed (n) times
        """
    def clearAccessCounters(self) -> None:
        """
        Clears access_count for each cache entry.
        """
    def deleteEntriesAtOrBelowThreshold(self, threshold_access_count) -> None:
        """
        Deletes entries that haven't been accessed recently.
        """
    def deleteStaleEntries(self) -> None:
        """
        Deletes entries that have expired.
        """
    def cleanup(self) -> None:
        """
        Removes cache entries.
        """
    def getCacheReport(self):
        """
        Reports on the contents of the cache.
        """
    def ZCache_invalidate(self, ob) -> None:
        """
        Invalidates the cache entries that apply to ob.
        """
    def ZCache_get(
        self, ob, view_name: str = "", keywords=None, mtime_func=None, default=None
    ):
        """
        Gets a cache entry or returns default.
        """
    def ZCache_set(
        self, ob, data, view_name: str = "", keywords=None, mtime_func=None
    ) -> None:
        """
        Sets a cache entry.
        """

class RAMCacheManager(CacheManager, SimpleItem):
    """Manage a RAMCache, which stores rendered data in RAM.

    This is intended to be used as a low-level cache for
    expensive Python code, not for objects published
    under their own URLs such as web pages.

    RAMCacheManager *can* be used to cache complete publishable
    pages, such as DTMLMethods/Documents and Page Templates,
    but this is not advised: such objects typically do not attempt
    to cache important out-of-band data such as 3xx HTTP responses,
    and the client would get an erroneous 200 response.

    Such objects should instead be cached with an
    AcceleratedHTTPCacheManager and/or downstream
    caching.
    """

    security: Incomplete
    manage_options: Incomplete
    meta_type: str
    zmi_icon: str
    id: Incomplete
    title: str
    def __init__(self, ob_id) -> None: ...
    def getId(self):
        """ """
    ZCacheManager_getCache__roles__: Incomplete
    def ZCacheManager_getCache(self): ...
    def getSettings(self):
        """Returns the current cache settings."""
    manage_main: Incomplete
    def manage_editProps(self, title, settings=None, REQUEST=None):
        """Changes the cache settings."""
    manage_stats: Incomplete
    def getCacheReport(self):
        """
        Returns the list of objects in the cache, sorted according to
        the user's preferences.
        """
    def sort_link(self, name, id):
        """
        Utility for generating a sort link.
        """
    def manage_invalidate(self, paths, REQUEST=None):
        """ZMI helper to invalidate an entry"""

class _ByteCounter:
    """auxiliary file like class which just counts the bytes written."""
    def write(self, bytes) -> None: ...
    def getCount(self): ...

manage_addRAMCacheManagerForm: Incomplete

def manage_addRAMCacheManager(self, id, REQUEST=None):
    """Adds a RAM cache manager to the folder."""
