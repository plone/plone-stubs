from _typeshed import Incomplete
from persistent import Persistent

LOG: Incomplete

class RawValueHolder(Persistent):
    """Place the raw value in a separate persistent object so that it does not
    get loaded when all we want is the output.
    """

    value: Incomplete
    def __init__(self, value) -> None: ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

class RichTextValue:
    """The actual value.

    Note that this is not a persistent object, to avoid a separate ZODB object
    being loaded.
    """
    def __init__(
        self,
        raw=None,
        mimeType=None,
        outputMimeType=None,
        encoding: str = "utf-8",
        output=None,
    ) -> None: ...
    @property
    def raw(self): ...
    @property
    def encoding(self): ...
    @property
    def raw_encoded(self): ...
    @property
    def mimeType(self): ...
    @property
    def outputMimeType(self): ...
    @property
    def output(self): ...
    def output_relative_to(self, context):
        """Transforms the raw value to the output mimetype, within a specified context.

        If the value's mimetype is already the same as the output mimetype,
        no transformation is performed.

        The context parameter is relevant when the transformation is
        context-dependent. For example, Plone's resolveuid-and-caption
        transform converts relative links to absolute links using the context
        as a base.

        If a transformer cannot be found for the specified context, a
        transformer with the site as a context is used instead.
        """
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def getSize(self): ...
