from Products.GenericSetup.utils import ObjectManagerHelpers
from Products.GenericSetup.utils import PropertyManagerHelpers
from Products.GenericSetup.utils import XMLAdapterBase

class WorkflowToolXMLAdapter(
    XMLAdapterBase, ObjectManagerHelpers, PropertyManagerHelpers
):
    """XML im- and exporter for WorkflowTool."""

    name: str

def importWorkflowTool(context) -> None:
    """Import workflow tool and contained workflow definitions from XML files."""

def exportWorkflowTool(context) -> None:
    """Export workflow tool and contained workflow definitions as XML files."""
