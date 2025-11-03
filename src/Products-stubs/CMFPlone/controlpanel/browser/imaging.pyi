from _typeshed import Incomplete
from plone.app.registry.browser import controlpanel
from plone.base.interfaces.controlpanel import IImagingSchema

log: Incomplete

class ImagingControlPanelForm(controlpanel.RegistryEditForm):
    id: str
    label: Incomplete
    schema = IImagingSchema
    schema_prefix: str

class ImagingControlPanel(controlpanel.ControlPanelFormWrapper):
    form = ImagingControlPanelForm
