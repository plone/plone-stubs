from _typeshed import Incomplete
from Products.GenericSetup.utils import XMLAdapterBase

def dummyGetId(): ...

class Blacklist:
    def getExcludedInterfaces(self): ...

class PropertyPortletAssignmentExportImportHandler:
    """Import portlet assignment settings based on zope.schema properties"""

    assignment: Incomplete
    def __init__(self, assignment) -> None: ...
    def import_assignment(self, interface, node) -> None: ...
    def export_assignment(self, interface, doc, node) -> None: ...
    def import_node(self, interface, child) -> None:
        """Import a single <property /> node"""
    def export_field(self, doc, field):
        """Turn a zope.schema field into a node and return it"""
    def extract_text(self, node): ...
    def from_unicode(self, field, value): ...
    def field_typecast(self, field, value): ...

class PortletsXMLAdapter(XMLAdapterBase):
    """In- and exporter for a local portlet configuration"""

    name: str

def importPortlets(context) -> None:
    """Import portlet managers and portlets"""

def exportPortlets(context) -> None:
    """Export portlet managers and portlets"""

class InvalidPortletForDefinition(Exception):
    message: str
    args: Incomplete
    def __init__(self, node) -> None: ...
