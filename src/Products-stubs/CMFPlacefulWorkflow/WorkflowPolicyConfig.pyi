from _typeshed import Incomplete
from OFS.SimpleItem import SimpleItem

manage_addWorkflowPolicyConfigForm: Incomplete

def manage_addWorkflowPolicyConfig(self, REQUEST=None) -> None:
    """add a Workflow Policy Configuratio into the system"""

class WorkflowPolicyConfig(SimpleItem):
    """Workflow policy configuration"""

    meta_type: str
    index_html: Incomplete
    security: Incomplete
    manage_main: Incomplete
    manage_options: Incomplete
    id: Incomplete
    title: str
    def __init__(
        self, workflow_policy_in: str = "", workflow_policy_below: str = ""
    ) -> None:
        """Initialize a new MailHost instance"""
    def manage_makeChanges(self, workflow_policy_in, workflow_policy_below) -> None:
        """Store the policies"""
    def getPolicyInId(self): ...
    def getPolicyBelowId(self): ...
    def getPolicyIn(self): ...
    def getPolicyBelow(self): ...
    workflow_policy_in: Incomplete
    def setPolicyIn(self, policy, update_security: bool = False) -> None: ...
    workflow_policy_below: Incomplete
    def setPolicyBelow(self, policy, update_security: bool = False) -> None: ...
    def getPlacefulChainFor(self, portal_type, start_here: bool = False):
        """Get the chain for the given portal_type.

        Returns None if no placeful chain is found.
        Does _not_ acquire from parent configurations.

        Usecases:
        If the policy config is in the object that request the chain we cannot
        take the 'below' policy.
        In other case we test the 'below' policy first and, if there's no chain
        found, the 'in' policy.
        """
