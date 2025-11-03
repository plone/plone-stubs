from ..plugins.BasePlugin import BasePlugin
from _typeshed import Incomplete
from zope.interface import Interface

class IChallengeProtocolChooserPlugin(Interface):
    """Marker interface."""

def registerRequestType(label, iface) -> None: ...
def listRequestTypesLabels(): ...

manage_addChallengeProtocolChooserForm: Incomplete

def addChallengeProtocolChooserPlugin(
    dispatcher, id, title=None, mapping=None, REQUEST=None
) -> None:
    """Add a ChallengeProtocolChooserPlugin to a Pluggable Auth Service."""

class ChallengeProtocolChooser(BasePlugin):
    """PAS plugin for choosing challenger protocol based on request"""

    meta_type: str
    zmi_icon: str
    security: Incomplete
    manage_options: Incomplete
    title: Incomplete
    def __init__(self, id, title=None, mapping=None) -> None: ...
    @security.private
    def chooseProtocols(self, request): ...
    manage_editProtocolMappingForm: Incomplete
    def manage_editProtocolMapping(self, REQUEST=None):
        """Edit Protocol Mapping"""
    def manage_updateProtocolMapping(self, mapping, REQUEST=None) -> None:
        """Update mapping of Request Type to Protocols"""
