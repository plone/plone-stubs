from _typeshed import Incomplete
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.base.interfaces import IDateAndTimeSchema

class DateAndTimeControlPanelForm(RegistryEditForm):
    id: str
    schema = IDateAndTimeSchema
    schema_prefix: str
    label: Incomplete
    description: Incomplete

class DateAndTimeControlPanel(ControlPanelFormWrapper):
    form = DateAndTimeControlPanelForm
