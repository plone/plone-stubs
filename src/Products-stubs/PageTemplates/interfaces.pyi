from zope.interface import Interface

class IUnicodeEncodingConflictResolver(Interface):
    """A utility that tries to convert a non-unicode string into
    a Python unicode by implementing some policy in order
    to figure out a possible encoding - either through the
    calling context, the location or the system environment
    """
    def resolve(context, text, expression) -> None:
        """Returns 'text' as unicode string.
        'context' is the current context object.
        'expression' is the original expression (can be used for
        logging purposes)
        """

class IZopeAwareEngine(Interface):
    """Interface to mark a TALES engine aware of Zope specifics."""
