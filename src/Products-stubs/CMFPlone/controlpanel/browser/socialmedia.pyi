from _typeshed import Incomplete
from plone.app.registry.browser import controlpanel
from plone.base.interfaces import ISocialMediaSchema

class SocialControlPanelForm(controlpanel.RegistryEditForm):
    id: str
    label: Incomplete
    description: Incomplete
    schema = ISocialMediaSchema
    schema_prefix: str

class SocialControlPanel(controlpanel.ControlPanelFormWrapper):
    form = SocialControlPanelForm
