from zope.interface import Interface

class IZopePageTemplate(Interface):
    """Page Templates using TAL, TALES, and METAL."""
    def read() -> None:
        """Generate a text representation of the Template source."""
    def write(text) -> None:
        """Change the Template by parsing a read()-style source text."""
