from _typeshed import Incomplete
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.restapi.controlpanels import RegistryConfigletPanel
from plone.volto.interfaces import IVoltoSettings

class VoltoSettingsEditForm(RegistryEditForm):
    schema = IVoltoSettings
    label: Incomplete
    schema_prefix: str
    def updateFields(self) -> None: ...
    def updateWidgets(self) -> None: ...

class VoltoSettingsControlPanel(ControlPanelFormWrapper):
    form = VoltoSettingsEditForm

class VoltoControlpanel(RegistryConfigletPanel):
    schema = IVoltoSettings
    configlet_id: str
    configlet_category_id: str
    schema_prefix: str
