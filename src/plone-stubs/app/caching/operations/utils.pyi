from _typeshed import Incomplete

PAGE_CACHE_KEY: str
PAGE_CACHE_ANNOTATION_KEY: str
ETAG_ANNOTATION_KEY: str
LASTMODIFIED_ANNOTATION_KEY: str
logger: Incomplete
parseETagLock: Incomplete
etagQuote: Incomplete
etagNoQuote: Incomplete

def setCacheHeaders(
    published,
    request,
    response,
    maxage=None,
    smaxage=None,
    etag=None,
    lastModified=None,
    vary=None,
) -> None:
    """General purpose dispatcher to set various cache headers

    ``maxage`` is the cache timeout value in seconds
    ``smaxage`` is the proxy cache timeout value in seconds.
    ``lastModified`` is a datetime object for the last modified time
    ``etag`` is an etag string
    ``vary`` is a vary header string
    """

def doNotCache(published, request, response) -> None:
    """Set response headers to ensure that the response is not cached by
    web browsers or caching proxies.

    This is an IE-safe operation. Under certain conditions, IE chokes on
    ``no-cache`` and ``no-store`` cache-control tokens so instead we just
    expire immediately and disable validation.
    """

def cacheInBrowser(published, request, response, etag=None, lastModified=None) -> None:
    """Set response headers to indicate that browsers should cache the
    response but expire immediately and revalidate the cache on every
    subsequent request.

    ``etag`` is a string value indicating an ETag to use.
    ``lastModified`` is a datetime object

    If neither etag nor lastModified is given then no validation is
    possible and this becomes equivalent to doNotCache()
    """

def cacheInProxy(
    published, request, response, smaxage, etag=None, lastModified=None, vary=None
) -> None:
    """Set headers to cache the response in a caching proxy.

    ``smaxage`` is the timeout value in seconds.
    ``lastModified`` is a datetime object for the last modified time
    ``etag`` is an etag string
    ``vary`` is a vary header string
    """

def cacheInBrowserAndProxy(
    published,
    request,
    response,
    maxage,
    smaxage=None,
    etag=None,
    lastModified=None,
    vary=None,
) -> None:
    """Set headers to cache the response in the browser and caching proxy if
    applicable.

    ``maxage`` is the timeout value in seconds
    ``smaxage`` is the proxy timeout value in seconds
    ``lastModified`` is a datetime object for the last modified time
    ``etag`` is an etag string
    ``vary`` is a vary header string
    """

def cacheInRAM(
    published, request, response, etag=None, lastModified=None, annotationsKey=...
) -> None:
    """Set a flag indicating that the response for the given request
    should be cached in RAM.

    This will signal to a transform chain step after the response has been
    generated to store the result in the RAM cache.

    To actually use the cached response, you can implement
    ``interceptResponse()`` in your caching operation to call
    ``fetchFromRAMCache()`` and then return the value of the
    ``cachedResponse()`` helper.

    ``etag`` is a string identifying the resource.

    ``annotationsKey`` is the key used by the transform to look up the
    caching key when storing the response in the cache. It should match that
    passed to ``storeResponseInRAMCache()``.
    """

def cachedResponse(
    published, request, response, status, headers, body, gzip: bool = False
):
    """Returned a cached page. Modifies the response (status and headers)
    and returns the cached body.

    ``status`` is the cached HTTP status
    ``headers`` is a dictionary of cached HTTP headers
    ``body`` is a cached response body
    ``gzip`` should be set to True if the response is to be gzipped
    """

def notModified(published, request, response, etag=None, lastModified=None):
    """Return a ``304 NOT MODIFIED`` response. Modifies the response (status)
    and returns an empty body to indicate the request should be interrupted.

    ``etag`` is an ETag to set on the response
    ``lastModified`` is the last modified date to set on the response

    Both ``etag`` and ``lastModified`` are optional.
    """

def cacheStop(request, rulename):
    """Check for any cache stop variables in the request."""

def isModified(request, etag=None, lastModified=None):
    """Return True or False depending on whether the published resource has
    been modified.

    ``etag`` is the current etag, to be checked against the If-None-Match
    header.

    ``lastModified`` is the current last-modified datetime, to be checked
    against the If-Modified-Since header.
    """

