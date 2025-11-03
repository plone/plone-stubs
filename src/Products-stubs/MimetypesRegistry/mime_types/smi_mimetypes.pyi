from _typeshed import Incomplete
from xml.sax.handler import ContentHandler

DIR: Incomplete
SMI_NAME: str
SMI_COMPILED_NAME: str
SMI_FILE: Incomplete
SMI_COMPILED_FILE: Incomplete

class SharedMimeInfoHandler(ContentHandler):
    current: Incomplete
    collect_comment: Incomplete
    mimes: Incomplete
    def __init__(self) -> None: ...
    def startElement(self, name, attrs) -> None: ...
    def endElement(self, name) -> None: ...
    def characters(self, contents) -> None: ...

def parseSMIFile(infofile): ...
def readSMIFile():
    """Reads a shared mime info XML file"""

mimetypes: Incomplete

def initialize(registry) -> None: ...
