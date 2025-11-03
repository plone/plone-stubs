from _typeshed import Incomplete
from OFS.Folder import Folder
from Products.CMFCore.ActionProviderBase import ActionProviderBase
from Products.CMFCore.utils import UniqueObject

logger: Incomplete
suffix_map: Incomplete
encodings_map: Incomplete

class MimeTypesRegistry(UniqueObject, ActionProviderBase, Folder):
    """Mimetype registry that deals with
    a) registering types
    b) wildcarding of rfc-2046 types
    c) classifying data into a given type
    """

    id: str
    meta_type: str
    isPrincipiaFolderish: int
    meta_types: Incomplete
    all_meta_types: Incomplete
    manage_options: Incomplete
    manage_addMimeTypeForm: Incomplete
    manage_main: Incomplete
    manage_editMimeTypeForm: Incomplete
    security: Incomplete
    __allow_access_to_unprotected_subobjects__: int
    encodings_map: Incomplete
    suffix_map: Incomplete
    extensions: Incomplete
    globs: Incomplete
    def __init__(self, id=None) -> None: ...
    def register(self, mimetype) -> None:
        """Register a new mimetype

        mimetype must implement IMimetype
        """
    def register_mimetype(self, mt, mimetype) -> None: ...
    def register_extension(self, extension, mimetype) -> None:
        """Associate a file's extension to a IMimetype

        extension is a string representing a file extension (not
        prefixed by a dot) mimetype must implement IMimetype
        """
    def register_glob(self, glob, mimetype) -> None:
        """Associate a glob to a IMimetype

        glob is a shell-like glob that will be translated to a regex
        to match against whole filename.
        mimetype must implement IMimetype.
        """
    def unregister(self, mimetype) -> None:
        """Unregister a new mimetype

        mimetype must implement IMimetype
        """
    @security.public
    def mimetypes(self):
        """Return all defined mime types, each one implements at least
        IMimetype
        """
    @security.public
    def list_mimetypes(self):
        """Return all defined mime types, as string"""
    @security.public
    def lookup(self, mimetypestring):
        """Lookup for IMimetypes object matching mimetypestring

        mimetypestring may have an empty minor part or containing a
        wildcard (*) mimetypestring may and IMimetype object (in this
        case it will be returned unchanged

        Return a list of mimetypes objects associated with the
        RFC-2046 name return an empty list if no one is known.
        """
    @security.public
    def lookupExtension(self, filename):
        """Lookup for IMimetypes object matching filename

        Filename maybe a file name like 'content.txt' or an extension
        like 'rest'

        Return an IMimetype object associated with the file's
        extension or None
        """
    @security.public
    def globFilename(self, filename):
        """Lookup for IMimetypes object matching filename

        Filename must be a complete filename with extension.

        Return an IMimetype object associated with the glob's or None
        """
    @security.public
    def lookupGlob(self, glob): ...
    @security.public
    def classify(self, data, mimetype=None, filename=None):
        """Classify works as follows:
        1) you tell me the rfc-2046 name and I give you an IMimetype
           object
        2) the filename includes an extension from which we can guess
           the mimetype
        3) we can optionally introspect the data
        4) default to self.defaultMimetype if no data was provided
           else to application/octet-stream of no filename was provided,
           else to text/plain

        Return an IMimetype object or None
        """
    def __call__(self, data, **kwargs):
        """Return a triple (data, filename, mimetypeobject) given
        some raw data and optional parameters

        method from the isourceAdapter interface
        """
    @security.public
    def guess_encoding(self, data):
        """Try to guess encoding from a text value.

        If no encoding can be guessed, fall back to utf-8.
        """
    def manage_delObjects(self, ids, REQUEST=None) -> None:
        """delete the selected mime types"""
    def manage_addMimeType(
        self,
        id,
        mimetypes,
        extensions,
        icon_path,
        binary: int = 0,
        globs=None,
        REQUEST=None,
    ) -> None:
        """add a mime type to the tool"""
    def manage_editMimeType(
        self,
        name,
        new_name,
        mimetypes,
        extensions,
        icon_path,
        binary: int = 0,
        globs=None,
        REQUEST=None,
    ) -> None:
        """Edit a mime type by name"""

def split(name):
    """split a mime type in a (major / minor) 2-tuple"""