def visibleToRole(published, role, permission: str = "View"):
    """Determine if the published object would be visible to the given
    role.

    ``role`` is a role name, e.g. ``Anonymous``.
    ``permission`` is the permission to check for.
    """

def getContext(published, marker=...):
    """Given a published object, attempt to look up a context

    ``published`` is the object that was published.
    ``marker`` is a marker interface to look for

    Returns an item providing ``marker`` or None, if it cannot be found.
    """

def formatDateTime(dt):
    """Format a Python datetime object as an RFC1123 date.

    If the datetime object is timezone-naive, it is assumed to be local time.
    """

def parseDateTime(str):
    """Return a Python datetime object from an an RFC1123 date.

    Returns a datetime object with a timezone. If no timezone is found in the
    input string, assume local time.
    """

def getLastModifiedAnnotation(published, request, lastModified: bool = True):
    """Try to get the last modified date from a request annotation if available,
    otherwise try to get it from published object
    """

def getLastModified(published, lastModified: bool = True):
    """Get a last modified date or None.

    If an ``ILastModified`` adapter can be found, and returns a date that is
    not timezone aware, assume it is local time and add timezone.
    """

def getExpiration(maxage):
    """Get an expiration date as a datetime in the local timezone.

    ``maxage`` is the maximum age of the item, in seconds. If it is 0 or
    negative, return a date ten years in the past.
    """

def getETagAnnotation(published, request, keys=(), extraTokens=()):
    """Try to get the ETag from a request annotation if available,
    otherwise try to get it from published object
    """

def getETag(published, request, keys=(), extraTokens=()):
    """Calculate an ETag.

    ``keys`` is a list of types of items to include in the ETag. These must
    match named multi-adapters on (published, request) providing
    ``IETagValue``.

    ``extraTokens`` is a list of additional ETag tokens to include, verbatim
    as strings.

    All tokens will be concatenated into an ETag string, separated by pipes.
    """

def parseETags(text, allowWeak: bool = True, _result=None):
    """Parse a header value into a list of etags. Handles fishy quoting and
    other browser quirks.

    ``text`` is the header value to parse.
    ``allowWeak`` should be False if weak ETag values should not be returned
    ``_result`` is internal - don't set it.

    Returns a list of strings. For weak etags, the W/ prefix is removed.
    """

def getRAMCache(globalKey=...):
    """Get a RAM cache instance for the given key. The return value is ``None``
    if no RAM cache can be found, or a mapping object supporting at least
    ``__getitem__()``, ``__setitem__()`` and ``get()`` that can be used to get
    or set cache values.

    ``key`` is the global cache key, which must be unique site-wide. Most
    commonly, this will be the operation dotted name.
    """

def getRAMCacheKey(request, etag=None, lastModified=None):
    """Calculate the cache key for pages cached in RAM.

    ``etag`` is a unique etag string.

    ``lastModified`` is a datetime object giving the last=modified
     date for the resource.

    The cache key is a combination of the resource's URL, the etag,
    and the last-modified date. Both the etag and last=modified are
    optional but in most cases that are worth caching in RAM, the etag
    is needed to ensure the key changes when the resource view changes.
    """

def storeResponseInRAMCache(
    request, response, result, globalKey=..., annotationsKey=...
) -> None:
    """Store the given response in the RAM cache.

    ``result`` should be the response body as a string.

    ``globalKey`` is the global cache key. This needs to be the same key
    as the one used to fetch the data.

    ``annotationsKey`` is the key in annotations on the request from which
    the (resource-identifying) caching key should be retrieved. The default
    is that used by the ``cacheInRAM()`` helper function.
    """

def fetchFromRAMCache(
    request, etag=None, lastModified=None, globalKey=..., default=None
):
    """Return a page cached in RAM, or None if it cannot be found.

    The return value is a tuple as stored by ``storeResponseInRAMCache()``.

    ``etag`` is an ETag for the content, and is usually used as a basis for
    the cache key.

    ``lastModified`` is the last modified date for the content, which can
    potentially be used instead of etag if sufficient to ensure freshness.
    Perhaps a rare occurrence but it's here in case someone needs it.
    Do not use this to cache binary responses (like images and file downloads)
    as Zope already caches most of the payload of these.

    ``globalKey`` is the global cache key. This needs to be the same key
    as the one used to store the data, i.e. it must correspond to the one
    used when calling ``storeResponseInRAMCache()``.
    """
