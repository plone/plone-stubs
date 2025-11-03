from _typeshed import Incomplete
from zope.interface import Interface
from zope.schema.interfaces import IObject

_: Incomplete

class IRichText(IObject):
    """A text field that stores MIME type"""

    default_mime_type: Incomplete
    output_mime_type: Incomplete
    allowed_mime_types: Incomplete
    max_length: Incomplete

class IRichTextValue(Interface):
    """The value actually stored in a RichText field.

    This stores the following values on the parent object

      - A separate persistent object with the original value
      - A cache of the value transformed to the default output type

    The object is immutable.
    """

    raw: Incomplete
    mimeType: Incomplete
    outputMimeType: Incomplete
    encoding: Incomplete
    raw_encoded: Incomplete
    output: Incomplete

class TransformError(Exception):
    """Exception raised if a value could not be transformed. This is normally
    caused by another exception. Inspect self.cause to find that.
    """

    message: Incomplete
    cause: Incomplete
    def __init__(self, message, cause=None) -> None: ...

class ITransformer(Interface):
    """A simple abstraction for invoking a transformation from one MIME
    type to another.

    This is not intended as a general transformations framework, but rather
    as a way to abstract away a dependency on the underlying transformation
    engine.

    This interface will be implemented by an adapter onto the context where
    the value is stored.
    """
    def __call__(value, mimeType) -> None:
        """Transform the IRichTextValue 'value' to the given MIME type.
        Return a unicode string. Raises TransformError if something went
        wrong.
        """
