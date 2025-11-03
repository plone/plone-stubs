from ..DCWorkflow import DCWorkflowDefinition
from Products.GenericSetup.browser.utils import AddWithPresettingsViewBase

class DCWorkflowDefinitionAddView(AddWithPresettingsViewBase):
    """Add view for DCWorkflowDefinition."""

    klass = DCWorkflowDefinition
    description: str
    def getProfileInfos(self): ...
