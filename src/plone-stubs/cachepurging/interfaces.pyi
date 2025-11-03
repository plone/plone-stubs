from _typeshed import Incomplete
from zope.interface import Interface

_: Incomplete

class ICachePurgingSettings(Interface):
    """Settings used by the purging algorithm.

    Should be installed into ``plone.registry``.
    """

    enabled: Incomplete
    cachingProxies: Incomplete
    virtualHosting: Incomplete
    domains: Incomplete

class IPurgePathRewriter(Interface):
    """Used to rewrite paths for purging. This should be registered as an
    adapter on the request.

    The same instance may be reused several times in the same request.
    """
    def __call__(path) -> None:
        """Given a relative path, return a list of paths to purge (e.g. if
        there are multiple variants). The returned paths should not have a
        domain component, but should be relative to the domain root, e.g.
        /path/to/view. Return an empty list if there is nothing to purge.
        """

class IPurger(Interface):
    """A utility used to manage the purging process."""
    def purgeAsync(url, httpVerb: str = "PURGE") -> None:
        """Send a PURGE request to a particular URL asynchronously in a
        worker thread.
        """
    def purgeSync(url, httpVerb: str = "PURGE") -> None:
        """Send a PURGE request to a particular URL synchronosly.

        Returns a triple ``(status, xcache, xerror)`` where ``status`` is
        the HTTP status of the purge request, ``xcache`` is the contents of
        the ``x-cache`` response header, and ``x-error`` is the contents
        of the first header found from the list of headers in
        ``errorHeaders``.
        """
    def stopThreads(wait: bool = False) -> None:
        """Attempts to stop all threads.  Threads stop immediately after
        the current item is being processed.

        Returns True if successful, or False if threads are still running
        after waiting 5 seconds for each one.
        """
    errorHeaders: Incomplete
    http_1_1: Incomplete
