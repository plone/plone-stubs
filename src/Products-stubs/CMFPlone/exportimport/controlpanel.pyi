from plone.base.interfaces import IControlPanel
from Products.GenericSetup.utils import XMLAdapterBase

class ControlPanelXMLAdapter(XMLAdapterBase):
    """
    XML im- and exporter for Plone control panel.  Most of this
    code is taken from the actions handler in CMFCore.
    """

    __used_for__ = IControlPanel
    name: str

def importControlPanel(context) -> None:
    """Import Plone control panel."""

def exportControlPanel(context) -> None:
    """Export actions tool."""
