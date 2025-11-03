from _typeshed import Incomplete

LOGGER: Incomplete

class DefaultDexterityTextIndexFieldConverter:
    """Fallback field converter which uses the rendered widget in display
    mode for generating a indexable string.
    """

    context: Incomplete
    field: Incomplete
    widget: Incomplete
    def __init__(self, context, field, widget) -> None:
        """Initialize field converter"""
    def convert(self):
        """Convert the adapted field value to text/plain for indexing"""

class DexterityRichTextIndexFieldConverter:
    """Fallback field converter which uses the rendered widget in display
    mode for generating a indexable string.
    """

    context: Incomplete
    field: Incomplete
    def __init__(self, context, field, widget) -> None:
        """Initialize field converter"""
    def convert(self):
        """Convert a rich text field value to text/plain for indexing"""

class NamedfileFieldConverter(DefaultDexterityTextIndexFieldConverter):
    """Converts the file data of a named file using portal_transforms."""
    def convert(self):
        """Transforms file data to text for indexing safely."""

class IntFieldConverter(DefaultDexterityTextIndexFieldConverter):
    """Converts the data of a int field"""
    def convert(self):
        """return the adapted field value"""

class TupleFieldConverter(DefaultDexterityTextIndexFieldConverter):
    """Converts the data of a tuple field"""
    def convert(self):
        """return the adapted field value"""
