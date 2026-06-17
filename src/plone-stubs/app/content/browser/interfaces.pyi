from zope.interface import Interface

class IFolderContentsView(Interface):
    """Interface, which provides methods for folder contents"""
    def test(self, a, b, c) -> None:
        """A simple replacement of python's test."""
    def getAllowedTypes(self) -> None:
        """Returns allowed types for context."""
    def title(self) -> None:
        """Returns the title for the template."""
