from _typeshed import Incomplete
from OFS.Folder import Folder
from Persistence import Persistent

logger: Incomplete
__reload_module__: int
base_ignore: Incomplete
ignore: Incomplete
ignore_re: Incomplete

class _walker:
    ignore: Incomplete
    def __init__(self, ignore) -> None: ...
    def __call__(self, dirlist, dirname, names) -> None: ...

class DirectoryInformation:
    data: Incomplete
    use_dir_mtime: bool
    ignore: Incomplete
    subdirs: Incomplete
    def __init__(self, filepath, reg_key, ignore=...) -> None: ...
    def getSubdirs(self): ...
    def reload(self) -> None: ...
    objects: Incomplete
    def getContents(self, registry): ...
    def prepareContents(self, registry): ...

class DirectoryRegistry:
    def __init__(self) -> None: ...
    def registerFileExtension(self, ext, klass) -> None: ...
    def registerMetaType(self, mt, klass) -> None: ...
    def getTypeByExtension(self, ext): ...
    def getTypeByMetaType(self, mt): ...
    def registerDirectory(
        self, name, _prefix, subdirs: int = 1, ignore=...
    ) -> None: ...
    def registerDirectoryByKey(
        self, filepath, reg_key, subdirs: int = 1, ignore=...
    ) -> None: ...
    def reloadDirectory(self, reg_key) -> None: ...
    def getDirectoryInfo(self, reg_key): ...
    def listDirectories(self): ...

registerDirectory: Incomplete
registerFileExtension: Incomplete
registerMetaType: Incomplete

def listFolderHierarchy(
    ob, path, rval, adding_meta_type=None, max: int = 0
) -> None: ...

class DirectoryView(Persistent):
    """Directory views mount filesystem directories."""

    meta_type: str
    id: Incomplete
    def __init__(
        self, id, reg_key: str = "", fullname=None, properties=None
    ) -> None: ...
    def __of__(self, parent): ...
    def getId(self): ...

class DirectoryViewSurrogate(Folder):
    """Folderish DirectoryView."""

    meta_type: str
    zmi_icon: str
    all_meta_types: Incomplete
    security: Incomplete
    def __init__(self, real, data, objects) -> None: ...
    def __setattr__(self, name, value) -> None: ...
    def __delattr__(self, name) -> None: ...
    manage_propertiesForm: Incomplete
    def manage_properties(self, reg_key, REQUEST=None) -> None:
        """Update the directory path of the DirectoryView."""
    def getCustomizableObject(self): ...
    def listCustFolderPaths(self, adding_meta_type=None, max: int = 0):
        """List possible customization folders as key, value pairs."""
    def getDirPath(self): ...
    @security.public
    def getId(self): ...

manage_addDirectoryViewForm: Incomplete

def createDirectoryView(parent, reg_key, id=None) -> None:
    """Add either a DirectoryView or a derivative object."""

def addDirectoryViews(ob, name, _prefix) -> None:
    """Add a directory view for every subdirectory of the given directory.

    Meant to be called by filesystem-based code. Note that registerDirectory()
    still needs to be called by product initialization code to satisfy
    persistence demands.
    """

def manage_addDirectoryView(self, reg_key, id=None, REQUEST=None):
    """Add either a DirectoryView or a derivative object."""

def manage_listAvailableDirectories(*args):
    """List registered directories."""
