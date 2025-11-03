from _typeshed import Incomplete
from Products.GenericSetup.utils import NodeAdapterBase
from Products.GenericSetup.utils import ObjectManagerHelpers
from Products.GenericSetup.utils import XMLAdapterBase

class DirectoryViewNodeAdapter(NodeAdapterBase):
    """Node im- and exporter for DirectoryView."""

    node: Incomplete

class SkinsToolXMLAdapter(XMLAdapterBase, ObjectManagerHelpers):
    """XML im- and exporter for SkinsTool."""

    name: str

def importSkinsTool(context) -> None:
    """Import skins tool FSDirViews and skin paths from an XML file."""

def exportSkinsTool(context) -> None:
    """Export skins tool FSDVs and skin paths as an XML file."""
