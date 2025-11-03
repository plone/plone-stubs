from _typeshed import Incomplete

import threading

logger: Incomplete

class DefaultPurger:
    timeout: Incomplete
    queues: Incomplete
    workers: Incomplete
    backlog: Incomplete
    queueLock: Incomplete
    errorHeaders: Incomplete
    def __init__(
        self, timeout=(3, 27), backlog: int = 0, errorHeaders=("x-squid-error",)
    ) -> None: ...
    def purge(self, session, url, httpVerb: str = "PURGE"):
        """Perform the single purge request.

        Returns a triple ``(resp, xcache, xerror)`` where ``resp`` is the
        response object for the connection, ``xcache`` is the contents of the
        X-Cache header, and ``xerror`` is the contents of the first header
        found of the header list in ``self.errorHeaders``.
        """
    def purgeSync(self, url, httpVerb: str = "PURGE"):
        """Purge synchronous.

        Fails if requests to cache fails.
        """
    def purgeAsync(self, url, httpVerb: str = "PURGE") -> None: ...
    def stopThreads(self, wait: bool = False): ...
    def getQueueAndWorker(self, url):
        """Create or retrieve a queue and a worker thread instance for the
        given URL.
        """
    @property
    def http_1_1(self): ...

class Worker(threading.Thread):
    """Worker thread for purging."""

    host: Incomplete
    scheme: Incomplete
    producer: Incomplete
    queue: Incomplete
    stopping: bool
    def __init__(self, queue, host, scheme, producer) -> None: ...
    def stop(self) -> None: ...
    def run(self) -> None: ...

DEFAULT_PURGER: Incomplete

def stopThreads() -> None: ...
