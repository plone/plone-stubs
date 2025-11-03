from _typeshed import Incomplete
from Products.GenericSetup.utils import NodeAdapterBase
from Products.GenericSetup.utils import ObjectManagerHelpers
from Products.GenericSetup.utils import PropertyManagerHelpers
from Products.GenericSetup.utils import XMLAdapterBase

class ActionCategoryNodeAdapter(
    NodeAdapterBase, ObjectManagerHelpers, PropertyManagerHelpers
):
    """Node im- and exporter for ActionCategory."""

    node: Incomplete

class ActionNodeAdapter(NodeAdapterBase, PropertyManagerHelpers):
    """Node im- and exporter for Action."""

    node: Incomplete

class ActionsToolXMLAdapter(XMLAdapterBase, ObjectManagerHelpers):
    """XML im- and exporter for ActionsTool."""

    name: str

def importActionProviders(context) -> None:
    """Import actions tool."""

def exportActionProviders(context) -> None:
    """Export actions tool."""
