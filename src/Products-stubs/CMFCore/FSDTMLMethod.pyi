from .FSObject import FSObject
from _typeshed import Incomplete
from App.special_dtml import HTML
from DocumentTemplate.security import RestrictedDTML
from OFS.role import RoleManager

class FSDTMLMethod(RestrictedDTML, RoleManager, FSObject, HTML):
    """FSDTMLMethods act like DTML methods but are not directly
    modifiable from the management interface.
    """

    meta_type: str
    zmi_icon: str
    manage_options: Incomplete
    security: Incomplete
    manage_main: Incomplete
    encoding: Incomplete
    def __init__(self, id, filepath, fullname=None, properties=None) -> None: ...
    @security.private
    def read_raw(self): ...
    index_html: Incomplete
    __code__: Incomplete
    default_content_type: str
    def __call__(self, client=None, REQUEST={}, RESPONSE=None, **kw):
        """Render the document given a client object, REQUEST mapping,
        Response, and key word arguments."""
    def getCacheNamespaceKeys(self):
        """
        Returns the cacheNamespaceKeys.
        """
    def setCacheNamespaceKeys(self, keys, REQUEST=None):
        """
        Sets the list of names that should be looked up in the
        namespace to provide a cache key.
        """
    def validate(self, inst, parent, name, value, md=None): ...
    manage_FTPget: Incomplete
    PrincipiaSearchSource: Incomplete
    document_src: Incomplete
    manage_haveProxy: Incomplete
