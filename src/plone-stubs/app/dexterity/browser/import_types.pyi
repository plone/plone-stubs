from _typeshed import Incomplete
from Products.GenericSetup.context import BaseContext
from z3c.form import form
from zope.interface import Interface
from zope.interface import invariant

class ITypeProfileImport(Interface):
    """Fields for a zip import form"""

    profile_file: Incomplete
    @invariant
    def isGoodImportFile(data) -> None: ...

class TypeProfileImport:
    form_fields: Incomplete
    profile_file: Incomplete
    def __init__(self, profile_file) -> None: ...

class TypeProfileImportForm(form.AddForm):
    label: Incomplete
    description: Incomplete
    fields: Incomplete
    id: str
    def create(self, data): ...
    status: Incomplete
    def add(self, profile_import) -> None: ...
    def nextURL(self): ...

TypeProfileImportFormPage: Incomplete

class ZipFileImportContext(BaseContext):
    """GS Import context for a ZipFile"""

    name_list: Incomplete
    def __init__(
        self, tool, archive_bits, encoding=None, should_purge: bool = False
    ) -> None: ...
    def readDataFile(self, filename, subdir=None): ...
    def getLastModified(self, path): ...
    def isDirectory(self, path):
        """See IImportContext"""
    def listDirectory(self, path, skip=[]):
        """See IImportContext"""
