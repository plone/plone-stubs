from zope.interface import Interface

class IFolderContentsView(Interface):
    """Interface, which provides methods for folder contents"""
    def test(a, b, c) -> None:
        """A simple replacement of python's test."""
    def getAllowedTypes() -> None:
        """Returns allowed types for context."""
    def title() -> None:
        """Returns the title for the template."""
