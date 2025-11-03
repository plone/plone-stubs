from _typeshed import Incomplete
from plone.namedfile.interfaces import INamedBlobFile
from plone.namedfile.interfaces import INamedBlobImage
from plone.namedfile.interfaces import INamedFile
from plone.namedfile.interfaces import INamedImage
from zope.schema import Object
from zope.schema import ValidationError

_: Incomplete

class InvalidFile(ValidationError):
    """Exception for a invalid file."""

    __doc__: Incomplete

class InvalidImageFile(ValidationError):
    """Exception for a invalid image file."""

    __doc__: Incomplete

class BinaryContenttypeValidator:
    field: Incomplete
    value: Incomplete
    def __init__(self, field, value) -> None: ...
    def __call__(self) -> None: ...

class FileContenttypeValidator(BinaryContenttypeValidator):
    exception = InvalidFile

class ImageContenttypeValidator(BinaryContenttypeValidator):
    exception = InvalidImageFile

class NamedField(Object):
    accept: Incomplete
    schema: Incomplete
    def __init__(self, **kw) -> None: ...
    def validate(self, value, interface) -> None: ...

class NamedFile(NamedField):
    """A NamedFile field"""

    schema = INamedFile
    accept: Incomplete
    def validate(self, value) -> None: ...

class NamedImage(NamedField):
    """A NamedImage field"""

    schema = INamedImage
    accept: Incomplete
    def validate(self, value) -> None: ...

class NamedBlobFile(NamedField):
    """A NamedBlobFile field"""

    schema = INamedBlobFile
    accept: Incomplete
    def validate(self, value) -> None: ...

class NamedBlobImage(NamedField):
    """A NamedBlobImage field"""

    schema = INamedBlobImage
    accept: Incomplete
    def validate(self, value) -> None: ...
