from _typeshed import Incomplete
from Acquisition import Implicit
from OFS.Cache import Cacheable
from OFS.role import RoleManager
from OFS.SimpleItem import Item

class FSObject(Implicit, Item, RoleManager, Cacheable):
    """FSObject is a base class for all filesystem based look-alikes.

    Subclasses of this class mimic ZODB based objects like Image and
    DTMLMethod, but are not directly modifiable from the management
    interface. They provide means to create a TTW editable copy, however.
    """

    title: str
    security: Incomplete
    id: Incomplete
    def __init__(self, id, filepath, fullname=None, properties=None) -> None: ...
    def manage_doCustomize(
        self, folder_path, RESPONSE=None, root=None, obj=None
    ) -> None:
        """Makes a ZODB Based clone with the same data.

        Calls _createZODBClone for the actual work.
        """
    def get_size(self):
        """Get the size of the underlying file."""
    def getModTime(self):
        """Return the last_modified date of the file we represent.

        Returns a DateTime instance.
        """
    def bobobase_modification_time(self):
        """Get the modification time the file did have last time it was read."""
    def getObjectFSPath(self):
        """Return the path of the file we represent"""

class BadFile(FSObject):
    """
    Represent a file which was not readable or parseable
    as its intended type.
    """

    meta_type: str
    icon: str
    BAD_FILE_VIEW: str
    manage_options: Incomplete
    exc_str: Incomplete
    file_contents: str
    def __init__(
        self, id, filepath, exc_str: str = "", fullname=None, properties=None
    ) -> None: ...
    security: Incomplete
    showError: Incomplete
    def manage_showError(self, REQUEST):
        """ """
    @security.public
    def getFileContents(self):
        """
        Return the contents of the file, if we could read it.
        """
    @security.public
    def getExceptionText(self):
        """
        Return the exception thrown while reading or parsing
        the file.
        """
