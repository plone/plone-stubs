from _typeshed import Incomplete

class UserID:
    """The ``userid`` etag component, returning the current user's id"""

    published: Incomplete
    request: Incomplete
    def __init__(self, published, request) -> None: ...
    def __call__(self): ...

class Roles:
    """The ``roles`` etag component, returning the current user's roles,
    separated by semicolons
    """

    published: Incomplete
    request: Incomplete
    def __init__(self, published, request) -> None: ...
    def __call__(self): ...

class Language:
    """The ``language`` etag component, returning the value of the
    HTTP_ACCEPT_LANGUAGE request key.
    """

    published: Incomplete
    request: Incomplete
    def __init__(self, published, request) -> None: ...
    def __call__(self): ...

class UserLanguage:
    """The ``userLanguage`` etag component, returning the user's preferred
    language
    """

    published: Incomplete
    request: Incomplete
    def __init__(self, published, request) -> None: ...
    def __call__(self): ...

class LastModified:
    """The ``lastModified`` etag component, returning the last modification
    timestamp
    """

    published: Incomplete
    request: Incomplete
    def __init__(self, published, request) -> None: ...
    def __call__(self): ...

class CatalogCounter:
    """The ``catalogCounter`` etag component, returning a counter which is
    incremented each time the catalog is updated.
    """

    published: Incomplete
    request: Incomplete
    def __init__(self, published, request) -> None: ...
    def __call__(self): ...

class ObjectLocked:
    """The ``locked`` etag component, returning 1 or 0 depending on whether
    the object is locked.
    """

    published: Incomplete
    request: Incomplete
    def __init__(self, published, request) -> None: ...
    def __call__(self): ...

class Skin:
    """The ``skin`` etag component, returning the current skin name."""

    published: Incomplete
    request: Incomplete
    def __init__(self, published, request) -> None: ...
    def __call__(self): ...

class AnonymousOrRandom:
    """The ``anonymousOrRandom`` etag component. This is normally added
    implicitly by the ``anonOnly`` setting. It will return for anonymous
    users, but a random number for logged-in ones. The idea is to force a
    re-fetch of a page every time for logged-in users.
    """

    published: Incomplete
    request: Incomplete
    def __init__(self, published, request) -> None: ...
    def __call__(self): ...

class CopyCookie:
    """The ``copy`` etag component, returning 1 or 0 depending on whether
    the '__cp' cookie is set.
    """

    published: Incomplete
    request: Incomplete
    def __init__(self, published, request) -> None: ...
    def __call__(self): ...

class ResourceRegistries:
    """The ``resourceRegistries`` etag component, returning a timestamp.

    This is the last modified timestamp from the Plone 5+ Resource Registries.
    This is useful for avoiding requests for expired resources from cached pages.
    """

    published: Incomplete
    request: Incomplete
    def __init__(self, published, request) -> None: ...
    def __call__(self): ...

class Layout:
    """The 'layout' etag component, returning they layout of a content item."""

    published: Incomplete
    request: Incomplete
    def __init__(self, published, request) -> None: ...
    def __call__(self): ...
