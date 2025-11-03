from _typeshed import Incomplete

def exportSiteStructure(context) -> None: ...
def importSiteStructure(context) -> None: ...

class FolderishExporterImporter:
    """Tree-walking exporter / importer for "folderish" types.

    Folderish instances are mapped to directories within the \'structure\'
    portion of the profile, where the folder\'s relative path within the site
    corresponds to the path of its directory under \'structure\'.

    The subobjects of a folderish instance are enumerated in the \'.objects\'
    file in the corresponding directory.  This file is a CSV file, with one
    row per subobject, with the following wtructure::

     "<subobject id>","<subobject portal_type>"

    Subobjects themselves are represented as individual files or
    subdirectories within the parent\'s directory.
    """

    context: Incomplete
    def __init__(self, context) -> None: ...
    def listExportableItems(self):
        """See IFilesystemExporter."""
    def export(self, export_context, subdir, root: bool = False) -> None:
        """See IFilesystemExporter."""
    def import_(self, import_context, subdir, root: bool = False) -> None:
        """See IFilesystemImporter."""

class CSVAwareFileAdapter:
    """Adapter for content whose "natural" representation is CSV."""

    context: Incomplete
    def __init__(self, context) -> None: ...
    def export(self, export_context, subdir, root: bool = False) -> None:
        """See IFilesystemExporter."""
    def listExportableItems(self):
        """See IFilesystemExporter."""
    def import_(self, import_context, subdir, root: bool = False) -> None:
        """See IFilesystemImporter."""

class INIAwareFileAdapter:
    """Exporter/importer for content whose "natural" representation is an
    \'.ini\' file.
    """

    context: Incomplete
    def __init__(self, context) -> None: ...
    def export(self, export_context, subdir, root: bool = False) -> None:
        """See IFilesystemExporter."""
    def listExportableItems(self):
        """See IFilesystemExporter."""
    def import_(self, import_context, subdir, root: bool = False) -> None:
        """See IFilesystemImporter."""

class SimpleINIAware:
    """Exporter/importer for content which doesn't know from INI."""

    context: Incomplete
    def __init__(self, context) -> None: ...
    def getId(self): ...
    def as_ini(self):
        """ """
    def put_ini(self, text) -> None:
        """ """

class FauxDAVRequest:
    def __init__(self, **kw) -> None: ...
    def __getitem__(self, key): ...
    def get(self, key, default=None): ...
    def get_header(self, key, default=None): ...

class FauxDAVResponse:
    def setHeader(self, key, value, lock: bool = False) -> None: ...
    def setStatus(self, value, reason=None) -> None: ...

class DAVAwareFileAdapter:
    """Exporter/importer for content who handle their own FTP / DAV PUTs."""

    context: Incomplete
    def __init__(self, context) -> None: ...
    def export(self, export_context, subdir, root: bool = False) -> None:
        """See IFilesystemExporter."""
    def listExportableItems(self):
        """See IFilesystemExporter."""
    def import_(self, import_context, subdir, root: bool = False) -> None:
        """See IFilesystemImporter."""
