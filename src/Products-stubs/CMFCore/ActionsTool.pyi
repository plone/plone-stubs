from .ActionProviderBase import ActionProviderBase
from .utils import UniqueObject
from _typeshed import Incomplete
from OFS.ObjectManager import IFAwareObjectManager
from OFS.OrderedFolder import OrderedFolder

class ActionsTool(
    UniqueObject, IFAwareObjectManager, OrderedFolder, ActionProviderBase
):
    """
    Weave together the various sources of "actions" which are apropos
    to the current user and context.
    """

    id: str
    meta_type: str
    zmi_icon: str
    action_providers: Incomplete
    security: Incomplete
    manage_options: Incomplete
    manage_overview: Incomplete
    manage_actionProviders: Incomplete
    def manage_aproviders(
        self,
        apname: str = "",
        chosen=(),
        add_provider: int = 0,
        del_provider: int = 0,
        REQUEST=None,
    ):
        """
        Manage action providers through-the-web.
        """
    def manage_editActionsForm(self, REQUEST, manage_tabs_message=None):
        """Show the 'Actions' management tab."""
    @security.private
    def listActions(self, info=None, object=None):
        """List all the actions defined by a provider."""
    def listActionProviders(self):
        """List the ids of all Action Providers queried by this tool."""
    def addActionProvider(self, provider_name) -> None:
        """Add an Action Provider id to the providers queried by this tool."""
    def deleteActionProvider(self, provider_name) -> None:
        """Delete an Action Provider id from providers queried by this tool."""
    @security.public
    def listFilteredActionsFor(self, object=None):
        """List all actions available to the user."""
