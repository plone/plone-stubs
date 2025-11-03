from Products.GenericSetup.utils import PropertyManagerHelpers
from Products.GenericSetup.utils import XMLAdapterBase

class MemberDataToolXMLAdapter(XMLAdapterBase, PropertyManagerHelpers):
    """XML im- and exporter for MemberDataTool."""

    name: str

def importMemberDataTool(context) -> None:
    """Import member data tool settings from an XML file."""

def exportMemberDataTool(context) -> None:
    """Export member data tool settings as an XML file."""
