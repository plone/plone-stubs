from _typeshed import Incomplete
from zope.interface import Interface

_: Incomplete

class ICacheProfiles(Interface):
    """Marker interface for extension profiles that contain cache settings.
    These will primarily include a ``registry.xml`` file to configure cache
    settings.

    To use the marker interface, you can do::

        <genericsetup:registerProfile
            name="my-cache-settings"
            title="My cache settings"
            directory="profiles/my-cache-settings"
            description="My cache settings"
            for="plone.app.caching.interfaces.ICacheProfiles"
            provides="Products.GenericSetup.interfaces.EXTENSION"
            />

    This will hide the profile from the Plone quickinstaller, and make it
    available for installation in the cache settings control panel.
    """

class IPloneCacheSettings(Interface):
    """Settings stored in the registry.

    Basic cache settings are represented by
    ``plone.caching.interfaces.ICacheSettings``. These are additional,
    Plone-specific settings.
    """

    templateRulesetMapping: Incomplete
    contentTypeRulesetMapping: Incomplete
    purgedContentTypes: Incomplete
    cacheStopRequestVariables: Incomplete

class IETagValue(Interface):
    """ETag component builder

    Register a named multi-adapter from ``(published, request)`` to this
    interface to provide the values for ETag components. Various caching
    operations will look up such adapters to compose an ETag value. The
    adapter name is used in options configuring those components.
    """
    def __call__() -> None:
        """Return the ETag component, as a string."""

class IRAMCached(Interface):
    """Marker interface applied to the request if it should be RAM cached.

    The cache key will be stored in request annotations.
    """
