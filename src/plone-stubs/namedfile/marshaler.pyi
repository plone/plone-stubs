from _typeshed import Incomplete
from plone.namedfile import NamedBlobFile
from plone.namedfile import NamedBlobImage
from plone.namedfile import NamedFile
from plone.namedfile import NamedImage
from plone.rfc822.defaultfields import BaseFieldMarshaler

class BaseNamedFileFieldMarshaler(BaseFieldMarshaler):
    """Base marshaler for plone.namedfile values. Actual adapters are
    registered as subclasses.
    """

    ascii: bool
    factory: Incomplete
    def encode(self, value, charset: str = "utf-8", primary: bool = False): ...
    def decode(
        self,
        value,
        message=None,
        charset: str = "utf-8",
        contentType=None,
        primary: bool = False,
    ): ...
    def getContentType(self): ...
    def postProcessMessage(self, message) -> None:
        """Encode message as base64 and set content disposition"""

class NamedFileFieldMarshaler(BaseNamedFileFieldMarshaler):
    """Marshaler for an INamedFile field"""

    factory = NamedFile

class NamedImageFieldMarshaler(BaseNamedFileFieldMarshaler):
    """Marshaler for an INamedImage field"""

    factory = NamedImage

class NamedBlobFileFieldMarshaler(BaseNamedFileFieldMarshaler):
    """Marshaler for an INamedBlobFile field"""

    factory = NamedBlobFile

class NamedBlobImageFieldMarshaler(BaseNamedFileFieldMarshaler):
    """Marshaler for an INamedBlobImage field"""

    factory = NamedBlobImage
