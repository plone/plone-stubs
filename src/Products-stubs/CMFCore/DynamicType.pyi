from _typeshed import Incomplete

class DynamicType:
    """
    Mixin for portal content that allows the object to take on
    a dynamic type property.
    """

    portal_type: Incomplete
    security: Incomplete
    @security.public
    def getPortalTypeName(self):
        """Get the portal type name that can be passed to portal_types."""
    @security.public
    def getTypeInfo(self):
        """Get the TypeInformation object specified by the portal type."""
    @security.public
    def getActionInfo(
        self, action_chain, check_visibility: int = 0, check_condition: int = 0
    ):
        """Get an Action info mapping specified by a chain of actions."""
    @security.public
    def getIconURL(self):
        """Get the absolute URL of the icon for the object."""
    @security.public
    def icon(self, relative_to_portal: int = 0):
        """
        Using this method allows the content class
        creator to grab icons on the fly instead of using a fixed
        attribute on the class.
        """
    getIcon = icon
    def __before_publishing_traverse__(self, arg1, arg2=None) -> None:
        """Pre-traversal hook."""
