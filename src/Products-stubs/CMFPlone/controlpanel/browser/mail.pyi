from _typeshed import Incomplete
from plone.app.registry.browser import controlpanel
from plone.base.interfaces.controlpanel import IMailSchema

log: Incomplete

class MailControlPanelForm(controlpanel.RegistryEditForm):
    id: str
    label: Incomplete
    schema = IMailSchema
    schema_prefix: str
    def handleSave(self, action) -> None: ...
    def handleCancel(self, action) -> None: ...
    status: Incomplete
    def save(self): ...
    def handle_test_action(self, action) -> None: ...

class MailControlPanel(controlpanel.ControlPanelFormWrapper):
    form = MailControlPanelForm
