from _typeshed import Incomplete

logger: Incomplete

def invalidateCache(settings, event) -> None:
    """Event handler for registry change"""

class ThemingPolicy:
    request: Incomplete
    def __init__(self, request) -> None:
        """Adapt IRequest.
        Do not call this class directly, always use a
        utils.theming_policy(request) adapter lookup.

        This enables overriding of the IThemingPolicy adapter
        via ZCML by integrators.

        When used as INoRequest adapter, returns the default policy.
        """
    def getSettings(self):
        """Settings for current theme."""
    def getCurrentTheme(self):
        """The name of the current theme."""
    def isThemeEnabled(self, settings=None):
        """Whether theming is enabled."""
    def getCache(self, theme=None):
        """Managing the cache is a policy decision."""
    def getCacheKey(self, theme=None): ...
    def getCacheStorage(self): ...
    def invalidateCache(self) -> None:
        """When our settings are changed, invalidate the cache on all zeo clients"""
    def get_theme(self):
        """Managing the theme cache is a plone.app.theming policy
        decision. Moved out out Products.CMFPlone."""
    def set_theme(self, themeName, themeObj) -> None:
        """Update the theme cache"""

class ThemeCache:
    """Simple cache for the transform and theme"""

    transform: Incomplete
    expressions: Incomplete
    themeObj: Incomplete
    def __init__(self) -> None: ...
    def updateTransform(self, transform) -> None: ...
    def updateExpressions(self, expressions) -> None: ...
    def updateTheme(self, themeObj) -> None: ...
