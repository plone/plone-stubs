from _typeshed import Incomplete
from Products.CMFCore.URLTool import URLTool as BaseTool
from Products.CMFPlone.PloneBaseTool import PloneBaseTool
from Products.isurlinportal import isURLInPortal

class URLTool(PloneBaseTool, BaseTool):
    meta_type: str
    security: Incomplete
    toolicon: str
    isURLInPortal = isURLInPortal
    def getPortalObject(self): ...
