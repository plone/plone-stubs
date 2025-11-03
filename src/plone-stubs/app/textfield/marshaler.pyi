from plone.rfc822.defaultfields import BaseFieldMarshaler

class RichTextFieldMarshaler(BaseFieldMarshaler):
    """Field marshaler for plone.app.textfield values."""

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
    def getContentType(self): ...
    def getCharset(self, default: str = "utf-8"): ...
