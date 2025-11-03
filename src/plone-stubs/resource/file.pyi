from _typeshed import Incomplete
from ZPublisher.Iterators import filestream_iterator

class ResourceIterator(filestream_iterator):
    """Resource iterator that allows (inefficient) coercion to str/unicode.

    This is needed for ResourceRegistries support, for example.
    """
    def __unicode__(self): ...

class FilesystemFile:
    """Representation of a file. When called, it will set response headers
    and return the file's contents
    """

    path: Incomplete
    request: Incomplete
    __parent__: Incomplete
    lastModifiedTimestamp: Incomplete
    def __init__(self, parent, request, path, name) -> None: ...
    def getContentType(self, default: str = "application/octet-stream"): ...
    def __call__(self, REQUEST=None, RESPONSE=None): ...

class FileLastModified:
    """Determine when a file was last modified, for caching purposes"""

    context: Incomplete
    def __init__(self, context) -> None: ...
    def __call__(self): ...

def rawReadFile(context): ...
