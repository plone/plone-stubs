from _typeshed import Incomplete
from Acquisition import Implicit
from webdav.Resource import Resource

class DAVResourceMixin:
    """Mixin class for WebDAV resource support.

    The main purpose of this class is to implement the Zope 2 WebDAV API to
    delegate to more granular adapters.
    """

    security: Incomplete
    def get_size(self): ...
    def getSize(self): ...
    def content_type(self): ...
    def Format(self): ...
    def manage_DAVget(self):
        """Get the body of the content item in a WebDAV response."""
    def manage_FTPget(self, REQUEST=None, RESPONSE=None):
        """Return the body of the content item in an FTP or WebDAV response.

        This adapts self to IRawReadFile(), which is then returned as an
        iterator. The adapter should provide IStreamIterator.
        """
    def PUT(self, REQUEST=None, RESPONSE=None):
        """WebDAV method to replace self with a new resource. This is also
        used when initialising an object just created from a NullResource.

        This will look up an IRawWriteFile adapter on self and write to it,
        line-by-line, from the request body.
        """

class DAVCollectionMixin(DAVResourceMixin):
    """Mixin class for WebDAV collection support.

    The main purpose of this class is to implement the Zope 2 WebDAV API to
    delegate to more granular adapters.
    """

    security: Incomplete
    def MKCOL_handler(self, id, REQUEST=None, RESPONSE=None) -> None:
        """Handle "make collection" by delegating to an IDirectoryFactory
        adapter.
        """
    def PUT_factory(self, name, contentType, body):
        """Handle constructing a new object upon a PUT request by delegating
        to an IFileFactory adapter
        """
    def listDAVObjects(self):
        """Return objects for WebDAV folder listings.

        We add a non-folderish pseudo object which contains the "body" data
        for this container.
        """

class FolderDataResource(Implicit, Resource):
    """This object is a proxy which is created on-demand during traversal,
    to allow access to the "file-like" aspects of a container type.

    When a Container object is listed via WebDAV, the first item in the folder
    listing is an instance of this class with an id of \'_data\'. When
    requested, the default Dexterity IPublishTraverse adapter will also return
    an instance (the instances are non-persistent). A GET, PUT, HEAD, LOCK,
    UNLOCK, PROPFIND or PROPPATCH request against this resource will be
    treated as if it were a request against the parent object, treating it
    as a resource (file) rather than a collection (folder).
    """

    __dav_collection__: int
    security: Incomplete
    def __init__(self, name, parent) -> None: ...
    def __getattr__(self, name): ...
    def __setattr__(self, name, value) -> None: ...
    @property
    def id(self): ...
    def getId(self): ...
    def HEAD(self, REQUEST, RESPONSE):
        """HEAD request: use the Resource algorithm on the data of the
        parent.
        """
    def OPTIONS(self, REQUEST, RESPONSE):
        """OPTIONS request: delegate to parent"""
    def TRACE(self, REQUEST, RESPONSE):
        """TRACE request: delegate to parent"""
    def PROPFIND(self, REQUEST, RESPONSE):
        """PROPFIND request: use Resource algorithm on self, so that we do
        not appear as a folder.

        Certain things may be acquired, notably .propertysheets
        """
    def PROPPATCH(self, REQUEST, RESPONSE):
        """PROPPATCH request: Use Resource algorithm on self, so that we do
        not appear as a folder.

        Certain things may be acquired, notably .propertysheets
        """
    def LOCK(self, REQUEST, RESPONSE):
        """LOCK request: delegate to parent"""
    def UNLOCK(self, REQUEST, RESPONSE):
        """UNLOCK request: delegate to parent"""
    def PUT(self, REQUEST, RESPONSE):
        """PUT request: delegate to parent"""
    def MKCOL(self, REQUEST, RESPONSE) -> None:
        """MKCOL request: not allowed"""
    def DELETE(self, REQUEST, RESPONSE) -> None:
        """DELETE request: not allowed"""
    def COPY(self, REQUEST, RESPONSE) -> None:
        """COPY request: not allowed"""
    def MOVE(self, REQUEST, RESPONSE) -> None:
        """MOVE request: not allowed"""
    def manage_DAVget(self):
        """DAV content access: delete to manage_FTPget()"""
    def manage_FTPget(self):
        """FTP access: delegate to parent"""
    def listDAVObjects(self):
        """DAV object listing: return nothing"""

