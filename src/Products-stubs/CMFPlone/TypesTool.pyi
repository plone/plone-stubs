from _typeshed import Incomplete
from Products.CMFCore.TypesTool import TypesTool as BaseTool
from Products.CMFPlone.PloneBaseTool import PloneBaseTool

class TypesTool(PloneBaseTool, BaseTool):
    meta_type: str
    security: Incomplete
    toolicon: str
    def listTypeTitles(self, container=None): ...
    def listActions(self, info=None, object=None, category=None): ...
    def listActionInfos(
        self,
        action_chain=None,
        object=None,
        check_visibility: int = 1,
        check_permissions: int = 1,
        check_condition: int = 1,
        max: int = -1,
        category=None,
    ): ...
