from _typeshed import Incomplete
from zope.interface import Interface

class IContentIcon(Interface):
    """An icon for a piece of content"""

    width: Incomplete
    height: Incomplete
    url: Incomplete
    description: Incomplete
    title: Incomplete
    def html_tag() -> None:
        """Return a HTML string that is the tag for rendering this icon."""
