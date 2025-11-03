from Products.GenericSetup.utils import PropertyManagerHelpers
from Products.GenericSetup.utils import XMLAdapterBase

class CookieCrumblerXMLAdapter(XMLAdapterBase, PropertyManagerHelpers):
    """XML im- and exporter for CookieCrumbler."""

    name: str

def importCookieCrumbler(context) -> None:
    """Import cookie crumbler settings from an XML file."""

def exportCookieCrumbler(context) -> None:
    """Export cookie crumbler settings as an XML file."""
