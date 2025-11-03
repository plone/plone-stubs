from Products.CMFCore.interfaces import IDublinCore
from zope.interface.common.sequence import IReadSequence

class IContentListing(IReadSequence):
    """Sequence of IContentListingObjects."""

class IContentListingObject(IDublinCore):
    """Unified representation of content objects in listings."""
    def getDataOrigin() -> None:
        """The origin of the data for the object."""
    def getObject() -> None:
        """get the real object (may be expensive)."""
    def getId() -> None:
        """get the object id in its container."""
    def getPath() -> None:
        """Path to the object, relative to the portal root."""
    def getURL(relative: bool = False) -> None:
        """Full url to the object, including the portal root."""
    def uuid() -> None:
        """Unique content identifier."""
    def getSize() -> None:
        """size in bytes."""
    def review_state() -> None:
        """Workflow review state."""
    def Title() -> None:
        """Title."""
    def Description() -> None:
        """Description."""
    def CroppedDescription() -> None:
        """A cropped description."""
    def Type() -> None:
        """Type title."""
    def PortalType() -> None:
        """Content type id of the object."""
    def listCreators() -> None:
        """List creators of the object."""
    def getUserData(username) -> None:
        """Get some data of a given user."""
    def Creator() -> None:
        """Creator of the object."""
    def Author() -> None:
        """Author of the object."""
    def Subject() -> None:
        """Subject(s) of the object."""
    def Date() -> None:
        """Date of the object."""
    def CreationDate() -> None:
        """Creation date of the object."""
    def EffectiveDate() -> None:
        """Date, when content will be shown in listings."""
    def ExpirationDate() -> None:
        """Date, when content will be removed from listings."""
    def ModificationDate() -> None:
        """Date, when object was last modified."""
    def Language() -> None:
        """Language of the object."""
    def ContentTypeClass() -> None:
        """The contenttype suitable as a css class name, matching Plone
        conventions.
        """
    def MimeTypeIcon() -> None:
        """return mimetype icon from mimetype registry if contenttype is
        File else None
        """
