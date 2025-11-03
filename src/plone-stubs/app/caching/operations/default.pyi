from _typeshed import Incomplete

class BaseCaching:
    """A generic caching operation class that can do pretty much all the usual
    caching operations based on options settings. For UI simplicity, it might
    be easier to subclass this in your custom operations to set a few default
    operations.

    Generic options (Default value for each is None):

    ``maxage``
        is the maximum age of the cached item, in seconds..

    ``smaxage``
        is the maximum age of the cached item in proxies, in seconds.

    ``etags''
        is a list of etag components to use when constructing an etag.

    ``lastModified``
        is a boolean indicating whether to set a Last-Modified header
        and turn on 304 responses.

    ``ramCache``
        is a boolean indicating whether to turn on RAM caching for this item.
        Etags are only required if the URL is not specific enough to ensure
        uniqueness.

    ``vary``
        is a string to add as a Vary header value in the response.
    """

    title: Incomplete
    description: Incomplete
    prefix: str
    options: Incomplete
    maxage: Incomplete
    smaxage: Incomplete
    etags: Incomplete
    vary: Incomplete
    lastModified: bool
    ramCache: bool
    anonOnly: bool
    published: Incomplete
    request: Incomplete
    def __init__(self, published, request) -> None: ...
    def interceptResponse(self, rulename, response, class_=None): ...
    def modifyResponse(self, rulename, response, class_=None): ...

class WeakCaching(BaseCaching):
    """Weak caching operation. A subclass of the generic BaseCaching
    operation to help make the UI approachable by mortals
    """

    title: Incomplete
    description: Incomplete
    prefix: str
    sort: int
    options: Incomplete
    maxage: int
    smaxage: Incomplete
    etags: Incomplete
    vary: Incomplete
    lastModified: bool
    ramCache: bool
    anonOnly: bool

class ModerateCaching(BaseCaching):
    """Moderate caching operation. A subclass of the generic BaseCaching
    operation to help make the UI approachable by mortals
    """

    title: Incomplete
    description: Incomplete
    prefix: str
    sort: int
    options: Incomplete
    maxage: int
    smaxage: int
    etags: Incomplete
    vary: Incomplete
    lastModified: bool
    ramCache: bool
    anonOnly: bool

class StrongCaching(BaseCaching):
    """Strong caching operation. A subclass of the generic BaseCaching
    operation to help make the UI approachable by mortals
    """

    title: Incomplete
    description: Incomplete
    prefix: str
    sort: int
    options: Incomplete
    maxage: int
    smaxage: Incomplete
    etags: Incomplete
    vary: Incomplete
    lastModified: bool
    ramCache: bool
    anonOnly: bool

class TerseCaching(BaseCaching):
    """Terse caching operation."""

    title: Incomplete
    description: Incomplete
    prefix: str
    sort: int
    options: Incomplete
    maxage: int
    smaxage: int
    vary: str
    etags: Incomplete
    lastModified: bool
    ramCache: bool
    anonOnly: bool

class NoCaching:
    """A caching operation that tries to keep the response
    out of all caches.
    """

    title: Incomplete
    description: Incomplete
    prefix: str
    sort: int
    options: Incomplete
    published: Incomplete
    request: Incomplete
    def __init__(self, published, request) -> None: ...
    def interceptResponse(self, rulename, response) -> None: ...
    def modifyResponse(self, rulename, response) -> None: ...
