from _typeshed import Incomplete
from Products.Five.browser import BrowserView

ALLOWED_INLINE_MIMETYPES: Incomplete
DISALLOWED_INLINE_MIMETYPES: Incomplete
USE_DENYLIST: Incomplete

class Download(BrowserView):
    """Download a file, via ../context/@@download/fieldname/filename

    `fieldname` is the name of an attribute on the context that contains
    the file. `filename` is the filename that the browser will be told to
    give the file. If not given, it will be looked up from the field.

    The attribute under `fieldname` should contain a named (blob) file/image
    instance from this package.

    If no `fieldname` is supplied, then a default field is looked up through
    adaption to `plone.rfc822.interfaces.IPrimaryFieldInfo`.
    """

    fieldname: Incomplete
    filename: Incomplete
    def __init__(self, context, request) -> None: ...
    def publishTraverse(self, request, name): ...
    def __call__(self): ...
    def handle_request_range(self, file): ...
    def get_canonical(self, file): ...
    def set_headers(self, file) -> None: ...

class DisplayFile(Download):
    """Display a file, via ../context/@@display-file/fieldname/filename

    Same as Download, however in this case we don't set the filename so the
    browser can decide to display the file instead.
    """

    allowed_inline_mimetypes = ALLOWED_INLINE_MIMETYPES
    disallowed_inline_mimetypes = DISALLOWED_INLINE_MIMETYPES
    use_denylist = USE_DENYLIST
    def set_headers(self, file): ...
