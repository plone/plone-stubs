from _typeshed import Incomplete
from zope.interface import Interface
from zope.schema.interfaces import IField
from zope.schema.interfaces import InvalidDottedName

class InvalidRegistryKey(InvalidDottedName):
    """A registry key is a dotted name with up to one '/'."""

class IPersistentField(IField):
    """A field that can be persistent along with a record.

    We provide our own implementation of the basic field types that are
    supported by the registry.

    A persistent field may track which interface and field it originally
    was constructed from. This is done by the registerInterface() method
    on the IRegistry, for example. Only the interface/field names are stored,
    not actual object references.
    """

    interfaceName: Incomplete
    fieldName: Incomplete

class IFieldRef(Interface):
    """A reference to another field.

    This allows a record to use a field that belongs to another record. Field
    refs are allowed in the Record() constructor.

    Note that all attributes are read-only.
    """

    recordName: Incomplete
    originalField: Incomplete

class IRecord(Interface):
    """A record stored in the registry.

    A record may be "bound" or "unbound". If bound, it will have a
    __parent__ attribute giving the IRegistry it belongs to. It will then
    get and set its field and value attributes from the internal storage in
    the registry. If unbound, it will store its own values.

    A record becomes bound when added to the registry. Records retrieved from
    the registry are always bound.
    """

    field: Incomplete
    value: Incomplete

class IRecordEvent(Interface):
    """Base interface for record level events"""

    record: Incomplete

class IRecordAddedEvent(IRecordEvent):
    """Event fired when a record is added to a registry."""

class IRecordRemovedEvent(IRecordEvent):
    """Event fired when a record is removed from a registry."""

class IRecordModifiedEvent(IRecordEvent):
    """Event fired when a record's value is modified."""

    oldValue: Incomplete
    newValue: Incomplete

class IInterfaceAwareRecord(Interface):
    """A record will be marked with this interface if it knows which
    interface its field came from.
    """

    interfaceName: Incomplete
    interface: Incomplete
    fieldName: Incomplete

class IRegistry(Interface):
    """The configuration registry"""

    records: Incomplete
    def __getitem__(key) -> None:
        """Get the value under the given key. A record must have been
        installed for this key for this to be valid. Otherwise, a KeyError is
        raised.
        """
    def get(key, default=None) -> None:
        """Attempt to get the value under the given key. If it does not
        exist, return the given default.
        """
    def __setitem__(key, value) -> None:
        """Set the value under the given key. A record must have been
        installed for this key for this to be valid. Otherwise, a KeyError is
        raised. If value is not of a type that's allowed by the record, a
        ValidationError is raised.
        """
    def __contains__(key) -> bool:
        """Determine if the registry contains a record for the given key."""
    def forInterface(interface, check: bool = True, omit=(), prefix=None) -> None:
        """Get an IRecordsProxy for the given interface. If `check` is True,
        an error will be raised if one or more fields in the interface does
        not have an equivalent setting.
        """
    def registerInterface(interface, omit=(), prefix=None) -> None:
        """Create a set of records based on the given interface. For each
        schema field in the interface, a record will be inserted with a
        name like `${interface.__identifier__}.${field.__name__}`, and a
        value equal to default value of that field. Any field with a name
        listed in `omit`, or with the `readonly` property set to True, will
        be ignored. Supply an alternative identifier with `prefix`.
        """

class IRecordsProxy(Interface):
    """This object is returned by IRegistry.forInterface(). It will be
    made to provide the relevant interface, i.e. it will have the
    attributes that the interface promises. Those attributes will be retrieved
    from or written to the underlying IRegistry.
    """

    __schema__: Incomplete
    __registry__: Incomplete
    __omitted__: Incomplete
