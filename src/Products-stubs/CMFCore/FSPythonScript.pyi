from .FSObject import FSObject
from _typeshed import Incomplete
from Products.PythonScripts.PythonScript import PythonScript
from Shared.DC.Scripts.Script import Script

class CustomizedPythonScript(PythonScript):
    """Subclass which captures the "source" version\'s text."""

    security: Incomplete
    original_source: Incomplete
    def __init__(self, id, text) -> None: ...
    def getDiff(self):
        """Return a diff of the current source with the original source."""
    manage_showDiff: Incomplete
    manage_options: Incomplete

class FSPythonScript(FSObject, Script):
    """FSPythonScripts act like Python Scripts but are not directly
    modifiable from the management interface."""

    meta_type: str
    zmi_icon: str
    manage_options: Incomplete
    security: Incomplete
    manage_main: Incomplete
    def __render_with_namespace__(self, namespace):
        """Calls the script."""
    def __call__(self, *args, **kw):
        """Calls the script."""
    def ZScriptHTML_tryParams(self):
        """Parameters to test the script with."""
    def read(self): ...
    def document_src(self, REQUEST=None, RESPONSE=None):
        """Return unprocessed document source."""
    def PrincipiaSearchSource(self):
        """Support for searching - the document's contents are searched."""
    def params(self): ...
    manage_haveProxy: Incomplete
    def body(self): ...
    def get_size(self): ...
    def manage_FTPget(self):
        """Get source for FTP download"""
    __defaults__: Incomplete
    __code__: Incomplete
    def title(self): ...
    title: Incomplete
    def getBindingAssignments(self): ...
