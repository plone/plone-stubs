from _typeshed import Incomplete
from Products.GenericSetup.content import DAVAwareFileAdapter

def exportSiteStructure(context) -> None: ...
def importSiteStructure(context) -> None: ...
def encode_if_needed(text, encoding): ...

class FolderishDAVAwareFileAdapter(DAVAwareFileAdapter):
    """A version of the DAVAwareFileAdapter that uses .properties to store
    the DAV result, rather than its own id. For use in serialising folderish
    objects."""

class StructureFolderWalkingAdapter:
    """Tree-walking exporter for "folderish" types.

    Folderish instances are mapped to directories within the \'structure\'
    portion of the profile, where the folder\'s relative path within the site
    corresponds to the path of its directory under \'structure\'.

    The subobjects of a folderish instance are enumerated in the \'.objects\'
    file in the corresponding directory.  This file is a CSV file, with one
    row per subobject, with the following wtructure::

     "<subobject id>","<subobject portal_type>"

    Subobjects themselves are represented as individual files or
    subdirectories within the parent\'s directory.
    If the import step finds that any objects specified to be created by the
    \'structure\' directory setup already exist, these objects will be deleted
    and then recreated by the profile.  The existence of a \'.preserve\' file
    within the \'structure\' hierarchy allows specification of objects that
    should not be deleted.  \'.preserve\' files should contain one preserve
    rule per line, with shell-style globbing supported (i.e. \'b*\' will match
    all objects w/ id starting w/ \'b\'.

    Similarly, a \'.delete\' file can be used to specify the deletion of any
    objects that exist in the site but are NOT in the \'structure\' hierarchy,
    and thus will not be recreated during the import process.
    """

    context: Incomplete
    def __init__(self, context) -> None: ...
    def read_data_file(self, import_context, datafile, subdir): ...
    def export(self, export_context, subdir, root: bool = False) -> None:
        """See IFilesystemExporter."""
    def import_(self, import_context, subdir, root: bool = False) -> None:
        """See IFilesystemImporter."""
