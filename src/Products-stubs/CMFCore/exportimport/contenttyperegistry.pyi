from Products.GenericSetup.utils import XMLAdapterBase

class ContentTypeRegistryXMLAdapter(XMLAdapterBase):
    """XML im- and exporter for ContentTypeRegistry."""

    name: str

def importContentTypeRegistry(context) -> None:
    """Import content type registry settings from an XML file."""

def exportContentTypeRegistry(context) -> None:
    """Export content type registry settings as an XML file."""
