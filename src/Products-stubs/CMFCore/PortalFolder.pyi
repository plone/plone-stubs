from .CMFCatalogAware import OpaqueItemManager
from .DynamicType import DynamicType
from _typeshed import Incomplete
from OFS.Folder import Folder
from OFS.OrderSupport import OrderSupport

class PortalFolderBase(DynamicType, OpaqueItemManager, Folder):
    """Base class for portal folder."""

    security: Incomplete
    description: str
    manage_options: Incomplete
    id: Incomplete
    title: Incomplete
    def __init__(self, id, title: str = "", description: str = "") -> None: ...
    def Title(self):
        """Dublin Core Title element - resource name."""
    def Description(self):
        """Dublin Core Description element - resource summary."""
    def Type(self):
        """Dublin Core Type element - resource type."""
    def setTitle(self, title) -> None:
        """Set Dublin Core Title element - resource name."""
    def setDescription(self, description) -> None:
        """Set Dublin Core Description element - resource summary."""
    def edit(self, title: str = "", description: str = "") -> None:
        """
        Edit the folder title (and possibly other attributes later)
        """
    @security.public
    def allowedContentTypes(self):
        """
        List type info objects for types which can be added in
        this folder.
        """
    @security.public
    def contentItems(self, filter=None): ...
    @security.public
    def contentIds(self, filter=None): ...
    @security.public
    def contentValues(self, filter=None): ...
    def listFolderContents(self, contentFilter=None):
        """List viewable contentish and folderish sub-objects."""
    def listDAVObjects(self): ...
    @security.public
    def encodeFolderFilter(self, REQUEST):
        """
        Parse cookie string for using variables in dtml.
        """
    @security.public
    def decodeFolderFilter(self, encoded):
        """Parse cookie string for using variables in dtml.

        This is a public method and the input is not under our control.
        To prevent a DOS this method will refuse to decode data that seems
        conspicuously large.
        """
    def content_type(self) -> None:
        """
        WebDAV needs this to do the Right Thing (TM).
        """
    def PUT_factory(self, name, typ, body):
        """Factory for PUT requests to objects which do not yet exist.

        Used by NullResource.PUT.

        Returns -- Bare and empty object of the appropriate type (or None, if
        we don't know what to do)
        """
    def invokeFactory(self, type_name, id, RESPONSE=None, *args, **kw):
        """Invokes the portal_types tool."""
    def checkIdAvailable(self, id): ...
    def MKCOL_handler(self, id, REQUEST=None, RESPONSE=None) -> None:
        """
        Handle WebDAV MKCOL.
        """
    def manage_addFolder(self, id, title: str = "", REQUEST=None):
        """Add a new folder-like object with id *id*.

        IF present, use the parent object's 'mkdir' alias; otherwise, just add
        a PortalFolder.
        """

class PortalFolder(OrderSupport, PortalFolderBase):
    """Implements portal content management, but not UI details."""

    portal_type: str
    security: Incomplete
    manage_options: Incomplete
    def manage_addPortalFolder(self, id, title: str = "", REQUEST=None):
        """Add a new PortalFolder object with id *id*."""

PortalFolderFactory: Incomplete
manage_addPortalFolder: Incomplete

class ContentFilter:
    """Represent a predicate against a content object's metadata."""

    MARKER: Incomplete
    filterSubject: Incomplete
    predicates: Incomplete
    description: Incomplete
    def __init__(
        self,
        Title=...,
        Creator=...,
        Subject=...,
        Description=...,
        created=...,
        created_usage: str = "range:min",
        modified=...,
        modified_usage: str = "range:min",
        Type=...,
        portal_type=...,
        **Ignored,
    ) -> None: ...
    def hasSubject(self, obj):
        """
        Converts Subject string into a List for content filter view.
        """
    def __call__(self, content): ...
