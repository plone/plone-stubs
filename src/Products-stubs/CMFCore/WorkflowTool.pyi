from .ActionProviderBase import ActionProviderBase
from .utils import UniqueObject
from _typeshed import Incomplete
from AccessControl.requestmethod import postonly
from OFS.Folder import Folder
from OFS.ObjectManager import IFAwareObjectManager

class WorkflowTool(UniqueObject, IFAwareObjectManager, Folder, ActionProviderBase):
    """Mediator tool, mapping workflow objects"""

    id: str
    meta_type: str
    security: Incomplete
    manage_options: Incomplete
    manage_overview: Incomplete
    def manage_selectWorkflows(self, REQUEST, manage_tabs_message=None):
        """Show a management screen for changing type to workflow connections."""
    @postonly
    def manage_changeWorkflows(self, default_chain, props=None, REQUEST=None):
        """Changes which workflows apply to objects of which type."""
    @security.private
    def listActions(self, info=None, object=None):
        """Returns a list of actions to be displayed to the user.

        o Invoked by the portal_actions tool.

        o Allows workflows to include actions to be displayed in the
          actions box.

        o Object actions are supplied by workflows that apply to the object.

        o Global actions are supplied by all workflows.
        """
    @security.private
    def getCatalogVariablesFor(self, ob):
        """Get a mapping of "workflow-relevant" attributes."""
    @security.public
    def doActionFor(self, ob, action, wf_id=None, *args, **kw):
        """Perform the given workflow action on 'ob'."""
    @security.public
    def getInfoFor(self, ob, name, default=..., wf_id=None, *args, **kw):
        """Get the given bit of workflow information for the object."""
    @security.private
    def notifyCreated(self, ob) -> None:
        """Notify all applicable workflows that an object has been created."""
    @security.private
    def notifyBefore(self, ob, action) -> None:
        """Notify all applicable workflows of an action before it happens."""
    @security.private
    def notifySuccess(self, ob, action, result=None) -> None:
        """Notify all applicable workflows that an action has taken place."""
    @security.private
    def notifyException(self, ob, action, exc) -> None:
        """Notify all applicable workflows that an action failed."""
    @security.private
    def getHistoryOf(self, wf_id, ob):
        """Get the history of an object for a given workflow."""
    @security.private
    def getStatusOf(self, wf_id, ob):
        """Get the last element of a workflow history for a given workflow."""
    @security.private
    def setStatusOf(self, wf_id, ob, status) -> None:
        """Append a record to the workflow history of a given workflow."""
    @postonly
    def setDefaultChain(self, default_chain, REQUEST=None) -> None:
        """Set the default chain for this tool."""
    @postonly
    def setChainForPortalTypes(
        self, pt_names, chain, verify: bool = True, REQUEST=None
    ) -> None:
        """Set a chain for specific portal types."""
    @security.private
    def getDefaultChain(self):
        """Get the default chain for this tool."""
    @security.private
    def listChainOverrides(self):
        """List portal type specific chain overrides."""
    @security.private
    def getChainFor(self, ob):
        """Get the chain that applies to the given object."""
    @postonly
    def updateRoleMappings(self, REQUEST=None):
        """Allow workflows to update the role-permission mappings."""
    @security.private
    def getWorkflowById(self, wf_id):
        """Retrieve a given workflow."""
    @security.private
    def getDefaultChainFor(self, ob):
        """Get the default chain, if applicable, for ob."""
    @security.private
    def getWorkflowIds(self):
        """Return the list of workflow ids."""
    def getWorkflowsFor(self, ob):
        """Find the workflows for the type of the given object."""

class DefaultWorkflowStatus:
    context: Incomplete
    wf_id: Incomplete
    def __init__(self, context, workflow) -> None: ...
    def get(self): ...
    def set(self, status) -> None: ...

def default_workflow_history(context, workflow): ...
