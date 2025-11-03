from _typeshed import Incomplete
from plone.restapi.services import Service

zcatalog_version: Incomplete
SUPPORT_NOT_UUID_QUERIES: bool

class QuerystringSearch:
    """Returns the querystring search results given a p.a.querystring data."""

    context: Incomplete
    request: Incomplete
    def __init__(self, context, request) -> None: ...
    def __call__(self): ...

class QuerystringSearchPost(Service):
    """Returns the querystring search results given a p.a.querystring data."""
    def reply(self): ...

class QuerystringSearchGet(Service):
    """Returns the querystring search results given a p.a.querystring data."""
    def reply(self): ...
