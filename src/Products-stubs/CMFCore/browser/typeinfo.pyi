from ..TypesTool import FactoryTypeInformation
from ..TypesTool import ScriptableTypeInformation
from Products.GenericSetup.browser.utils import AddWithPresettingsViewBase

class FactoryTypeInformationAddView(AddWithPresettingsViewBase):
    """Add view for FactoryTypeInformation."""

    klass = FactoryTypeInformation
    description: str
    def getProfileInfos(self): ...

class ScriptableTypeInformationAddView(FactoryTypeInformationAddView):
    """Add view for ScriptableTypeInformation."""

    klass = ScriptableTypeInformation
