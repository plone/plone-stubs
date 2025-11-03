from _typeshed import Incomplete
from Products.CMFCore.SkinsTool import SkinsTool as BaseTool
from Products.CMFPlone.PloneBaseTool import PloneBaseTool

class SkinsTool(PloneBaseTool, BaseTool):
    meta_type: str
    security: Incomplete
    toolicon: str
    default_skin: str
    request_varname: str
    def addSkinSelection(
        self, skinname, skinpath, test: int = 0, make_default: int = 0
    ) -> None: ...
    def manage_skinLayers(
        self,
        chosen=(),
        add_skin: int = 0,
        del_skin: int = 0,
        skinname: str = "",
        skinpath: str = "",
        REQUEST=None,
    ):
        """Change the skinLayers."""
