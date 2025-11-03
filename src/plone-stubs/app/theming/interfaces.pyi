from _typeshed import Incomplete
from zope.interface import Interface

_: Incomplete
THEME_RESOURCE_NAME: str
RULE_FILENAME: str
DEFAULT_THEME_FILENAME: str
TEMPLATE_THEME: str
MANIFEST_FORMAT: Incomplete
THEME_EXTENSIONS: Incomplete

def get_default_custom_css_timestamp(): ...

class ITheme(Interface):
    """A theme, loaded from a resource directory"""

    rules: Incomplete
    title: Incomplete
    description: Incomplete
    absolutePrefix: Incomplete
    parameterExpressions: Incomplete
    doctype: Incomplete
    preview: Incomplete

class IThemeSettings(Interface):
    """Transformation settings"""

    enabled: Incomplete
    currentTheme: Incomplete
    rules: Incomplete
    absolutePrefix: Incomplete
    readNetwork: Incomplete
    hostnameBlacklist: Incomplete
    parameterExpressions: Incomplete
    doctype: Incomplete
    custom_css: Incomplete
    custom_css_timestamp: Incomplete

class IThemingLayer(Interface):
    """Browser layer used to indicate that plone.app.theming is installed"""

class IThemePlugin(Interface):
    """Register a named utility providing this interface to create a theme
    plugin.

    The various lifecycle methods will be called with the relevant theme
    name and a dictionary called ``settings`` which reflects any settings for
    this plugin stored in the theme's manifest.

    Plugin settings are found in a section called ``[theme:pluginname]``.

    Plugins may have dependencies. Dependent plugins are invoked after their
    dependencies. The settings of dependencies are passed to lifecycle methods
    in the variable ``dependencySetings``, which is a dictionary of
    dictionaries. The keys are plugin names, and the values equivalent to
    the ``settings`` variable for the corresponding plugin.

    If a given plugin can't be the found, an exception will be thrown during
    activation.
    """

    dependencies: Incomplete
    def onDiscovery(theme, settings, dependenciesSettings) -> None:
        """Called when the theme is discovered at startup time. This is
        not applicable for through-the-web/zip-file imported themes!
        """
    def onCreated(theme, settings, dependenciesSettings) -> None:
        """Called when the theme is created through the web (or imported
        from a zip file)
        """
    def onEnabled(theme, settings, dependenciesSettings) -> None:
        """Called when the theme is enabled through the control panel, either
        because the global "enabled" flag was switched, or because the theme
        was changed.
        """
    def onDisabled(theme, settings, dependenciesSettings) -> None:
        """Called when the given theme is disabled through the control panel,
        either because the global "enabled" flag was switched, or because the
        theme was changed.
        """
    def onRequest(request, theme, settings, dependenciesSettings) -> None:
        """Called upon traversal into the site when a theme is enabled"""

class IThemeAppliedEvent(Interface):
    theme: Incomplete

class INoRequest(Interface):
    """Fallback to enable querying for the policy adapter
    even in the absence of a proper IRequest."""

class IThemingPolicy(Interface):
    """An adapter on request that provides access to the current
    theme and theme settings.
    """
    def getSettings() -> None:
        """Settings for current theme."""
    def getCurrentTheme() -> None:
        """The name of the current theme."""
    def isThemeEnabled() -> None:
        """Whether theming is enabled."""
    def getCache(theme=None) -> None:
        """Managing the cache is a policy decision."""
    def getCacheKey(theme=None) -> None:
        """Managing the cache is a policy decision."""
    def invalidateCache() -> None:
        """When our settings are changed, invalidate the cache on all zeo clients."""
    def get_theme() -> None:
        """Returns the current theme object, cached."""
    def set_theme(themeName, themeObj) -> None:
        """Update the theme cache."""
