from _typeshed import Incomplete
from Products.CMFCore.exportimport.workflow import WorkflowToolXMLAdapter
from Products.GenericSetup.OFSP.exportimport import FolderXMLAdapter

class PlacefulWorkflowXMLAdapter(FolderXMLAdapter):
    body: Incomplete

class WorkflowPoliciesXMLAdapter(WorkflowToolXMLAdapter):
    @property
    def name(self): ...

def importWorkflowPolicies(context) -> None:
    """Import workflow policies from the XML file."""

def exportWorkflowPolicies(context) -> None:
    """Export workflow policies as an XML file."""
