from _typeshed import Incomplete
from Products.GenericSetup.utils import XMLAdapterBase

def as_bool(string, default: bool = False): ...

class PropertyRuleElementExportImportHandler:
    """Import portlet assignment settings based on zope.schema properties"""

    element: Incomplete
    descriptor: Incomplete
    def __init__(self, element) -> None: ...
    def import_element(self, node) -> None: ...
    def export_element(self, doc, node) -> None: ...
    def import_node(self, interface, child) -> None:
        """Import a single <property /> node"""
    def export_field(self, doc, field):
        """Turn a zope.schema field into a node and return it"""

class RulesXMLAdapter(XMLAdapterBase):
    """In- and exporter for a local portlet configuration"""

    name: str

def importRules(context) -> None:
    """Import content rules"""

def exportRules(context) -> None:
    """Export content rules"""
