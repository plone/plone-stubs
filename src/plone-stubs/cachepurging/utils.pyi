from _typeshed import Incomplete
from collections.abc import Generator

def isCachePurgingEnabled(registry=None):
    """Return True if caching is enabled"""

def getPathsToPurge(context, request) -> Generator[Incomplete, Incomplete]:
    """Given the current request and an object, look up paths to purge for
    the object and yield them one by one. An IPurgePathRewriter adapter may
    be used to rewrite the paths.
    """

def getURLsToPurge(path, proxies) -> Generator[Incomplete]:
    """Yield full purge URLs for a given path, taking the caching proxies
    listed in the registry into account.
    """
