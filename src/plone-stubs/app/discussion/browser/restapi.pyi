from ..interfaces import IDiscussionSettings
from _typeshed import Incomplete
from plone.restapi.controlpanels import RegistryConfigletPanel
from zope.interface import Interface

IControlpanelLayer = Interface

class DiscussionControlPanel(RegistryConfigletPanel):
    """Volto-compatible REST API control panel for discussion settings."""

    schema = IDiscussionSettings
    schema_prefix: Incomplete
    configlet_id: str
    configlet_category_id: str
    title: Incomplete
    group: str
