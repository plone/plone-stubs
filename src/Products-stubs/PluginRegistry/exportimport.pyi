from _typeshed import Incomplete
from collections.abc import Generator
from Products.GenericSetup.utils import ExportConfiguratorBase
from Products.GenericSetup.utils import ImportConfiguratorBase

def exportPluginRegistry(context):
    """Export plugin registry as an XML file.

    o Designed for use as a GenericSetup export step.
    """

def importPluginRegistry(context):
    """Import plugin registry from an XML file.

    o Designed for use as a GenericSetup import step.
    """

class PluginRegistryExporter(ExportConfiguratorBase):
    context: Incomplete
    def __init__(self, context, encoding: str = "utf-8") -> None: ...
    def listPluginTypes(self) -> Generator[Incomplete]: ...

class PluginRegistryImporter(ImportConfiguratorBase):
    context: Incomplete
    def __init__(self, context, encoding: str = "utf-8") -> None: ...

class PluginRegistryFileExportImportAdapter:
    """Designed for ues when exporting / importing PR's within a container."""

    context: Incomplete
    def __init__(self, context) -> None: ...
    def export(self, export_context, subdir, root: bool = False) -> None:
        """See IFilesystemExporter."""
    def listExportableItems(self):
        """See IFilesystemExporter."""
    def import_(self, import_context, subdir, root: bool = False) -> None:
        """See IFilesystemImporter."""
