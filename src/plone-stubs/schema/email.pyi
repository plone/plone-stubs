from _typeshed import Incomplete
from zope.schema import NativeStringLine
from zope.schema.interfaces import INativeStringLine
from zope.schema.interfaces import ValidationError

_: Incomplete

class IEmail(INativeStringLine):
    """A field containing an email address"""

class InvalidEmail(ValidationError):
    __doc__: Incomplete

class Email(NativeStringLine):
    """Email schema field"""
    def fromBytes(self, value): ...
    def fromUnicode(self, value): ...
