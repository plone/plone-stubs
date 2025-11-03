from _typeshed import Incomplete
from plone.supermodel.exportimport import BaseHandler

class RichTextHandler_(BaseHandler):
    """Special handling for the RichText field, to deal with 'default'
    that may be unicode.
    """

    filteredAttributes: Incomplete
    def __init__(self, klass) -> None: ...

class RichTextToUnicode:
    context: Incomplete
    def __init__(self, context) -> None: ...
    def toUnicode(self, value): ...

RichTextHandler: Incomplete
