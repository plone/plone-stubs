from .FSObject import FSObject
from _typeshed import Incomplete

class FSImage(FSObject):
    """FSImages act like images but are not directly
    modifiable from the management interface."""

    meta_type: str
    zmi_icon: str
    content_type: str
    alt: str
    height: str
    width: str
    manage_options: Incomplete
    security: Incomplete
    manage_main: Incomplete
    def __init__(self, id, filepath, fullname=None, properties=None) -> None: ...
    def tag(self, *args, **kw): ...
    def index_html(self, REQUEST, RESPONSE):
        """
        The default view of the contents of a File or Image.

        Returns the contents of the file or image.  Also, sets the
        Content-Type HTTP header to the objects content type.
        """
    def modified(self): ...
    def getContentType(self):
        """Get the content type of a file or image.

        Returns the content type (MIME type) of a file or image.
        """
    def get_size(self):
        """
        Return the size of the image.
        """
    manage_FTPget = index_html
