from Products.GenericSetup.utils import ObjectManagerHelpers
from Products.GenericSetup.utils import PropertyManagerHelpers
from Products.GenericSetup.utils import XMLAdapterBase

class TypeInformationXMLAdapter(XMLAdapterBase, PropertyManagerHelpers):
    """XML im- and exporter for TypeInformation."""

class TypesToolXMLAdapter(XMLAdapterBase, ObjectManagerHelpers, PropertyManagerHelpers):
    """XML im- and exporter for TypesTool."""

    name: str

def importTypesTool(context) -> None:
    """Import types tool and content types from XML files."""

def exportTypesTool(context) -> None:
    """Export types tool content types as a set of XML files."""
