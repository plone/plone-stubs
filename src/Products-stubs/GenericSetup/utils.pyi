from _typeshed import Incomplete
from Acquisition import Implicit
from xml.dom.minidom import Document
from xml.dom.minidom import Element

CONVERTER: Incomplete
DEFAULT: Incomplete
KEY: Incomplete
I18NURI: str
LINES_HAS_TEXT: bool

class ImportConfiguratorBase(Implicit):
    """Synthesize data from XML description."""

    security: Incomplete
    def __init__(self, site, encoding: str = "utf-8") -> None: ...
    def parseXML(self, xml):
        """Pseudo API."""

class ExportConfiguratorBase(Implicit):
    """Synthesize XML description."""

    security: Incomplete
    def __init__(self, site, encoding: str = "utf-8") -> None: ...
    def generateXML(self, **kw):
        """Pseudo API."""

class _LineWrapper:
    def __init__(self, writer, indent, addindent, newl, max) -> None: ...
    def queue(self, text) -> None: ...
    def write(self, text: str = "", enforce: bool = False) -> None: ...

class _Element(Element):
    """minidom element with 'pretty' XML output."""
    def writexml(
        self, writer, indent: str = "", addindent: str = "", newl: str = ""
    ) -> None: ...

class PrettyDocument(Document):
    """minidom document with 'pretty' XML output."""
    def createElement(self, tagName): ...
    def createElementNS(self, namespaceURI, qualifiedName): ...
    def writexml(
        self,
        writer,
        indent: str = "",
        addindent: str = "",
        newl: str = "",
        encoding: str = "utf-8",
        standalone=None,
    ) -> None: ...
    def toprettyxml(
        self, indent: str = "\t", newl: str = "\n", encoding: str = "utf-8"
    ): ...

class NodeAdapterBase:
    """Node im- and exporter base."""

    context: Incomplete
    environ: Incomplete
    def __init__(self, context, environ) -> None: ...

class BodyAdapterBase(NodeAdapterBase):
    """Body im- and exporter base."""

    node: Incomplete
    body: Incomplete
    mime_type: str
    name: str
    suffix: str

class XMLAdapterBase(BodyAdapterBase):
    """XML im- and exporter base."""

    body: Incomplete
    mime_type: str
    name: str
    suffix: str
    filename: str

class ObjectManagerHelpers:
    """ObjectManager in- and export helpers."""

class PropertyManagerHelpers:
    """PropertyManager im- and export helpers.

    o Derived classes can supply a '_PROPERTIES' scehma, which is then used
      to mock up a temporary propertysheet for the object.  The adapter's
      methods ('_extractProperties', '_purgeProperties', '_initProperties')
      then run against that propertysheet.
    """
    def __init__(self, context, environ) -> None: ...

class MarkerInterfaceHelpers:
    """Marker interface im- and export helpers."""

def exportObjects(obj, parent_path, context) -> None:
    """Export subobjects recursively."""

def importObjects(obj, parent_path, context) -> None:
    """Import subobjects recursively."""
