from _typeshed import Incomplete
from Acquisition import Implicit
from Products.GenericSetup.content import DAVAwareFileAdapter
from Products.GenericSetup.content import FolderishExporterImporter

def getPackagePath(instance): ...

class SimpleXMLExportImport(Implicit):
    """Base for plugins whose configuration can be dumped to an XML file.

    o Derived classes must define:

      '_FILENAME' -- a class variable naming the export template

      '_getExportInfo' --  a method returning a mapping which will be passed
       to the template as 'info'.

      '_ROOT_TAGNAME' -- the name of the root tag in the XML (for sanity check)

      '_purgeContext' -- a method which clears our context.

      '_updateFromDOM' -- a method taking the root node of the DOM.
    """

    encoding: Incomplete
    context: Incomplete
    def __init__(self, context) -> None: ...
    def export(self, export_context, subdir, root: bool = False) -> None:
        """See IFilesystemExporter."""
    def listExportableItems(self):
        """See IFilesystemExporter."""
    def import_(self, import_context, subdir, root: bool = False) -> None:
        """See IFilesystemImporter"""

class ZODBUserManagerExportImport(SimpleXMLExportImport):
    """Adapter for dumping / loading ZODBUSerManager to an XML file."""

class ZODBGroupManagerExportImport(SimpleXMLExportImport):
    """Adapter for dumping / loading ZODBGroupManager to an XML file."""

class ZODBRoleManagerExportImport(SimpleXMLExportImport):
    """Adapter for dumping / loading ZODBGroupManager to an XML file."""

class CookieAuthHelperExportImport(SimpleXMLExportImport):
    """Adapter for dumping / loading CookieAuthHelper to an XML file."""

class DomainAuthHelperExportImport(SimpleXMLExportImport):
    """Adapter for dumping / loading DomainAuthHelper to an XML file."""

class TitleOnlyExportImport(SimpleXMLExportImport):
    """Adapter for dumping / loading title-only plugins to an XML file."""

class DelegatePathExportImport(SimpleXMLExportImport):
    """Adapter for dumping / loading plugins with 'delegate' via XML."""

class DynamicGroupsPluginExportImport(SimpleXMLExportImport):
    """Adapter for dumping / loading DynamicGroupsPlugin to an XML file."""

class ChallengeProtocolChooserExportImport(SimpleXMLExportImport):
    """Adapter for dumping / loading ChallengeProtocolChooser to an XML file."""

class ScriptablePluginExportImport(FolderishExporterImporter):
    """Export / import the Scriptable type plugin."""
    def export(self, export_context, subdir, root: bool = False) -> None:
        """See IFilesystemExporter."""
    def import_(self, import_context, subdir, root: bool = False) -> None:
        """See IFilesystemImporter."""

class PythonScriptFileAdapter(DAVAwareFileAdapter):
    """File-ish for PythonScript."""

class NotCompetent_byRolesExportImport(SimpleXMLExportImport):
    """Adapter for dumping / loading NCbR plugin."""
