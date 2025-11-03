from _typeshed import Incomplete
from collections.abc import Generator
from plone.dexterity.schema import portalTypeToSchemaName as portalTypeToSchemaName
from plone.dexterity.schema import SchemaNameEncoder as SchemaNameEncoder
from plone.dexterity.schema import schemaNameToPortalType as schemaNameToPortalType
from plone.dexterity.schema import splitSchemaName as splitSchemaName

log: Incomplete

def resolveDottedName(dottedName):
    """Resolve a dotted name to a real object"""

def iterSchemataForType(portal_type) -> Generator[Incomplete, Incomplete]:
    """XXX: came from plone.app.deco.utils, very similar to iterSchemata

    Not fully merged codewise with iterSchemata as that breaks
    test_webdav.test_readline_mimetype_additional_schemata.
    """

def iterSchemata(context) -> Generator[Incomplete, Incomplete]:
    """Return an iterable containing first the object's schema, and then
    any form field schemata for any enabled behaviors.
    """

def getAdditionalSchemata(context=None, portal_type=None) -> Generator[Incomplete]:
    """Get additional schemata for this context or this portal_type.

    Additional form field schemata can be defined in behaviors.

    Usually either context or portal_type should be set, not both.
    The idea is that for edit forms or views you pass in a context
    (and we get the portal_type from there) and for add forms you pass
    in a portal_type (and the context is irrelevant then).  If both
    are set, the portal_type might get ignored, depending on which
    code path is taken.
    """

def createContent(portal_type, **kw): ...
def addContentToContainer(container, object, checkConstraints: bool = True):
    """Add an object to a container.

    The portal_type must already be set correctly. If checkConstraints
    is False no check for addable content types is done. The new object,
    wrapped in its new acquisition context, is returned.
    """

def createContentInContainer(
    container, portal_type, checkConstraints: bool = True, **kw
): ...
def safe_utf8(st): ...
def safe_unicode(st): ...
def datify(in_date):
    """Get a DateTime object from a string (or anything parsable by DateTime,
    a datetime.date, a datetime.datetime
    """

def all_merged_tagged_values_dict(ifaces, key):
    """mergedTaggedValueDict of all interfaces for a given key

    usually interfaces is a list of schemas
    """
