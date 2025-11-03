from _typeshed import Incomplete
from plone.app.registry.browser import controlpanel
from plone.base.interfaces import IEditingSchema

class EditingControlPanelForm(controlpanel.RegistryEditForm):
    id: str
    label: Incomplete
    schema = IEditingSchema
    schema_prefix: str
    def updateWidgets(self) -> None: ...

class EditingControlPanel(controlpanel.ControlPanelFormWrapper):
    form = EditingControlPanelForm
