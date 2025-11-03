from _typeshed import Incomplete
from Products.MimetypesRegistry.MimeTypeItem import MimeTypeItem

__all__ = [
    "application_msword",
    "application_octet_stream",
    "application_rtf",
    "text_html",
    "text_html_safe",
    "text_plain",
    "text_pre_plain",
    "text_python",
    "text_rest",
    "text_structured",
    "text_web_intelligent",
    "text_web_markdown",
    "text_web_textile",
    "text_wiki",
    "text_xml",
]

class text_plain(MimeTypeItem):
    mimetypes: Incomplete
    extensions: Incomplete
    binary: int

class text_pre_plain(MimeTypeItem):
    mimetypes: Incomplete
    extensions: Incomplete
    binary: int

class text_structured(MimeTypeItem):
    mimetypes: Incomplete
    extensions: Incomplete
    binary: int

class text_rest(MimeTypeItem):
    mimetypes: Incomplete
    extensions: Incomplete
    binary: int

class text_python(MimeTypeItem):
    mimetypes: Incomplete
    extensions: Incomplete
    binary: int

class text_wiki(MimeTypeItem):
    mimetypes: Incomplete
    extensions: Incomplete
    binary: int

class application_rtf(MimeTypeItem):
    mimetypes: Incomplete
    extensions: Incomplete
    binary: int

class application_msword(MimeTypeItem):
    mimetypes: Incomplete
    extensions: Incomplete
    binary: int

class text_xml(MimeTypeItem):
    mimetypes: Incomplete
    extensions: Incomplete
    binary: int
    def classify(self, data): ...

class application_octet_stream(MimeTypeItem):
    mimetypes: Incomplete
    binary: int
    extensions: Incomplete

class text_html(MimeTypeItem):
    mimetypes: Incomplete
    extensions: Incomplete
    binary: int

class text_html_safe(MimeTypeItem):
    mimetypes: Incomplete
    extensions: Incomplete
    binary: int

class text_web_intelligent(MimeTypeItem):
    mimetypes: Incomplete
    extensions: Incomplete
    binary: int

class text_web_markdown(MimeTypeItem):
    mimetypes: Incomplete
    extensions: Incomplete
    binary: int

class text_web_textile(MimeTypeItem):
    mimetypes: Incomplete
    extensions: Incomplete
    binary: int
