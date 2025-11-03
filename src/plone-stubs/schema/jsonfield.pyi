from _typeshed import Incomplete
from zope.schema import Field
from zope.schema.interfaces import IField

_: Incomplete
DEFAULT_JSON_SCHEMA: Incomplete

class IJSONField(IField):
    """A text field that stores A JSON."""

    schema: Incomplete

class JSONField(Field):
    widget: Incomplete
    json_schema: Incomplete
    def __init__(self, schema=..., widget=None, **kw) -> None: ...
    def fromUnicode(self, value):
        """Get value from unicode.

        Value can be a valid JSON object:

            JSONField().fromUnicode(\'{"items": []}\')

        or it can be a Python dict stored as string:

            JSONField().fromUnicode("{\'items\': []}")

        In both cases the result is:

            {"items": []}
        """
