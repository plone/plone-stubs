from .FSObject import FSObject
from _typeshed import Incomplete

class Warnings:
    messages: Incomplete
    def __init__(self) -> None: ...
    def write(self, message) -> None: ...

class FSReSTMethod(FSObject):
    """A chunk of StructuredText, rendered as a skin method of a CMF site."""

    meta_type: str
    report_level: int
    input_encoding: str
    output_encoding: str
    manage_options: Incomplete
    security: Incomplete
    manage_main: Incomplete
    class _func_code: ...
    __code__: Incomplete
    __defaults__: Incomplete
    index_html: Incomplete
    default_content_type: str
    def cook(self): ...
    def __call__(self, REQUEST={}, RESPONSE=None, **kw):
        """Return our rendered StructuredText."""
    @security.private
    def modified(self): ...
    def manage_FTPget(self):
        """Fetch our source for delivery via FTP."""
    def PrincipiaSearchSource(self):
        """Fetch our source for indexing in a catalog."""
    def document_src(self):
        """Fetch our source for rendering in the ZMI."""
