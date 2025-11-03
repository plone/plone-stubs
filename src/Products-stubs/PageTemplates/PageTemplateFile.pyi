from _typeshed import Incomplete
from OFS.SimpleItem import SimpleItem
from OFS.Traversable import Traversable
from Products.PageTemplates.PageTemplate import PageTemplate
from Shared.DC.Scripts.Script import Script

LOG: Incomplete

def guess_type(filename, body): ...

class PageTemplateFile(SimpleItem, Script, PageTemplate, Traversable):
    """Zope 2 implementation of a PageTemplate loaded from a file."""

    meta_type: str
    __code__: Incomplete
    __defaults__: Incomplete
    security: Incomplete
    encoding: Incomplete
    id: Incomplete
    filename: Incomplete
    def __init__(self, filename, _prefix=None, encoding=..., **kw) -> None: ...
    def pt_getContext(self): ...
    def pt_macros(self): ...
    def pt_source_file(self):
        """Returns a file name to be compiled into the TAL code."""
    def document_src(self, REQUEST=None, RESPONSE=None):
        """Return expanded document source."""
    __roles__: Incomplete
    def getOwner(self, info: int = 0) -> None:
        """Gets the owner of the executable object.

        This method is required of all objects that go into
        the security context stack.  Since this object came from the
        filesystem, it is owned by no one managed by Zope.
        """
