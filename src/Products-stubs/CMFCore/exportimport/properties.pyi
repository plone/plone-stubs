from Products.GenericSetup.utils import PropertyManagerHelpers
from Products.GenericSetup.utils import XMLAdapterBase

class PropertiesXMLAdapter(XMLAdapterBase, PropertyManagerHelpers):
    """XML im- and exporter for properties."""

def importSiteProperties(context) -> None:
    """Import site properties from an XML file."""

def exportSiteProperties(context) -> None:
    """Export site properties as an XML file."""
