from .FSObject import FSObject
from _typeshed import Incomplete
from Products.PageTemplates.PageTemplate import PageTemplate
from Shared.DC.Scripts.Script import Script

xml_detect_re: Incomplete
charset_re: Incomplete

class FSPageTemplate(FSObject, Script, PageTemplate):
    """Wrapper for Page Template."""

    meta_type: str
    zmi_icon: str
    manage_options: Incomplete
    security: Incomplete
    manage_main: Incomplete
    def __init__(self, id, filepath, fullname=None, properties=None) -> None: ...
    @security.private
    def read(self): ...
    expand: int
    output_encoding: str
    __defaults__: Incomplete
    __code__: Incomplete
    def pt_macros(self): ...
    def pt_render(self, source: int = 0, extra_context={}): ...
    def pt_source_file(self):
        """Return a file name to be compiled into the TAL code."""
    manage_FTPget: Incomplete
    get_size: Incomplete
    getSize = get_size
    PrincipiaSearchSource: Incomplete
    document_src: Incomplete
    pt_getContext: Incomplete
    source_dot_xml: Incomplete
