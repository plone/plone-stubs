from Products.GenericSetup.utils import XMLAdapterBase

class DiffToolXMLAdapter(XMLAdapterBase):
    """In- and exporter for DiffTool."""

    name: str

def importDiffTool(context) -> None:
    """Import Factory Tool configuration."""

def exportDiffTool(context) -> None:
    """Export Factory Tool configuration."""
