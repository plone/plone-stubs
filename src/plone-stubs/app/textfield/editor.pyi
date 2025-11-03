from _typeshed import Incomplete
from plone.app.textfield import interfaces
from zope.schema import interfaces as schema_ifaces

HAS_VOCABS: bool

class IRichText(interfaces.IRichText, schema_ifaces.IFromUnicode):
    default_mime_type: Incomplete
    default: Incomplete
    output_mime_type: Incomplete
    allowed_mime_types: Incomplete

RichTextFactory: Incomplete
