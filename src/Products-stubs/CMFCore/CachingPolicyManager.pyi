from _typeshed import Incomplete
from OFS.Cache import Cache
from OFS.Cache import CacheManager
from OFS.SimpleItem import SimpleItem

VIEW_METATYPES: Incomplete

def createCPContext(content, view_method, keywords, time=None):
    """
    Construct an expression context for TALES expressions,
    for use by CachingPolicy objects.
    """

class CPMCache(Cache):
    """Simple OFS.Cache-implementation"""

    security: Incomplete
    @security.private
    def ZCache_invalidate(self, ob) -> None:
        """An object is forced out of the cache

        This implementation stores nothing and does not attempt to
        communicate with cache servers, so this is a no-op.
        """
    @security.private
    def ZCache_get(self, ob, view_name, keywords, mtime_func, default) -> None:
        """An object is retrieved from the cache

        This implementation stores nothing - a no-op.
        """
    @security.private
    def ZCache_set(self, ob, data, view_name, keywords, mtime_func):
        """An object is pushed into the cache

        Even though this cache implementation does not cache anything per se,
        this method is used as a suitable hook to activate the real heavy
        lifting done by the CachePolicyManager.
        """

class CachingPolicy:
    """
    Represent a single class of cachable objects:

      - class membership is defined by \'predicate\', a TALES expression
        with access to the following top-level names:

        \'object\' -- the object itself

        \'view\' -- the name of the view method

        \'keywords\' -- keywords passed to the request

        \'request\' -- the REQUEST object itself

        \'member\' -- the authenticated member, or None if anonymous

        \'modules\' -- usual TALES access-with-import

        \'nothing\' -- None

        \'time\' -- A DateTime object for the current date and time

      - mtime_func is used to set the "Last-modified" HTTP response
        header, which is another TALES expression evaluated
        against the same namespace.  If not specified explicitly,
        uses \'object/modified\'.  mtime_func is also used in responding
        to conditional GETs.

      - The "Expires" HTTP response header and the "max-age" token of
        the "Cache-control" header will be set using \'max_age_secs\',
        if passed;  it should be an integer value in seconds.

      - The "s-maxage" token of the "Cache-control" header will be
        set using \'s_max_age_secs\', if passed;  it should be an integer
        value in seconds.

      - The "Vary" HTTP response headers will be set if a value is
        provided. The Vary header is described in RFC 2616. In essence,
        it instructs caches that respect this header (such as Squid
        after version 2.4) to distinguish between requests not just by
        the request URL, but also by values found in the headers showing
        in the Vary tag. "Vary: Cookie" would force Squid to also take
        Cookie headers into account when deciding what cached object to
        choose and serve in response to a request.

      - The "ETag" HTTP response header will be set if a value is
        provided. The value is a TALES expression and the result
        after evaluation will be used as the ETag header value.

      - Other tokens will be added to the "Cache-control" HTTP response
        header as follows:

         \'no_cache=1\' argument => "no-cache" token

         \'no_store=1\' argument => "no-store" token

         \'must_revalidate=1\' argument => "must-revalidate" token

         \'proxy_revalidate=1\' argument => "proxy-revalidate" token

         \'public=1\' argument => "public" token

         \'private=1\' argument => "private" token

         \'no_transform=1\' argument => "no-transform" token

      - The last_modified argument is used to determine whether to add a
        Last-Modified header.  last_modified=1 by default.  There appears
        to be a bug in IE 6 (and possibly other versions) that uses the
        Last-Modified header plus some heuristics rather than the other
        explicit caching headers to determine whether to render content
        from the cache.  If you set, say, max-age=0, must-revalidate and
        have a Last-Modified header some time in the past, IE will
        recognize that the page in cache is stale and will request an
        update from the server BUT if you have a Last-Modified header
        with an older date, will then ignore the update and render from
        the cache, so you may want to disable the Last-Modified header
        when controlling caching using Cache-Control headers.

      - The pre-check and post-check Cache-Control tokens are Microsoft
        proprietary tokens added to IE 5+.  Documentation can be found
        here: http://msdn.microsoft.com/workshop/author/perf/perftips.asp
        Unfortunately these are needed to make IE behave correctly.

    """
    def __init__(
        self,
        policy_id,
        predicate: str = "",
        mtime_func: str = "",
        max_age_secs=None,
        no_cache: int = 0,
        no_store: int = 0,
        must_revalidate: int = 0,
        vary: str = "",
        etag_func: str = "",
        s_max_age_secs=None,
        proxy_revalidate: int = 0,
        public: int = 0,
        private: int = 0,
        no_transform: int = 0,
        enable_304s: int = 0,
        last_modified: int = 1,
        pre_check=None,
        post_check=None,
    ) -> None: ...
    def getPolicyId(self):
        """ """
    def getPredicate(self):
        """ """
    def getMTimeFunc(self):
        """ """
    def getMaxAgeSecs(self):
        """ """
    def getSMaxAgeSecs(self):
        """ """
    def getNoCache(self):
        """ """
    def getNoStore(self):
        """ """
    def getMustRevalidate(self):
        """ """
    def getProxyRevalidate(self):
        """ """
    def getPublic(self):
        """ """
    def getPrivate(self):
        """ """
    def getNoTransform(self):
        """ """
    def getVary(self):
        """ """
    def getETagFunc(self):
        """ """
    def getEnable304s(self):
        """ """
    def getLastModified(self):
        """Should we set the last modified header?"""
    def getPreCheck(self):
        """ """
    def getPostCheck(self):
        """ """
    def testPredicate(self, expr_context):
        """Does this request match our predicate?"""
    def getHeaders(self, expr_context):
        """
        Does this request match our predicate?  If so, return a
        sequence of caching headers as ( key, value ) tuples.
        Otherwise, return an empty sequence.
        """

