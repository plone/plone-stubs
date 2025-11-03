from _typeshed import Incomplete
from zope.cachedescriptors import property as zproperty
from zope.publisher.browser import BrowserView

_: Incomplete

def authorize(context, request) -> None: ...

invalidFilenameChars: Incomplete

def validateFilename(name): ...

class FileManagerActions(BrowserView):
    imageExtensions: Incomplete
    previewTemplate: Incomplete
    @zproperty.Lazy
    def resourceDirectory(self): ...
    def getObject(self, path): ...
    def getExtension(self, obj=None, path=None): ...
    def getFolder(self, path):
        """Returns a dict of file and folder objects representing the
        contents of the given directory (indicated by a "path" parameter). The
        values are dicts as returned by getInfo().

        A boolean parameter "getsizes" indicates whether image dimensions
        should be returned for each item. Folders should always be returned
        before files.

        Optionally a "type" parameter can be specified to restrict returned
        files (depending on the connector). If a "type" parameter is given for
        the HTML document, the same parameter value is reused and passed
        to getFolder(). This can be used for example to only show image files
        in a file system tree.
        """
    def getFile(self, path): ...
    def normalizePath(self, path): ...
    def normalizeReturnPath(self, path): ...
    def parentPath(self, path): ...
    def getInfo(self, obj, path: str = "/"):
        """Returns information about a single file. Requests
        with mode "getinfo" will include an additional parameter, "path",
        indicating which file to inspect. A boolean parameter "getsize"
        indicates whether the dimensions of the file (if an image) should be
        returned.
        """
    def saveFile(self, path, value): ...
    def addFolder(self, path, name):
        """Create a new directory on the server within the given path."""
    def addFile(self, path, name):
        """Add a new empty file in the given directory"""
    def delete(self, path):
        """Delete the item at the given path."""
    def renameFile(self, path, newName):
        """Rename the item at the given path to the new name"""
    def move(self, path, directory):
        """Move the item at the given path to a new directory"""
    def do_action(self, action): ...
    def download(self, path):
        """Serve the requested file to the user"""
    def __call__(self): ...

class FileManager(BrowserView):
    """Render the file manager and support its AJAX requests."""

    previewTemplate: Incomplete
    staticFiles: str
    imageExtensions: Incomplete
    knownExtensions: Incomplete
    capabilities: Incomplete
    extensionsWithIcons: Incomplete
    protectedActions: Incomplete
    def pattern_options(self): ...
    def mode_selector(self, form): ...
    def __call__(self): ...
    def setup(self) -> None: ...
    @zproperty.Lazy
    def portalUrl(self): ...
    @zproperty.Lazy
    def resourceDirectory(self): ...
    @zproperty.Lazy
    def resourceType(self): ...
    @zproperty.Lazy
    def baseUrl(self): ...
    @zproperty.Lazy
    def fileConnector(self): ...
    @zproperty.Lazy
    def filemanagerConfiguration(self): ...
    def normalizePath(self, path): ...
    def normalizeReturnPath(self, path): ...
    def parentPath(self, path): ...
    def getFolder(self, path, getSizes: bool = False):
        """Returns a dict of file and folder objects representing the
        contents of the given directory (indicated by a "path" parameter). The
        values are dicts as returned by getInfo().

        A boolean parameter "getsizes" indicates whether image dimensions
        should be returned for each item. Folders should always be returned
        before files.

        Optionally a "type" parameter can be specified to restrict returned
        files (depending on the connector). If a "type" parameter is given for
        the HTML document, the same parameter value is reused and passed
        to getFolder(). This can be used for example to only show image files
        in a file system tree.
        """
    def getInfo(self, path, getSize: bool = False):
        """Returns information about a single file. Requests
        with mode "getinfo" will include an additional parameter, "path",
        indicating which file to inspect. A boolean parameter "getsize"
        indicates whether the dimensions of the file (if an image) should be
        returned.
        """
    def addFolder(self, path, name):
        """Create a new directory on the server within the given path."""
    def add(self, path, newfile, replacepath=None):
        """Add the uploaded file to the specified path. Unlike
        the other methods, this method must return its JSON response wrapped in
        an HTML <textarea>, so the MIME type of the response is text/html
        instead of text/plain. The upload form in the File Manager passes the
        current path as a POST param along with the uploaded file. The response
        includes the path as well as the name used to store the file. The
        uploaded file's name should be safe to use as a path component in a
        URL, so URL-encoded at a minimum.
        """
    def addNew(self, path, name):
        """Add a new empty file in the given directory"""
    def rename(self, path, newName):
        """Rename the item at the given path to the new name"""
    def delete(self, path):
        """Delete the item at the given path."""
    def move(self, path, directory):
        """Move the item at the given path to a new directory"""
    def download(self, path):
        """Serve the requested file to the user"""
    def getObject(self, path): ...
    def getExtension(self, path, obj): ...
    def getFile(self, path): ...
    def saveFile(self, path, value): ...
    def filetree(self): ...
