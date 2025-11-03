from ..interfaces import IDiscussionSettings
from _typeshed import Incomplete
from plone.app.registry.browser import controlpanel

class DiscussionSettingsEditForm(controlpanel.RegistryEditForm):
    """Discussion settings form."""

    schema = IDiscussionSettings
    id: str
    label: Incomplete
    description: Incomplete
    def updateFields(self) -> None: ...
    def updateWidgets(self) -> None: ...
    status: Incomplete
    def handleSave(self, action) -> None: ...
    def handleCancel(self, action) -> None: ...

class DiscussionSettingsControlPanel(controlpanel.ControlPanelFormWrapper):
    """Discussion settings control panel."""

    form = DiscussionSettingsEditForm
    index: Incomplete
    def __call__(self): ...
    @property
    def site_url(self):
        """Return the absolute URL to the current site, which is likely not
        necessarily the portal root.
        """
    def settings(self):
        """Compose a string that contains all registry settings that are
        needed for the discussion control panel.
        """
    def mailhost_warning(self) -> None:
        """Returns true if mailhost is not configured properly."""
    def custom_comment_workflow_warning(self) -> None:
        """Return True if a custom comment workflow is enabled."""

def notify_configuration_changed(event) -> None:
    """Event subscriber that is called every time the configuration changed."""
