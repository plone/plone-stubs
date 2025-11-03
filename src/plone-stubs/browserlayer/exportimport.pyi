from Products.GenericSetup.utils import XMLAdapterBase

def dummyGetId(): ...

class BrowserLayerXMLAdapter(XMLAdapterBase):
    """Im- and exporter for local browser layers"""

    name: str

def importLayers(context) -> None:
    """Import local browser layers"""

def exportLayers(context) -> None:
    """Export local browser layers"""
