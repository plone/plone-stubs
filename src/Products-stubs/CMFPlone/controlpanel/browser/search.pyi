from _typeshed import Incomplete
from plone.app.registry.browser import controlpanel
from plone.base.interfaces import ISearchSchema

class SearchControlPanelForm(controlpanel.RegistryEditForm):
    id: str
    label: Incomplete
    schema = ISearchSchema
    schema_prefix: str
    def updateFields(self) -> None: ...
    def updateWidgets(self) -> None: ...
    def applyChanges(self, data) -> None: ...

class SearchControlPanel(controlpanel.ControlPanelFormWrapper):
    form = SearchControlPanelForm
