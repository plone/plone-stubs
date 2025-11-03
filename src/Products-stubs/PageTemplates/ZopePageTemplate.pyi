from _typeshed import Incomplete
from Acquisition import Acquired
from Acquisition import Explicit
from OFS.Cache import Cacheable
from OFS.History import Historical
from OFS.PropertyManager import PropertyManager
from OFS.Traversable import Traversable
from Products.PageTemplates.PageTemplate import PageTemplate
from Shared.DC.Scripts.Script import Script
from ZPublisher import zpublish

preferred_encodings: Incomplete

class Src(Explicit):
    """I am scary code"""

    security: Incomplete
    PUT = Acquired
    document_src = Acquired
    index_html: Incomplete
    def __before_publishing_traverse__(self, ob, request) -> None: ...
    def __call__(self, REQUEST, RESPONSE):
        """ """

class ZopePageTemplate(
    Script, PageTemplate, Historical, Cacheable, Traversable, PropertyManager
):
    """Zope wrapper for Page Template using TAL, TALES, and METAL"""

    meta_type: str
    zmi_icon: str
    output_encoding: str
    __code__: Incomplete
    __defaults__: Incomplete
    manage_options: Incomplete
    security: Incomplete
    id: Incomplete
    expand: int
    def __init__(
        self,
        id,
        text=None,
        content_type: str = "text/html",
        strict: bool = True,
        output_encoding: str = "utf-8",
    ) -> None: ...
    def pt_edit(
        self, text, content_type, keep_output_encoding: bool = False
    ) -> None: ...
    pt_editForm: Incomplete
    manage = pt_editForm
    manage_main = pt_editForm
    source_dot_xml: Incomplete
    @zpublish
    def pt_editAction(self, REQUEST, title, text, content_type, expand: int = 0):
        """Change the title and document."""
    def pt_setTitle(self, title, encoding: str = "utf-8") -> None: ...
    @zpublish
    def pt_upload(self, REQUEST, file: str = "", encoding: str = "utf-8"):
        """Replace the document with the text in file."""
    def ZScriptHTML_tryParams(self):
        """Parameters to test the script with."""
    def manage_historyCompare(
        self, rev1, rev2, REQUEST, historyComparisonResults: str = ""
    ): ...
    def pt_getContext(self, *args, **kw): ...
    def write(self, text) -> None: ...
    def html(self): ...
    def get_size(self): ...
    getSize = get_size
    def PrincipiaSearchSource(self):
        """Support for searching - the document's contents are searched."""
    def document_src(self, REQUEST=None, RESPONSE=None):
        """Return expanded document source."""
    def pt_source_file(self):
        """Returns a file name to be compiled into the TAL code."""
    def pt_render(self, source: bool = False, extra_context={}): ...
    @zpublish
    def PUT(self, REQUEST, RESPONSE):
        """Handle HTTP PUT requests"""

manage_addPageTemplateForm: Incomplete

def manage_addPageTemplate(
    self,
    id,
    title: str = "",
    text: str = "",
    encoding: str = "utf-8",
    submit=None,
    REQUEST=None,
    RESPONSE=None,
):
    """Add a Page Template with optional file content."""

def initialize(context) -> None: ...
