from _typeshed import Incomplete
from persistent import Persistent

log: Incomplete
MAXCHUNKSIZE: Incomplete
IMAGE_INFO_BYTES: int
MAX_INFO_BYTES: Incomplete

class FileChunk(Persistent):
    """Wrapper for possibly large data"""

    next: Incomplete
    def __init__(self, data) -> None: ...
    def __getslice__(self, i, j): ...
    def __len__(self) -> int: ...
    __bytes__: Incomplete

FILECHUNK_CLASSES: Incomplete

class ModifiedPropertyMixin:
    @property
    def modified(self): ...

class NamedFile(Persistent, ModifiedPropertyMixin):
    """A non-BLOB file that stores a filename

    Let's test the constructor:

    >>> file = NamedFile()
    >>> file.contentType
    ''
    >>> file.data
    ''

    >>> file = NamedFile('Foobar')
    >>> file.contentType
    ''
    >>> file.data
    'Foobar'

    >>> file = NamedFile('Foobar', 'text/plain')
    >>> file.contentType
    'text/plain'
    >>> file.data
    'Foobar'

    >>> file = NamedFile(data='Foobar', contentType='text/plain')
    >>> file.contentType
    'text/plain'
    >>> file.data
    'Foobar'


    Let's test the mutators:

    >>> file = NamedFile()
    >>> file.contentType = 'text/plain'
    >>> file.contentType
    'text/plain'

    >>> file.data = 'Foobar'
    >>> file.data
    'Foobar'

    >>> file.data = None
    Traceback (most recent call last):
    ...
    TypeError: Cannot set None data on a file.


    Let's test large data input:

    >>> file = NamedFile()

    Insert as string:

    >>> file.data = 'Foobar'*60000
    >>> file.getSize()
    360000
    >>> file.data == 'Foobar'*60000
    True

    Insert data as FileChunk:

    >>> fc = FileChunk('Foobar'*4000)
    >>> file.data = fc
    >>> file.getSize()
    24000
    >>> file.data == 'Foobar'*4000
    True

    Insert data from file object:

    >>> from io import StringIO
    >>> sio = StringIO()
    >>> sio.write('Foobar'*100000)
    >>> sio.seek(0)
    >>> file.data = sio
    >>> file.getSize()
    600000
    >>> file.data == 'Foobar'*100000
    True


    Last, but not least, verify the interface:

    >>> from zope.interface.verify import verifyClass
    >>> INamedFile.implementedBy(NamedFile)
    True
    >>> verifyClass(INamedFile, NamedFile)
    True
    """

    filename: Incomplete
    data: Incomplete
    contentType: Incomplete
    def __init__(
        self, data: bytes = b"", contentType: str = "", filename=None
    ) -> None: ...
    def getSize(self):
        """See `IFile`"""

class NamedImage(NamedFile):
    """An non-BLOB image with a filename"""

    filename: Incomplete
    contentType: Incomplete
    exif_data: Incomplete
    def __init__(
        self, data: bytes = b"", contentType: str = "", filename=None
    ) -> None: ...
    def getImageSize(self):
        """See interface `IImage`"""
    data: Incomplete

class NamedBlobFile(Persistent, ModifiedPropertyMixin):
    """A file stored in a ZODB BLOB, with a filename"""

    filename: Incomplete
    contentType: Incomplete
    def __init__(
        self, data: bytes = b"", contentType: str = "", filename=None
    ) -> None: ...
    def open(self, mode: str = "r"): ...
    def openDetached(self): ...
    data: Incomplete
    @property
    def size(self): ...
    def getSize(self): ...

class NamedBlobImage(NamedBlobFile):
    """An image stored in a ZODB BLOB with a filename"""

    contentType: Incomplete
    exif: Incomplete
    def __init__(
        self, data: bytes = b"", contentType: str = "", filename=None
    ) -> None: ...
    data: Incomplete
    def getFirstBytes(self, start: int = 0, length=...):
        """Returns the first bytes of the file.

        Returns an amount which is sufficient to determine the image type.
        """
    def getImageSize(self):
        """See interface `IImage`"""
