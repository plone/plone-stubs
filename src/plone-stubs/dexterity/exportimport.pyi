from _typeshed import Incomplete
from Products.GenericSetup.content import FolderishExporterImporter

class DexterityContentExporterImporter(FolderishExporterImporter):
    """Tree-walking exporter / importer for Dexterity types.

    This is based on the generic one in GenericSetup,
    but it uses Dexterity\'s rfc822 serialization support
    to serialize the content.

    Folderish instances are mapped to directories within the \'structure\'
    portion of the profile, where the folder\'s relative path within the site
    corresponds to the path of its directory under \'structure\'.

    The subobjects of a folderish instance are enumerated in the \'.objects\'
    file in the corresponding directory.  This file is a CSV file, with one
    row per subobject, with the following structure::

     "<subobject id>","<subobject portal_type>"

    Subobjects themselves are represented as individual files or
    subdirectories within the parent\'s directory.
    """

    context: Incomplete
    def __init__(self, context) -> None: ...
    def export(self, export_context, subdir, root: bool = False) -> None:
        """See IFilesystemExporter."""
    def import_(self, import_context, subdir, root: bool = False) -> None:
        """See IFilesystemImporter."""
