from _typeshed import Incomplete
from plone.app.registry.browser import controlpanel
from plone.base.interfaces import ITinyMCESchema
from z3c.form import group

class TinyMCEPluginForm(group.GroupForm):
    label: Incomplete
    fields: Incomplete

class TinyMCEResourceTypesForm(group.GroupForm):
    label: Incomplete
    fields: Incomplete

class TinyMCEAdvancedForm(group.GroupForm):
    label: Incomplete
    fields: Incomplete

class TinyMCEControlPanelForm(controlpanel.RegistryEditForm):
    id: str
    label: Incomplete
    schema = ITinyMCESchema
    schema_prefix: str
    fields: Incomplete
    groups: Incomplete
    def updateFields(self) -> None: ...

class TinyMCEControlPanel(controlpanel.ControlPanelFormWrapper):
    form = TinyMCEControlPanelForm
