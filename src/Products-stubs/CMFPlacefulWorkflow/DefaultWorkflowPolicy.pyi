from _typeshed import Incomplete
from Products.CMFCore.utils import SimpleItemWithProperties

DEFAULT_CHAIN: str

class DefaultWorkflowPolicyDefinition(SimpleItemWithProperties):
    meta_type: str
    id: str
    security: Incomplete
    manage_options: Incomplete
    title: str
    description: str
    def __init__(self, id) -> None: ...
    def getId(self):
        """Return the id"""
    def getTitle(self):
        """Return the title"""
    def getDescription(self):
        """Return the description"""
    def setTitle(self, title) -> None:
        """Set the title"""
    def setDescription(self, description) -> None:
        """Set the description"""
    def manage_main(self, REQUEST, manage_tabs_message=None):
        """Show a management screen for changing type to workflow connections

        Display 'None' if there's no chain for a type.
        """
    def manage_changeWorkflows(
        self, title, description, default_chain, props=None, REQUEST=None
    ):
        """Changes which workflows apply to objects of which type

        A chain equal to 'None' is empty we remove the entry.
        """
    manage_changeWorkflows: Incomplete
    def setChainForPortalTypes(self, pt_names, chain, REQUEST=None) -> None:
        """Set a chain for portal types."""
    setChainForPortalTypes: Incomplete
    def getChainFor(self, ob, managescreen: bool = False):
        """Returns the chain that applies to the object.

        If chain doesn't exist we return None to get a fallback from
        portal_workflow.

        @param managescreen: If True return the special tuple
                            ('default') instead of the actual default
                            chain (hack).
        """
    def setDefaultChain(self, default_chain, REQUEST=None):
        """Sets the default chain for this tool."""
    setDefaultChain: Incomplete
    def getDefaultChain(self, ob):
        """Returns the default chain."""
    def setChain(self, portal_type, chain, REQUEST=None) -> None:
        """Set the chain for a portal type.

        @type chain: tuple of strings or None
        @param chain: A tuple of workflow ids to be set for the portal type.
                      A few special values exist:
                        - C{None}: Acquire chain from a policy above,
                                   ultimately from the portal workflow settings.
                        - C{()} (empty tuple): No workflow for this type.
                        - C{('default',)}: Use the configured default workflow.
        """
    setChain: Incomplete
    def delChain(self, portal_type, REQUEST=None) -> None:
        """Delete the chain for a portal type."""
    delChain: Incomplete
