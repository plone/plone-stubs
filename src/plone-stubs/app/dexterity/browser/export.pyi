from _typeshed import Incomplete
from Products.Five.browser import BrowserView
from Products.GenericSetup.context import TarballExportContext

class SelectiveZipExportContext(TarballExportContext):
    typelist: Incomplete
    filenames: Incomplete
    def __init__(
        self, tool, typelist, encoding=None, base_name: str = "setup_tool"
    ) -> None: ...
    def writeDataFile(self, filename, text, content_type, subdir=None) -> None: ...

class TypesExport(BrowserView):
    """Generate a types export archive for download"""
    def __call__(self): ...

class ModelsExport(BrowserView):
    """Generate an archive for download of model xml files for selected
    types.
    """
    def __call__(self): ...
