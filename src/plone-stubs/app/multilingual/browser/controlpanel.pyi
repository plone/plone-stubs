from _typeshed import Incomplete
from plone.app.multilingual.interfaces import IMultiLanguageExtraOptionsSchema
from plone.app.registry.browser import controlpanel
from Products.CMFPlone.controlpanel.browser.language import LanguageControlPanelForm
from Products.Five import BrowserView

_: Incomplete

class LanguageControlPanelFormPAM(LanguageControlPanelForm):
    """A modified language control panel, allows selecting multiple languages."""

    label: Incomplete
    description: Incomplete
    schema = IMultiLanguageExtraOptionsSchema
    status: Incomplete
    def handleSave(self, action) -> None: ...
    def handleCancel(self, action) -> None: ...

class LanguageControlPanel(controlpanel.ControlPanelFormWrapper):
    form = LanguageControlPanelFormPAM
    index: Incomplete

class multilingualMapViewJSON(BrowserView):
    """Helper view to get json translations"""
    def __call__(self):
        """Get the JSON information about based on a nodeId"""

class multilingualMapView(BrowserView):
    """The view for display the current multilingual map for the site"""

    __call__: Incomplete
    def languages(self): ...
    def canonicals(self):
        """We get all the canonicals and see which translations are
        missing"""
