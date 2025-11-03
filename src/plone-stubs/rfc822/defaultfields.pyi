from _typeshed import Incomplete

class BaseFieldMarshaler:
    """Base class for field marshalers"""

    ascii: bool
    context: Incomplete
    field: Incomplete
    instance: Incomplete
    def __init__(self, context, field) -> None: ...
    def marshal(self, charset: str = "utf-8", primary: bool = False): ...
    def demarshal(
        self,
        value,
        message=None,
        charset: str = "utf-8",
        contentType=None,
        primary: bool = False,
    ) -> None: ...
    def encode(self, value, charset: str = "utf-8", primary: bool = False) -> None: ...
    def decode(
        self,
        value,
        message=None,
        charset: str = "utf-8",
        contentType=None,
        primary: bool = False,
    ) -> None: ...
    def getContentType(self) -> None: ...
    def getCharset(self, default: str = "utf-8") -> None: ...
    def postProcessMessage(self, message) -> None: ...

class UnicodeFieldMarshaler(BaseFieldMarshaler):
    """Default marshaler for fields that support IFromUnicode"""
    def encode(self, value, charset: str = "utf-8", primary: bool = False): ...
    def decode(
        self,
        value,
        message=None,
        charset: str = "utf-8",
        contentType=None,
        primary: bool = False,
    ): ...
    def getCharset(self, default: str = "utf-8"): ...

class UnicodeValueFieldMarshaler(UnicodeFieldMarshaler):
    """Default marshaler for fields that contain unicode data and so may be
    ASCII safe.
    """

    ascii: bool
    def encode(self, value, charset: str = "utf-8", primary: bool = False): ...

class ASCIISafeFieldMarshaler(UnicodeFieldMarshaler):
    """Default marshaler for fields that are ASCII safe, but still support
    IFromUnicode. This includes Int, Float, Decimal, and Bool.
    """

    ascii: bool
    def getCharset(self, default: str = "utf-8") -> None: ...

class BytesFieldMarshaler(BaseFieldMarshaler):
    """Default marshaler for IBytes fields and children. These store str
    objects, so we will attempt to encode them directly.
    """

    ascii: bool
    def encode(self, value, charset: str = "utf-8", primary: bool = False): ...
    def decode(
        self,
        value,
        message=None,
        charset: str = "utf-8",
        contentType=None,
        primary: bool = False,
    ): ...

class DatetimeMarshaler(BaseFieldMarshaler):
    """Marshaler for Python datetime values"""

    ascii: bool
    def encode(self, value, charset: str = "utf-8", primary: bool = False): ...
    def decode(
        self,
        value,
        message=None,
        charset: str = "utf-8",
        contentType=None,
        primary: bool = False,
    ): ...

class DateMarshaler(BaseFieldMarshaler):
    """Marshaler for Python date values.

    Note: we don't use the date formatting support in the 'email' module as
    this does not seem to be capable of round-tripping values with time zone
    information.
    """

    ascii: bool
    def encode(self, value, charset: str = "utf-8", primary: bool = False): ...
    def decode(
        self,
        value,
        message=None,
        charset: str = "utf-8",
        contentType=None,
        primary: bool = False,
    ): ...

class TimedeltaMarshaler(BaseFieldMarshaler):
    """Marshaler for Python timedelta values

    Note: we don't use the date formatting support in the 'email' module as
    this does not seem to be capable of round-tripping values with time zone
    information.
    """

    ascii: bool
    def encode(self, value, charset: str = "utf-8", primary: bool = False): ...
    def decode(
        self,
        value,
        message=None,
        charset: str = "utf-8",
        contentType=None,
        primary: bool = False,
    ): ...

class CollectionMarshaler(BaseFieldMarshaler):
    """Marshaler for collection values"""

    ascii: bool
    def getCharset(self, default: str = "utf-8"): ...
    def encode(self, value, charset: str = "utf-8", primary: bool = False): ...
    def decode(
        self,
        value,
        message=None,
        charset: str = "utf-8",
        contentType=None,
        primary: bool = False,
    ): ...
