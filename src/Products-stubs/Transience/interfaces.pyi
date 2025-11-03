from zope.interface import Interface

class ITransient(Interface):
    def invalidate() -> None:
        """
        Invalidate (expire) the transient object.

        Causes the transient object container\'s "before destruct" method
        related to this object to be called as a side effect.
        """
    def isValid() -> None:
        """
        Return true if transient object is still valid, false if not.
        A transient object is valid if its invalidate method has not been
        called.
        """
    def getLastAccessed() -> None:
        """
        Return the time the transient object was last accessed in
        integer seconds-since-the-epoch form.  Last accessed time
        is defined as the last time the transient object\'s container
        "asked about" this transient object.
        """
    def setLastAccessed() -> None:
        """
        Cause the last accessed time to be set to now.
        """
    def getLastModified() -> None:
        """
        Return the time the transient object was last modified in
        integer seconds-since-the-epoch form.  Modification generally implies
        a call to one of the transient object's __setitem__ or __delitem__
        methods, directly or indirectly as a result of a call to
        update, clear, or other mutating data access methods.
        """
    def setLastModified() -> None:
        """
        Cause the last modified time to be set to now.
        """
    def getCreated() -> None:
        """
        Return the time the transient object was created in integer
        seconds-since-the-epoch form.
        """
    def getContainerKey() -> None:
        """
        Return the key under which the object was placed in its
        container.
        """

class IDictionaryLike(Interface):
    def keys() -> None:
        """Return sequence of key elements."""
    def values() -> None:
        """Return sequence of value elements."""
    def items() -> None:
        """Return sequence of (key, value) elements."""
    def get(k, default: str = "marker") -> None:
        """
        Return value associated with key k.  Return None or default if k
        does not exist.
        """
    def has_key(k) -> None:
        """Return true if item referenced by key k exists."""
    def __contains__(key) -> bool:
        """Return true if item referenced by key k exists."""
    def clear() -> None:
        """Remove all key/value pairs."""
    def update(d) -> None:
        """
        Merge dictionary d into ourselves.
        """

class IItemWithId(Interface):
    def getId() -> None:
        """
        Returns a meaningful unique id for the object.  Note that this id
        need not the key under which the object is stored in its container.
        """

class ITTWDictionary(IDictionaryLike, IItemWithId):
    def set(k, v) -> None:
        """
        Call __setitem__ with key k, value v.
        """
    def delete(k) -> None:
        """
        Call __delitem__ with key k.
        """
    def __guarded_setitem__(k, v) -> None:
        """
        Call __setitem__ with key k, value v.
        """

class IImmutablyValuedMappingOfPickleableObjects(Interface):
    def __setitem__(k, v) -> None:
        """
        Sets key k to value v, if k is both hashable and pickleable and
        v is pickleable, else raise TypeError.
        """
    def __getitem__(k) -> None:
        """
        Returns the value associated with key k.

        Note that no guarantee is made to persist changes made to mutable
        objects obtained via __getitem__, even if they support the ZODB
        Persistence interface.  In order to ensure that changes to mutable
        values are persisted, you need to explicitly put the value back in
        to the mapping via __setitem__.
        """
    def __delitem__(k) -> None:
        """
        Remove the key/value pair related to key k.
        """

class IHomogeneousItemContainer(Interface):
    """
    An object which:
     1.  Contains zero or more subobjects, all of the same type.
     2.  Is responsible for the creation of its subobjects.
     3.  Allows for the access of a subobject by key.
    """
    def get(k, default=None) -> None:
        """
        Return value associated with key k via __getitem__.  If value
        associated with k does not exist, return default.

        Returned item is acquisition-wrapped in self unless a default
        is passed in and returned.
        """
    def has_key(k) -> None:
        """
        Return true if container has value associated with key k, else
        return false.
        """

class IStringKeyedHomogeneousItemContainer(IHomogeneousItemContainer):
    def new(k) -> None:
        """
        Creates a new subobject of the type supported by this container
        with key "k" and returns it.

        If an object already exists in the container with key "k", a
        KeyError is raised.

        "k" must be a string, else a TypeError is raised.

        If the container is \'full\', a MaxTransientObjectsExceeded exception
        will be raised.

        Returned object is acquisition-wrapped in self.
        """
    def new_or_existing(k) -> None:
        """
        If an object already exists in the container with key "k", it
        is returned.

        Otherwise, create a new subobject of the type supported by this
        container with key "k" and return it.

        "k" must be a string, else a TypeError is raised.

        If a new object needs to be created and the container is \'full\',
        a MaxTransientObjectsExceeded exception will be raised.

        Returned object is acquisition-wrapped in self.
        """

class ITransientItemContainer(Interface):
    def setTimeoutMinutes(timeout_mins) -> None:
        """
        Set the number of minutes of inactivity allowable for subobjects
        before they expire.
        """
    def getTimeoutMinutes() -> None:
        """
        Return the number of minutes allowed for subobject inactivity
        before expiration.
        """
    def getAddNotificationTarget() -> None:
        """
        Returns the currently registered 'add notification' value, or None.
        """
    def setAddNotificationTarget(f) -> None:
        """
        Cause the \'add notification\' function to be \'f\'.

        If \'f\' is not callable and is a string, treat it as a physical
        path to a Zope Script object (Python Script, External Method,
        et. al).

        \'add notify\' functions need accept two arguments: \'item\',
        which is the transient object being destroyed, and \'container\',
        which is the transient object container which is performing
        the destruction.  For example::

          def addNotify(item, container):
              print("id of \'item\' arg was %s" % item.getId())
        """
    def getDelNotificationTarget() -> None:
        """
        Returns the currently registered 'delete notification' value, or
        None.
        """
    def setDelNotificationTarget(f) -> None:
        """
        Cause the \'delete notification\' function to be \'f\'.

        If \'f\' is not callable and is a string, treat it as a physical
        path to a Zope Script object (Python Script, External Method,
        et. al).

        \'Before destruction\' functions need accept two arguments: \'item\',
        which is the transient object being destroyed, and \'container\',
        which is the transient object container which is performing
        the destruction.  For example::

          def delNotify(item, container):
              print("id of \'item\' arg was %s" % item.getId())
        """
