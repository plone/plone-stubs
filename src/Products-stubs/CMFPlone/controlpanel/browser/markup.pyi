from _typeshed import Incomplete
from plone.app.registry.browser import controlpanel
from plone.base.interfaces import IMarkupSchema

class MarkupControlPanelForm(controlpanel.RegistryEditForm):
    id: str
    label: Incomplete
    schema = IMarkupSchema
    schema_prefix: str
    def updateFields(self) -> None: ...

class MarkupControlPanel(controlpanel.ControlPanelFormWrapper):
    form = MarkupControlPanelForm
