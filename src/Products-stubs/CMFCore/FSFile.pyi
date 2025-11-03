from .FSObject import FSObject
from _typeshed import Incomplete

class FSFile(FSObject):
    """FSFiles act like images but are not directly
    modifiable from the management interface."""

    meta_type: str
    zmi_icon: str
    content_type: str
    manage_options: Incomplete
    security: Incomplete
    manage_main: Incomplete
    def __init__(self, id, filepath, fullname=None, properties=None) -> None: ...
    def __bytes__(self) -> bytes: ...
    def modified(self): ...
    def index_html(self, REQUEST, RESPONSE):
        """
        The default view of the contents of a File or Image.

        Returns the contents of the file or image.  Also, sets the
        Content-Type HTTP header to the objects content type.
        """
    def getContentType(self):
        """Get the content type of a file or image.

        Returns the content type (MIME type) of a file or image.
        """
    manage_FTPget = index_html
