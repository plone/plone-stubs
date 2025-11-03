from _typeshed import Incomplete
from plone.dexterity.content import DexterityContent as DexterityContent

CONTEXT_ENDPOINTS: Incomplete
PARENT_ENDPOINTS: Incomplete

class RestAPIPurgePaths:
    """RestAPI paths to purge for content items."""

    TRAVERSAL_PREFIX: str
    context: Incomplete
    def __init__(self, context: DexterityContent) -> None:
        """Initialize RestAPIPurgePaths."""
    def getRelativePaths(self) -> list[str]:
        """Return a list of paths that should be purged. The paths should be
        relative to the virtual hosting root, i.e. they should start with a
        '/'.

        These paths will be rewritten to incorporate virtual hosting if
        necessary.
        """
    def getAbsolutePaths(self) -> list[str]:
        """Return a list of paths that should be purged. The paths should be
        relative to the domain root, i.e. they should start with a '/'.

        These paths will *not* be rewritten to incorporate virtual hosting.
        """
