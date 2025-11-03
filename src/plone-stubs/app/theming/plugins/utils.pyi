from _typeshed import Incomplete
from collections.abc import Generator

def pluginsCacheKey(fun): ...
def pluginSettingsCacheKey(fun, themeDirectory, plugins=None): ...
def sortDependencies(plugins) -> Generator[Incomplete]:
    """Topological sort"""

def getPlugins():
    """Get all registered plugins topologically sorted"""

def getPluginSettings(themeDirectory, plugins=None):
    """Given an IResourceDirectory for a theme, return the settings for the
    given list of plugins (or all plugins, if not given) provided as a list
    of (name, plugin) pairs.

    Returns a dict of dicts, with the outer dict having plugin names as keys
    and containing plugins settings (key/value pairs) as values.
    """
