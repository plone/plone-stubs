from _typeshed import Incomplete
from plone.app.registry.browser import controlpanel
from plone.base.interfaces.syndication import ISiteSyndicationSettings

_: Incomplete

class SyndicationControlPanelForm(controlpanel.RegistryEditForm):
    schema = ISiteSyndicationSettings
    label: Incomplete
    description: Incomplete
    def updateFields(self) -> None: ...
    def getSyndicationSettingsButtonShown(self): ...
    def getSyndicationLinkShown(self): ...
    def forceCheckboxValue(self, widget, checked) -> None: ...
    def update(self) -> None: ...
    def setSyndicationActionSettings(self, data) -> None: ...
    status: Incomplete
    def handleSave(self, action) -> None:
        """
        Again, we're customizing this to handle saving
        portal_actions related setting data.
        """
    def handleCancel(self, action) -> None: ...

class SyndicationControlPanel(controlpanel.ControlPanelFormWrapper):
    form = SyndicationControlPanelForm
