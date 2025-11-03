from Products.CMFCore.interfaces import ICallableOpaqueItem
from zope.interface import Interface

class UniqueIdError(Exception): ...

class IUniqueIdGenerator(Interface):
    """Generate a unique id."""
    def __call__() -> None:
        """Return a unique id value."""
    def convert(uid) -> None:
        """Converts the unique id from string type to the appropriate
           uid type.

        The resulting type has to be the same as the one '__call__'
        returns.
        """

class IUniqueIdAnnotationManagement(Interface):
    """Manage unique id annotations."""
    def __call__(obj, id) -> None:
        """Attach an unique id attribute of 'id' to the passed object.

        Return a unique id object implementing 'IUniqueIdAnnotation'.
        """

class IUniqueIdAnnotation(ICallableOpaqueItem):
    """Opaque unique id item handling adding, copying, and deletion events."""
    def setUid(uid) -> None:
        """Set the uid value the unique id annotation shall return."""

class IUniqueIdSet(Interface):
    """(Un)register unique ids on objects."""
    def register(obj) -> None:
        """Register the object and return the unique id generated for it.

        If the object is already registered, its unique id is returned anyway.

        UniqueIdError is raised if object can not be registered a unique id.
        """
    def unregister(obj) -> None:
        """Remove the object from the indexes.

        UniqueIdError is raised if object was not registered previously.
        """
    def setUid(obj, uid, check_uniqueness: bool = True) -> None:
        """Set the unique id of an object.

        By default a check ensuring uniqueness is enabled. Be aware when
        disabling this check: You really need to know what you do !!!
        """

class IUniqueIdQuery(Interface):
    """Querying unique ids."""
    def queryUid(obj, default=None) -> None:
        """Return the unique id of the object.

        If the object doesn't have a unique, the default value is returned.
        """
    def getUid(obj) -> None:
        """Return the unique id of the object.

        If the object doesn't have a unique, a UniqueIdError is raised.
        """
    def queryObject(uid, default=None) -> None:
        """Return the object with the given uid.

        If no object exist with the given unique id, the default value is
        returned.
        """
    def getObject(uid) -> None:
        """Return the object with the given uid.

        If no object exist with the given unique id, a UniqueIdError is raised.
        """

class IUniqueIdHandler(IUniqueIdSet, IUniqueIdQuery):
    """Handle registering, querying unique ids and objects."""

class IUniqueIdBrainQuery(Interface):
    """Querying unique ids returning brains for efficiency sake.

    Returning a brain is more efficient than returning the object. A brain
    usually exposes only parts of the object and should only be read from.

    If the implementing class doesn't support returning a catalog brain it may
    fallback to return the object. To be entirely compatible it must implement
    the (non existing) interface catalog brains implement.
    """
    def queryBrain(uid, default=None) -> None:
        """Return the brain of object with the given uid.

        If no object exist with the given unique id, the default value
        is returned.
        """
    def getBrain(uid) -> None:
        """Return a brain of the object with the given uid.

        If no object exist with the given unique id, a UniqueIdError is
        raised.
        """

class IUniqueIdUnrestrictedQuery(Interface):
    """Querying unique ids unrestricted.

    The below methods return not yet effective and already expired
    objects regardless of the roles the caller has.

    CAUTION: Care must be taken not to open security holes by exposing
    the results of these methods to non authorized callers!

    If you're in doubth if you should use this method signature or
    the restricted ones ('IUniqueIdQuery' and 'IUniqueIdBrainQuery')
    use the latter!

    Returning a brain is more efficient than returning the object. A brain
    usually exposes only parts of the object and should only be read from.

    If the implementing class doesn't support returning a catalog
    brain it may fallback to return the object. To be entirely
    compatible it must implement the (non existing) interface
    catalog brains implement.
    """
    def unrestrictedQueryObject(uid, default=None) -> None:
        """Return the object with the given uid.

        If no object exist with the given unique id, the default value
        is returned.
        """
    def unrestrictedGetObject(uid) -> None:
        """Return a brain of the object with the given uid.

        If no object exist with the given unique id, a UniqueIdError
        is raised.
        """
    def unrestrictedQueryBrain(uid, default=None) -> None:
        """Return the brain of the object with the given uid.

        If no object exist with the given unique id, the default value
        is returned.
        """
    def unrestrictedGetBrain(uid) -> None:
        """Return a brain of the object with the given uid.

        If no object exist with the given unique id, a UniqueIdError
        is raised.
        """
