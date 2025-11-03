from _typeshed import Incomplete
from plone.app.registry.browser import controlpanel
from plone.base.interfaces import INavigationSchema

class NavigationControlPanelForm(controlpanel.RegistryEditForm):
    id: str
    label: Incomplete
    description: Incomplete
    schema = INavigationSchema
    schema_prefix: str
    def updateFields(self) -> None: ...

class NavigationControlPanel(controlpanel.ControlPanelFormWrapper):
    form = NavigationControlPanelForm
