from _typeshed import Incomplete
from plone.app.registry.browser import controlpanel
from plone.base.interfaces import IFilterSchema
from plone.z3cform import layout

class FilterControlPanel(controlpanel.RegistryEditForm):
    id: str
    label: Incomplete
    description: Incomplete
    schema = IFilterSchema
    schema_prefix: str
    form_name: Incomplete
    control_panel_view: str
    status: Incomplete
    def handleSave(self, action) -> None: ...
    def handleCancel(self, action) -> None: ...

class ControlPanelFormWrapper(layout.FormWrapper):
    """Use this form as the plone.z3cform layout wrapper to get the control
    panel layout.
    """

    index: Incomplete

FilterControlPanelView: Incomplete
