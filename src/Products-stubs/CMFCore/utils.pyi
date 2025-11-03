from _typeshed import Incomplete
from Acquisition import Implicit
from ExtensionClass import Base
from OFS.PropertyManager import PropertyManager
from OFS.SimpleItem import SimpleItem

HAS_ZSERVER: bool
dist: Incomplete
SUBTEMPLATE: str
ProductsPath: Incomplete
security: Incomplete

@security.private
def registerToolInterface(tool_id, tool_interface) -> None:
    """Register a tool ID for an interface

    This method can go away when getToolByName is going away
    """

@security.private
def getToolInterface(tool_id):
    """Get the interface registered for a tool ID"""

@security.public
def getToolByName(obj, name, default=...):
    """Get the tool, 'toolname', by acquiring it.

    o Application code should use this method, rather than simply
      acquiring the tool by name, to ease forward migration (e.g.,
      to Zope3).
    """

@security.public
def getUtilityByInterfaceName(dotted_name, default=...):
    """Get a tool by its fully-qualified dotted interface path

    This method replaces getToolByName for use in untrusted code.
    Trusted code should use zope.component.getUtility instead.
    """

@security.public
def cookString(text):
    """Make a Zope-friendly ID from 'text'.

    o Remove any spaces

    o Lowercase the ID.
    """

@security.public
def tuplize(valueName, value):
    """Make a tuple from 'value'.

    o Use 'valueName' to generate appropriate error messages.
    """

class FakeExecutableObject:
    """Fake ExecutableObject used to set proxy roles in trusted code."""
    def __init__(self, proxy_roles) -> None: ...
    def getOwner(self) -> None: ...
    getWrappedOwner = getOwner

parse_etags_lock: Incomplete

def parse_etags(
    text, result=None, etagre_quote=..., etagre_noquote=..., acquire=..., release=...
): ...

class _ViewEmulator(Implicit):
    """Auxiliary class used to adapt FSFile and FSImage
    for caching_policy_manager
    """
    def __init__(self, view_name: str = "") -> None: ...
    def getId(self): ...

class ImmutableId(Base):
    """Base class for objects which cannot be renamed."""

class UniqueObject(ImmutableId):
    """Base class for objects which cannot be "overridden" / shadowed."""

    zmi_icon: str
    __replaceable__: Incomplete

class SimpleItemWithProperties(PropertyManager, SimpleItem):
    """
    A common base class for objects with configurable
    properties in a fixed schema.
    """

    manage_options: Incomplete
    security: Incomplete
    def manage_propertiesForm(self, REQUEST, *args, **kw):
        """An override that makes the schema fixed."""

class ToolInit:
    """Utility class for generating the factories for several tools."""

    security: Incomplete
    meta_type: Incomplete
    tools: Incomplete
    icon: Incomplete
    def __init__(self, meta_type, tools, product_name=None, icon=None) -> None: ...
    product_name: Incomplete
    def initialize(self, context) -> None: ...

addInstanceForm: Incomplete

def manage_addToolForm(self, REQUEST):
    """Show the add tool form."""

def manage_addTool(self, type, REQUEST=None):
    """Add the tool specified by name."""

class ContentInit:
    """Utility class for generating factories for several content types."""

    security: Incomplete
    meta_type: Incomplete
    content_types: Incomplete
    permission: Incomplete
    extra_constructors: Incomplete
    visibility: Incomplete
    def __init__(
        self,
        meta_type,
        content_types,
        permission=None,
        extra_constructors=(),
        fti=(),
        visibility: str = "Global",
    ) -> None: ...
    def initialize(self, context) -> None: ...

def manage_addContentForm(self, REQUEST):
    """Show the add content type form."""

def manage_addContent(self, id, type, REQUEST=None):
    """Add the content type specified by name."""

def registerIcon(klass, iconspec, _prefix=None) -> None:
    """Make an icon available for a given class.

    o 'klass' is the class being decorated.

    o 'iconspec' is the path within the product where the icon lives.
    """

KEYSPLITRE: Incomplete

@security.public
def keywordsplitter(headers, names=("Subject", "Keywords"), splitter=...):
    """Split keywords out of headers, keyed on names.  Returns list."""

CONTRIBSPLITRE: Incomplete

@security.public
def contributorsplitter(headers, names=("Contributors",), splitter=...):
    """Split contributors out of headers, keyed on names.  Returns list."""

@security.public
def normalize(p): ...
@security.private
def getContainingPackage(module): ...
@security.private
def getPackageLocation(module):
    """Return the filesystem location of a module.

    This is a simple wrapper around the global package_home method which
    tricks it into working with just a module name.
    """

@security.private
def getPackageName(globals_): ...

class SimpleRecord:
    """record-like class"""
    def __init__(self, **kw) -> None: ...

def base64_encode(text): ...
def base64_decode(text): ...

Message: Incomplete
