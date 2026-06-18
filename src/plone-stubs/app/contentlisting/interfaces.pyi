from Products.CMFCore.interfaces import IDublinCore
from zope.interface.common.sequence import IReadSequence

class IContentListing(IReadSequence):
    """Sequence of IContentListingObjects."""

class IContentListingObject(IDublinCore):
    """Unified representation of content objects in listings."""
    def getDataOrigin(self) -> None:
        """The origin of the data for the object."""
    def getObject(self) -> None:
        """get the real object (may be expensive)."""
    def getId(self) -> None:
        """get the object id in its container."""
    def getPath(self) -> None:
        """Path to the object, relative to the portal root."""
    def getURL(self, relative: bool = False) -> None:
        """Full url to the object, including the portal root."""
    def uuid(self) -> None:
        """Unique content identifier."""
    def getSize(self) -> None:
        """size in bytes."""
    def review_state(self) -> None:
        """Workflow review state."""
    def Title(self) -> None:
        """Title."""
    def Description(self) -> None:
        """Description."""
    def CroppedDescription(self) -> None:
        """A cropped description."""
    def Type(self) -> None:
        """Type title."""
    def PortalType(self) -> None:
        """Content type id of the object."""
    def listCreators(self) -> None:
        """List creators of the object."""
    def getUserData(self, username) -> None:
        """Get some data of a given user."""
    def Creator(self) -> None:
        """Creator of the object."""
    def Author(self) -> None:
        """Author of the object."""
    def Subject(self) -> None:
        """Subject(s) of the object."""
    def Date(self) -> None:
        """Date of the object."""
    def CreationDate(self) -> None:
        """Creation date of the object."""
    def EffectiveDate(self) -> None:
        """Date, when content will be shown in listings."""
    def ExpirationDate(self) -> None:
        """Date, when content will be removed from listings."""
    def ModificationDate(self) -> None:
        """Date, when object was last modified."""
    def Language(self) -> None:
        """Language of the object."""
    def ContentTypeClass(self) -> None:
        """The contenttype suitable as a css class name, matching Plone
        conventions.
        """
    def MimeTypeIcon(self) -> None:
        """return mimetype icon from mimetype registry if contenttype is
        File else None
        """
