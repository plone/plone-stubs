from _typeshed import Incomplete

default_encoding: Incomplete

class DefaultUnicodeEncodingConflictResolver:
    """This resolver implements the old-style behavior and will
    raise an exception in case of the string 'text' can't be converted
    properly to unicode.
    """
    def resolve(self, context, text, expression): ...

class Z2UnicodeEncodingConflictResolver:
    """This resolver tries to lookup the encoding from the
    'default-zpublisher-encoding' setting in the Zope configuration
    file and defaults to the old ZMI encoding iso-8859-15.
    """

    mode: Incomplete
    def __init__(self, mode: str = "strict") -> None: ...
    def resolve(self, context, text, expression): ...

class PreferredCharsetResolver:
    """A resolver that tries use the encoding information
    from the HTTP_ACCEPT_CHARSET header.
    """
    def resolve(self, context, text, expression): ...

StrictUnicodeEncodingConflictResolver: Incomplete
ReplacingUnicodeEncodingConflictResolver: Incomplete
IgnoringUnicodeEncodingConflictResolver: Incomplete
