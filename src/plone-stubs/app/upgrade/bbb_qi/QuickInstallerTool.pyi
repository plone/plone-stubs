from OFS.ObjectManager import ObjectManager
from OFS.SimpleItem import SimpleItem
from Products.CMFCore.utils import UniqueObject

class HiddenProducts:
    def getNonInstallableProducts(self): ...

class QuickInstallerTool(UniqueObject, ObjectManager, SimpleItem):
    meta_type: str
    id: str
