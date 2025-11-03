from _typeshed import Incomplete

log: Incomplete
generated: Incomplete
transient: Incomplete
FTI_CACHE_KEY: str

def invalidate_cache(fti) -> None: ...
def lookup_fti(portal_type, cache: bool = True): ...
def volatile(func): ...

class SchemaCache:
    """Simple schema cache for FTI based schema information.

    This cache will store a Python object reference to the schema, as returned
    by fti.lookupSchema(), for any number of portal types. The value will
    be cached until the server is restarted or the cache is invalidated or
    cleared.

    You should only use this if you require bare-metal speed. For almost all
    operations, it's safer and easier to do:

        >> fti = getUtility(IDexterityFTI, name=portal_type)
        >> schema = fti.lookupSchema()

    The lookupSchema() call is probably as fast as this cache. However, if
    you need to avoid the utility lookup, you can use the cache like so:

        >> from plone.dexterity.schema import SCHEMA_CACHE
        >> my_schema = SCHEMA_CACHE.get(portal_type)

    The cache uses the FTI's modification time as its invariant.
    """

    lock: Incomplete
    cache_enabled: Incomplete
    invalidations: int
    def __init__(self, cache_enabled: bool = True) -> None: ...
    @volatile
    def get(self, fti):
        """main schema

        magic! fti is passed in as a string (identifier of fti), then volatile
        decorator looks it up and passes the FTI instance in.
        """
    @volatile
    def behavior_registrations(self, fti):
        """all behavior behavior registrations of a given fti passed in as
        portal_type string (magic see get)

        returns a tuple with instances of
        ``plone.behavior.registration.BehaviorRegistration`` instances
        for the given fti.
        """
    @volatile
    def subtypes(self, fti):
        """all registered marker interfaces of ftis behaviors

        XXX: this one does not make much sense and should be deprecated
        """
    @volatile
    def behavior_schema_interfaces(self, fti):
        """behavior schema interfaces registered for the fti

        all schemas from behaviors
        """
    @volatile
    def schema_interfaces(self, fti):
        """all schema interfaces registered for the fti

        main_schema plus schemas from behaviors
        """
    def clear(self) -> None: ...
    def invalidate(self, fti) -> None: ...
    @volatile
    def modified(self, fti): ...

SCHEMA_CACHE: Incomplete

class SchemaInvalidatedEvent:
    portal_type: Incomplete
    def __init__(self, portal_type) -> None: ...

def invalidate_schema(event) -> None: ...

class SchemaNameEncoder:
    """Schema name encoding"""

    key: Incomplete
    def encode(self, s): ...
    def decode(self, s): ...
    def join(self, *args): ...
    def split(self, s): ...

def portalTypeToSchemaName(portal_type, schema: str = "", prefix=None, suffix=None):
    """Return a canonical interface name for a generated schema interface."""

def schemaNameToPortalType(schemaName):
    """Return a the portal_type part of a schema name"""

def splitSchemaName(schemaName):
    """Return a tuple prefix, portal_type, schemaName"""

class SchemaModuleFactory:
    """Create dynamic schema interfaces on the fly"""

    lock: Incomplete
    def __call__(self, name, module):
        """Someone tried to load a dynamic interface that has not yet been
        created yet. We will attempt to load it from the FTI if we can. If
        the FTI doesn't exist, create a temporary marker interface that we
        can fill later.

        The goal here is to ensure that we create exactly one interface
        instance for each name. If we can't find an FTI, we'll cache the
        interface so that we don't get a new one with a different id later.
        This cache is global, so we synchronise the method with a thread
        lock.

        Once we have a properly populated interface, we set it onto the
        module using setattr(). This means that the factory will not be
        invoked again.
        """

class DexteritySchemaPolicy:
    """Determines how and where imported dynamic interfaces are created.
    Note that these schemata are never used directly. Rather, they are merged
    into a schema with a proper name and module, either dynamically or
    in code.
    """
    def module(self, schemaName, tree): ...
    def bases(self, schemaName, tree): ...
    def name(self, schemaName, tree): ...
