from _typeshed import Incomplete
from Acquisition import Implicit
from Products.GenericSetup.utils import BodyAdapterBase

TRIGGER_TYPES: Incomplete

class DCWorkflowDefinitionBodyAdapter(BodyAdapterBase):
    """Body im- and exporter for DCWorkflowDefinition."""

    body: Incomplete
    mime_type: str
    suffix: str

class WorkflowDefinitionConfigurator(Implicit):
    """Synthesize XML description of site's workflows."""

    security: Incomplete
    def __init__(self, obj) -> None: ...
    def getWorkflowInfo(self, workflow_id):
        """Return a mapping describing a given workflow.

        o Keys in the mappings:

          'id' -- the ID of the workflow within the tool

          'meta_type' -- the workflow's meta_type

          'title' -- the workflow's title property

          'description' -- the workflow's description property

        o See '_extractDCWorkflowInfo' below for keys present only for
          DCWorkflow definitions.

        """
    def generateWorkflowXML(self):
        """Pseudo API."""
    def getWorkflowScripts(self):
        """Get workflow scripts information"""
    def parseWorkflowXML(self, xml, encoding: str = "utf-8"):
        """Pseudo API."""
