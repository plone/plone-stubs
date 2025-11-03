from ..ActionInformation import Action
from ..ActionInformation import ActionCategory
from Products.GenericSetup.browser.utils import AddWithPresettingsViewBase

class ActionAddView(AddWithPresettingsViewBase):
    """Add view for Action."""

    klass = Action
    description: str
    def getProfileInfos(self): ...

class ActionCategoryAddView(AddWithPresettingsViewBase):
    """Add view for ActionCategory."""

    klass = ActionCategory
    description: str
    def getProfileInfos(self): ...
