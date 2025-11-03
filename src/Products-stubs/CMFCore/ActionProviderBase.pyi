from _typeshed import Incomplete

class ActionProviderBase:
    """Provide ActionTabs and management methods for ActionProviders"""

    security: Incomplete
    manage_options: Incomplete
    @security.private
    def listActions(self, info=None, object=None):
        """List all the actions defined by a provider."""
    @security.private
    def getActionObject(self, action):
        """Return the actions object or None if action doesn't exist."""
    @security.public
    def listActionInfos(
        self,
        action_chain=None,
        object=None,
        check_visibility: int = 1,
        check_permissions: int = 1,
        check_condition: int = 1,
        max: int = -1,
    ): ...
    @security.public
    def getActionInfo(
        self,
        action_chain,
        object=None,
        check_visibility: int = 0,
        check_condition: int = 0,
    ):
        """Get an ActionInfo object specified by a chain of actions."""
    def manage_editActionsForm(self, REQUEST, manage_tabs_message=None):
        """Show the 'Actions' management tab."""
    def addAction(
        self,
        id,
        name,
        action,
        condition,
        permission,
        category,
        visible: int = 1,
        icon_expr: str = "",
        link_target: str = "",
        REQUEST=None,
    ):
        """Add an action to our list."""
    def changeActions(self, properties=None, REQUEST=None):
        """Update our list of actions."""
    def deleteActions(self, selections=(), REQUEST=None):
        """Delete actions indicated by indexes in 'selections'."""
    def moveUpActions(self, selections=(), REQUEST=None):
        """Move the specified actions up one slot in our list."""
    def moveDownActions(self, selections=(), REQUEST=None):
        """Move the specified actions down one slot in our list."""