class StringStreamIterator:
    """Simple stream iterator to allow efficient data streaming."""

    file: Incomplete
    size: Incomplete
    chunk: Incomplete
    def __init__(self, data, size=None, chunk=...) -> None:
        """Consume data (a str) into a temporary file and prepare streaming.

        size is the length of the data. If not given, the length of the data
        string is used.

        chunk is the chunk size for the iterator
        """
    def __iter__(self): ...
    def next(self): ...
    def __len__(self) -> int: ...

class DefaultDirectoryFactory:
    """Default directory factory, invoked when an FTP/WebDAV operation
    attempts to create a new folder via a MKCOL request.

    The default implementation simply calls manage_addFolder().
    """

    context: Incomplete
    def __init__(self, context) -> None: ...
    def __call__(self, name) -> None: ...

class DefaultFileFactory:
    """Default file factory, invoked when an FTP/WebDAV operation
    attempts to create a new resource via a PUT request.

    The default implementation uses the content_type_registry to find a
    type to add, and then creates an instance using the portal_types
    tool.
    """

    context: Incomplete
    def __init__(self, context) -> None: ...
    def __call__(self, name, contentType, data): ...

class ReadFileBase:
    """Convenience base class for read files which delegate to another stream
    type (e.g. a temporary file or StringIO)

    Override _getStream() and any required methods.
    """

    context: Incomplete
    def __init__(self, context) -> None: ...
    mimeType: Incomplete
    encoding: str
    name: Incomplete
    @property
    def closed(self): ...
    def size(self): ...
    def seek(self, offset, whence=None) -> None: ...
    def tell(self): ...
    def close(self) -> None: ...
    def read(self, size=None): ...
    def readline(self, size=None): ...
    def readlines(self, sizehint=None): ...
    def __iter__(self): ...
    def next(self): ...

class DefaultReadFile(ReadFileBase):
    """IRawReadFile adapter for Dexterity objects.

    Uses RFC822 marshaler.

    This is also marked as an IStreamIterator, which means that it is safe
    to return it to the publisher directly. In particular, the size() method
    will return an accurate file size.
    """

    context: Incomplete
    def __init__(self, context) -> None: ...
    @property
    def mimeType(self): ...
    @property
    def encoding(self): ...
    @property
    def name(self): ...
    def size(self): ...
    __len__ = size
    def __next__(self):
        """Iterate over the stream"""

class WriteFileBase:
    """Convenience base class for write files which delegate to another
    stream, e.g. a file or StringIO.

    Implement _getStream() and override any methods required.
    """

    context: Incomplete
    def __init__(self, context) -> None: ...
    mimeType: Incomplete
    encoding: str
    name: Incomplete
    @property
    def closed(self): ...
    def seek(self, offset, whence=None) -> None: ...
    def tell(self): ...
    def close(self) -> None: ...
    def write(self, data) -> None: ...
    def writelines(self, sequence) -> None: ...
    def truncate(self, size=None) -> None: ...
    def flush(self) -> None: ...

class DefaultWriteFile:
    """IRawWriteFile file adapter for Dexterity objects.

    Uses RFC822 marshaler.
    """

    context: Incomplete
    def __init__(self, context) -> None: ...
    @property
    def mimeType(self): ...
    @mimeType.setter
    def mimeType(self, value) -> None: ...
    @property
    def encoding(self): ...
    @encoding.setter
    def encoding(self, value) -> None: ...
    @property
    def closed(self): ...
    @property
    def name(self): ...
    @name.setter
    def name(self, value) -> None: ...
    def seek(self, offset, whence=None) -> None: ...
    def tell(self): ...
    def close(self) -> None: ...
    def write(self, data) -> None: ...
    def writelines(self, sequence) -> None: ...
    def truncate(self, size=None) -> None: ...
    def flush(self) -> None: ...
