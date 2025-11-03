from _typeshed import Incomplete
from zope.interface import Interface

class IFilter(Interface):
    """A filter that accepts raw HTML and returns a filtered version.

    Register a named multi-adapter from (context, request) to
    this interface to install a new filter.

    To control the order of filters, use the 'order' attribute. It may be
    positive or negative."""

    order: Incomplete
    def is_enabled() -> None:
        """Returns a boolean indicating whether the filter should be
        applied."""
    def __call__(data) -> None:
        """Apply the filter.

        ``data`` is a UTF-8-encoded string.

        Return a UTF-8-encoded string, or ``None`` to indicate that the data
        should remain unmodified.
        """
