from _typeshed import Incomplete
from zope.interface import Interface

class IPlacefulWorkflowTool(Interface):
    """ """

    id: Incomplete
    def getMaxChainLength(self) -> None:
        """Return the max workflow chain length"""
    def setMaxChainLength(self, max_chain_length) -> None:
        """Set the max workflow chain length"""

class IPlacefulMarker(Interface):
    """A marker applied to the standard workflow tool to enable placeful
    lookup"""

class IWorkflowPolicyDefinition(Interface):
    """ """
