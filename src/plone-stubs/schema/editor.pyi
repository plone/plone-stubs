from .email import IEmail
from .jsonfield import IJSONField
from _typeshed import Incomplete
from zope.schema.interfaces import IURI

_: Incomplete

class IURI(IURI):
    default: Incomplete

class IEmail(IEmail):
    default: Incomplete

class IJSON(IJSONField):
    default: Incomplete

URIFactory: Incomplete
EmailFactory: Incomplete
JSONFactory: Incomplete
