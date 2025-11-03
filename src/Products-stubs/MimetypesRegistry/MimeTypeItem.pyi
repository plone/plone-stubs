from _typeshed import Incomplete
from Acquisition import Explicit
from OFS.SimpleItem import Item
from Persistence import Persistent

class MimeTypeItem(Persistent, Explicit, Item):
    security: Incomplete
    extensions: Incomplete
    globs: Incomplete
    mimetypes: Incomplete
    binary: Incomplete
    icon_path: Incomplete
    def __init__(
        self,
        name: str = "",
        mimetypes=None,
        extensions=None,
        binary=None,
        icon_path: str = "",
        globs=None,
    ) -> None: ...
    def __cmp__(self, other): ...
    def __hash__(self): ...
    @security.public
    def name(self):
        """The name of this object"""
    @security.public
    def major(self):
        """return the major part of the RFC-2046 name for this mime type"""
    @security.public
    def minor(self):
        """return the minor part of the RFC-2046 name for this mime type"""
    @security.public
    def normalized(self):
        """return the main RFC-2046 name for this mime type

        e.g. if this object has names ('text/restructured', 'text-x-rst')
        then self.normalized() will always return the first form.
        """
    @security.public
    def urlsafe(self):
        """Return a url safe version of the normalized version of this
        mime type.
        """
    def edit(
        self,
        name,
        mimetypes,
        extensions,
        icon_path,
        binary: int = 0,
        globs=None,
        REQUEST=None,
    ) -> None:
        """edit this mime type"""

ICONS_DIR: Incomplete
PREFIX: str

def guess_icon_path(mimetype, icons_dir=..., icon_ext: str = "png"): ...
