from _typeshed import Incomplete
from plone.app.registry.browser import controlpanel
from plone.i18n.interfaces import ILanguageSchema

class LanguageControlPanelForm(controlpanel.RegistryEditForm):
    id: str
    label: Incomplete
    description: Incomplete
    schema = ILanguageSchema
    schema_prefix: str
    status: Incomplete
    def handleSave(self, action) -> None: ...
    def handleCancel(self, action) -> None: ...

class LanguageControlPanel(controlpanel.ControlPanelFormWrapper):
    form = LanguageControlPanelForm
