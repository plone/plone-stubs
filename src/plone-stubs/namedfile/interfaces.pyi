from _typeshed import Incomplete
from zope.interface import Interface
from zope.schema.interfaces import IObject

_: Incomplete
HAVE_BLOBS: bool

class ITyped(Interface):
    contentType: Incomplete

class IFile(Interface):
    data: Incomplete
    def getSize() -> None:
        """Return the byte-size of the data of the object."""

class IImage(IFile):
    """This interface defines an Image that can be displayed."""
    def getImageSize() -> None:
        """Return a tuple (x, y) that describes the dimensions of
        the object.
        """

class IImageScaleTraversable(Interface):
    """Marker for items that should provide access to image scales for named
    image fields via the @@images view.
    """

class IAvailableSizes(Interface):
    """A callable returning a dictionary of scale name => (width, height)"""

class IStableImageScale(Interface):
    """Marker for image scales when accessed with a UID-based URL.
    These can be cached forever using the plone.stableResource ruleset.
    """

class IPluggableBinaryFieldValidation(Interface):
    def __call__(field, value) -> None:
        """validates field and value.

        raises zope.schema.ValidationError
        returns None
        """

class IPluggableFileFieldValidation(IPluggableBinaryFieldValidation):
    """pluggable validation for binary File fields"""

class IPluggableImageFieldValidation(IPluggableBinaryFieldValidation):
    """pluggable validation for binary Image fields"""

class INamed(Interface):
    """An item with a filename"""

    filename: Incomplete

class INamedTyped(INamed, ITyped):
    """An item with a filename and contentType"""

class INamedFile(INamedTyped, IFile):
    """A non-BLOB file with a filename"""

class INamedImage(INamedTyped, IImage):
    """A non-BLOB image with a filename"""

class INamedField(IObject):
    """Base field type"""

class INamedFileField(INamedField):
    """Field for storing INamedFile objects."""

    accept: Incomplete

class INamedImageField(INamedField):
    """Field for storing INamedImage objects."""

    accept: Incomplete

class IStorage(Interface):
    """Store file data"""
    def store(data, blob) -> None:
        """Store the data into the blob
        Raises NonStorable if data is not storable.
        """

class NotStorable(Exception):
    """Data is not storable"""

class IBlobby(Interface):
    """Marker interface for objects that support blobs."""

class INamedBlobFile(INamedFile, IBlobby):
    """A BLOB file with a filename"""

class INamedBlobImage(INamedImage, IBlobby):
    """A BLOB image with a filename"""

class INamedBlobFileField(INamedFileField):
    """Field for storing INamedBlobFile objects."""

class INamedBlobImageField(INamedImageField):
    """Field for storing INamedBlobImage objects."""