class CachingPolicyManager(SimpleItem, CacheManager):
    """
    Manage the set of CachingPolicy objects for the site;  dispatch
    to them from skin methods.
    """

    id: str
    meta_type: str
    zmi_icon: str
    security: Incomplete
    def __init__(self) -> None: ...
    manage_options: Incomplete
    manage_cachingPolicies: Incomplete
    @security.public
    def listPolicies(self):
        """List '(id, (policy, typeObjectName))' tuples for all policies."""
    def addPolicy(
        self,
        policy_id,
        predicate,
        mtime_func,
        max_age_secs,
        no_cache,
        no_store,
        must_revalidate,
        vary,
        etag_func,
        REQUEST=None,
        s_max_age_secs=None,
        proxy_revalidate: int = 0,
        public: int = 0,
        private: int = 0,
        no_transform: int = 0,
        enable_304s: int = 0,
        last_modified: int = 1,
        pre_check=None,
        post_check=None,
    ) -> None:
        """
        Add a caching policy.
        """
    def updatePolicy(
        self,
        policy_id,
        predicate,
        mtime_func,
        max_age_secs,
        no_cache,
        no_store,
        must_revalidate,
        vary,
        etag_func,
        REQUEST=None,
        s_max_age_secs=None,
        proxy_revalidate: int = 0,
        public: int = 0,
        private: int = 0,
        no_transform: int = 0,
        enable_304s: int = 0,
        last_modified: int = 1,
        pre_check: int = 0,
        post_check: int = 0,
    ) -> None:
        """
        Update a caching policy.
        """
    def movePolicyUp(self, policy_id, REQUEST=None) -> None:
        """
        Move a caching policy up in the list.
        """
    def movePolicyDown(self, policy_id, REQUEST=None) -> None:
        """
        Move a caching policy down in the list.
        """
    def removePolicy(self, policy_id, REQUEST=None) -> None:
        """
        Remove a caching policy.
        """
    def getHTTPCachingHeaders(self, content, view_method, keywords, time=None):
        """
        Return a list of HTTP caching headers based on 'content',
        'view_method', and 'keywords'.
        """
    def getModTimeAndETag(self, content, view_method, keywords, time=None):
        """Return the modification time and ETag for the content object,
        view method, and keywords as the tuple (modification_time, etag,
        set_last_modified_header), where modification_time is a DateTime,
        or None.
        """
    @security.private
    def ZCacheManager_getCache(self):
        """Retrieve a cache object"""

def handleCachingPolicyManagerEvent(ob, event) -> None:
    """Event subscriber for (un)registering a CPM as CacheManager"""

def manage_addCachingPolicyManager(self, REQUEST=None) -> None:
    """
    Add a CPM to self.
    """
