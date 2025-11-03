from Products.GenericSetup.utils import XMLAdapterBase

class RepositoryToolXMLAdapter(XMLAdapterBase):
    """Mode in- and exporter for RepositoryTool."""

    name: str

def importRepositoryTool(context) -> None:
    """Import Repository Tool configuration."""

def exportRepositoryTool(context) -> None:
    """Export Repository Tool configuration."""
