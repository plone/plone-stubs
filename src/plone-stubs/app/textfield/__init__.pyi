from _typeshed import Incomplete
from zope.schema import Object

_: Incomplete

class RichText(Object):
    """Text field that also stores MIME type"""

    default_mime_type: str
    output_mime_type: str
    allowed_mime_types: Incomplete
    max_length: Incomplete
    def __init__(
        self,
        default_mime_type: str = "text/html",
        output_mime_type: str = "text/x-html-safe",
        allowed_mime_types=None,
        max_length=None,
        schema=...,
        **kw,
    ) -> None: ...
    def fromUnicode(self, str_val): ...
