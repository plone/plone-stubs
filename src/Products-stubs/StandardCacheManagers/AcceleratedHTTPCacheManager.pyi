from _typeshed import Incomplete
from http.client import HTTPConnection
from OFS.Cache import Cache
from OFS.Cache import CacheManager
from OFS.SimpleItem import SimpleItem

logger: Incomplete

class AcceleratedHTTPCache(Cache):
    connection_factory = HTTPConnection
    hit_counts: Incomplete
    def __init__(self) -> None: ...
    def initSettings(self, kw) -> None: ...
    def ZCache_invalidate(self, ob): ...
    def ZCache_get(self, ob, view_name, keywords, mtime_func, default): ...
    def ZCache_set(self, ob, data, view_name, keywords, mtime_func) -> None: ...

caches: Incomplete
PRODUCT_DIR: Incomplete

class AcceleratedHTTPCacheManager(CacheManager, SimpleItem):
    security: Incomplete
    manage_options: Incomplete
    meta_type: str
    zmi_icon: str
    id: Incomplete
    title: str
    def __init__(self, ob_id) -> None: ...
    def getId(self):
        """ """
    @security.private
    def ZCacheManager_getCache(self): ...
    def getSettings(self):
        """ """
    manage_main: Incomplete
    def manage_editProps(self, title, settings=None, REQUEST=None):
        """ """
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

manage_addAcceleratedHTTPCacheManagerForm: Incomplete

def manage_addAcceleratedHTTPCacheManager(self, id, REQUEST=None):
    """ """
