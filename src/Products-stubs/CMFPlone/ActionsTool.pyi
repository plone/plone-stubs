from _typeshed import Incomplete
from Products.CMFCore.ActionsTool import ActionsTool as BaseTool
from Products.CMFPlone.PloneBaseTool import PloneBaseTool

class ActionsTool(PloneBaseTool, BaseTool):
    meta_type: str
    toolicon: str
    security: Incomplete
    @security.private
    def listActions(
        self, info=None, object=None, categories=None, ignore_categories=None
    ):
        """List all the actions defined by a provider."""
    @security.public
    def listActionInfos(
        self,
        action_chain=None,
        object=None,
        check_visibility: int = 1,
        check_permissions: int = 1,
        check_condition: int = 1,
        max: int = -1,
        categories=None,
        ignore_categories=None,
    ): ...
    @security.public
    def listFilteredActionsFor(
        self, object=None, ignore_providers=(), ignore_categories=None
    ): ...
