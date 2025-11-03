from _typeshed import Incomplete
from plone.app.registry.browser import controlpanel
from plone.base.interfaces import ISiteSchema

class SiteControlPanelForm(controlpanel.RegistryEditForm):
    id: str
    label: Incomplete
    description: Incomplete
    schema = ISiteSchema
    schema_prefix: str
    def updateFields(self) -> None: ...
    def updateWidgets(self) -> None: ...

class SiteControlPanel(controlpanel.ControlPanelFormWrapper):
    form = SiteControlPanelForm
