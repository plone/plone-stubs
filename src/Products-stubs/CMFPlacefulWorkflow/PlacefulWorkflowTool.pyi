from _typeshed import Incomplete
from OFS.Folder import Folder
from OFS.ObjectManager import IFAwareObjectManager
from Products.CMFCore.utils import ImmutableId

WorkflowPolicyConfig_id: str

def safeEditProperty(obj, key, value, data_type: str = "string") -> None:
    """An add or edit function, surprisingly useful :)"""

def addPlacefulWorkflowTool(self, REQUEST={}):
    """
    Factory method for the Placeful Workflow Tool
    """

class PlacefulWorkflowTool(ImmutableId, Folder, IFAwareObjectManager):
    """
    PlacefulWorkflow Tool
    """

    id: str
    meta_type: str
    security: Incomplete
    manage_options: Incomplete
    def __init__(self) -> None: ...
    def manage_addWorkflowPolicyForm(self, REQUEST):
        """Form for adding workflow policies."""
    def manage_addWorkflowPolicy(
        self,
        id,
        workflow_policy_type: str = "default_workflow_policy (Simple Policy)",
        duplicate_id: str = "empty",
        RESPONSE=None,
        REQUEST=None,
    ) -> None:
        """Adds a workflow policies from the registered types."""
    manage_addWorkflowPolicy: Incomplete
    def all_meta_types(self): ...
    def getWorkflowPolicyById(self, wfp_id):
        """Retrieve a given workflow policy."""
    def isValidPolicyName(self, policy_id):
        """Return True if a policy exist"""
    def getWorkflowPolicies(self):
        """Return the list of workflow policies."""
    def getWorkflowPolicyIds(self):
        """Return the list of workflow policy ids."""
    def getWorkflowPolicyInfos(self):
        """Return the list of workflow policy ids."""
    def getWorkflowPolicyConfig(self, ob):
        """Return a local workflow configuration if it exist"""
    def isSiteRoot(self, ob):
        """Returns a boolean value indicating if the object is an ISiteRoot
        or the default page of an ISiteRoot.
        """
    def getMaxChainLength(self):
        """Return the max workflow chain length"""
    def setMaxChainLength(self, max_chain_length) -> None:
        """Set the max workflow chain length"""

def addWorkflowPolicyFactory(factory, id=None, title=None) -> None: ...
