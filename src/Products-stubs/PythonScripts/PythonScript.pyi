from _typeshed import Incomplete
from OFS.Cache import Cacheable
from OFS.History import Historical
from Shared.DC.Scripts.Script import Script

import importlib.abc

LOG: Incomplete
Python_magic: Incomplete
Script_magic: int
manage_addPythonScriptForm: Incomplete

def manage_addPythonScript(
    self, id, title: str = "", file=None, REQUEST=None, submit=None
):
    """Add a Python script to a folder."""

class PythonScriptLoader(importlib.abc.Loader):
    """PEP302 loader to display source code in tracebacks"""
    def __init__(self, source) -> None: ...
    def get_source(self, name): ...

class PythonScript(Script, Historical, Cacheable):
    """Web-callable scripts written in a safe subset of Python.

    The function may include standard python code, so long as it does
    not attempt to use the "exec" statement or certain restricted builtins.
    """

    meta_type: str
    zmi_icon: str
    errors: Incomplete
    warnings: Incomplete
    manage_options: Incomplete
    id: Incomplete
    def __init__(self, id) -> None: ...
    security: Incomplete
    ZPythonScriptHTML_editForm: Incomplete
    manage = ZPythonScriptHTML_editForm
    manage_main = ZPythonScriptHTML_editForm
    def ZPythonScriptHTML_editAction(self, REQUEST, title, params, body):
        """Change the script's main parameters."""
    title: Incomplete
    def ZPythonScript_setTitle(self, title) -> None: ...
    def ZPythonScript_edit(self, params, body) -> None: ...
    def ZPythonScriptHTML_upload(self, REQUEST, file: str = ""):
        """Replace the body of the script with the text in file."""
    def ZScriptHTML_tryParams(self):
        """Parameters to test the script with."""
    def manage_historyCompare(
        self, rev1, rev2, REQUEST, historyComparisonResults: str = ""
    ): ...
    def manage_afterAdd(self, item, container) -> None: ...
    def manage_beforeDelete(self, item, container) -> None: ...
    def manage_afterClone(self, item) -> None: ...
    def get_filepath(self): ...
    def manage_haveProxy(self, r): ...
    manage_proxyForm: Incomplete
    def manage_proxy(self, roles=(), REQUEST=None):
        """Change Proxy Roles"""
    def PUT(self, REQUEST, RESPONSE):
        """Handle HTTP PUT requests"""
    manage_FTPput = PUT
    def write(self, text) -> None:
        """Change the Script by parsing a read()-style source text."""
    def manage_DAVget(self):
        """Get source for WebDAV"""
    manage_FTPget = manage_DAVget
    def read(self):
        """Generate a text representation of the Script source.

        Includes specially formatted comment lines for parameters,
        bindings, and the title.
        """
    def params(self): ...
    def body(self): ...
    def get_size(self): ...
    getSize = get_size
    def PrincipiaSearchSource(self):
        """Support for searching - the document's contents are searched."""
    def document_src(self, REQUEST=None, RESPONSE=None):
        """Return unprocessed document source."""

class PythonScriptTracebackSupplement:
    """Implementation of ITracebackSupplement"""

    object: Incomplete
    line: Incomplete
    def __init__(self, script, line: int = 0) -> None: ...
