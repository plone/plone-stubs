from _typeshed import Incomplete

class APIError(Exception):
    """Base class for exceptions raised by plone.restapi."""

class DeserializationError(Exception):
    """An error happened during deserialization of content."""

    msg: Incomplete
    def __init__(self, msg) -> None: ...

class QueryParsingError(Exception):
    """An error happened while parsing a search query."""
