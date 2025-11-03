from _typeshed import Incomplete
from zope.interface import Interface

class IStorage(Interface):
    """Manages Storing and Retrieving Version to and from the Storage

    Every resource has it's own history.
    """
    def isRegistered(history_id) -> None:
        """Returns True if the object is already registered.

        A registered object has a history.
        """
    def register(history_id, object, referenced_data={}, metadata={}) -> None:
        """Sets up a new history for the object and does the first save.

        The 'object' and the 'referenced_data' together contain the whole
        data to be added to the history.

        'object' is already a clone and needn't be cloned anymore before
        being added to the history. Data in 'referenced_data' are direct
        references to the original object and must be cloned before being
        added to the history.

        'referenced_data' is a list or tuple of python references or
        'IStreamableReference' objects.

        'metadata' must be a (nested) dictionary. If a 'comment' key exists
        the implementation may assume it is a human readable string.

        May veto the registering process by raising a 'StorageError'
        exception. No action is performed on repeated registering.

        Returns the value of the newest version(selector).
        """
    def save(history_id, object, referenced_data={}, metadata={}) -> None:
        """Appends an object current state to a history.

        The 'object' and the 'referenced_data' together contain the whole
        data to be added to the history.

        'object' is already a clone and needn't be cloned anymore before
        being added to the history. Data in 'referenced_data' are direct
        references to the original object and must be cloned before being
        added to the history.

        'referenced_data' is a list or tuple of python references or
        'IStreamableReference' objects.

        'metadata' must be a (nested) dictionary. If a 'comment' key exists
        the implementation may assume it is a human readable string.

        Returns the value of the newest version(selector).
        """
    def retrieve(history_id, selector) -> None:
        """Returns a selected version of an object, which has the given
           history id.

        Returns a 'IVersionData' object.
        """
    def getHistory(history_id) -> None:
        """Return the history of an object by the given history id.

        Returns a 'IHistory' object.
        """
    def getHistoryMetadata(history_id) -> None:
        """Returns the versioning metadata history."""
    def getModificationDate(history_id, selector=None) -> None:
        """Returns the modification date of the selected version of object
            which has the given history id.

        If selected is None, the most recent version (HEAD) is taken.
        """

class IPurgeSupport(Interface):
    """Storage Purge Support

    Purging a version from the storage removes that version irrevocably.

    Adds ``purge`` and extends the signature of ``retrieve``, ``getHistory``
    and ``getModificationDate``. The defaults of the extended methods
    mimique the standard behaviour of the original methods.

    With the introduction of purging two selection scheme exist for
    retrieving versions. Either purged versions are taken into account
    or not:

    - By passing ``countPurged=True`` purged versions are taken into
      account when accessing a version. When a purged version is accessed
      the storage tool decides what to do.
    - By passing ``countPurged=False`` purged versions are **not taken into
      account** when accessing a version.

    Example:

    An object got saved ten times. Two versions got purged in earlier
    calls. The history looks like this (``s`` means: depends on storage,
    ``e`` means: exception raised)::

      countPurged==True:

        selector:          0, 1, 2, 3, 4, 5, 6, 7, 8, 9
        version retrieved: 0, 1, 2, s, s, 5, 6, 7, 8, 9

      countPurged==False:

        selector:          0, 1, 2, 3, 4, 5, 6, 7, 8, 9
        version retrieved: 0, 1, 2, 5, 6, 7, 8, 9, e, e
    """
    def purge(history_id, selector, metadata={}, countPurged: bool = True) -> None:
        """Purge a Version from a Resources History

        If ``countPurged`` is ``True`` version numbering counts purged
        versions also. If ``False`` purged versiona are not taken into
        account.

        Purge the given version from the given history. The metadata
        passed may be used to store information about the reasons of
        the purging.
        """
    def retrieve(
        history_id, selector, countPurged: bool = True, substitute: bool = True
    ) -> None:
        """Return the Version of the Resource with the given History Id

        If ``countPurged`` is ``True`` purged versions are taken into
        account also. If ``False`` purged versions are ignored and not
        taken into account in counting.

        If ``substitute`` is ``True`` a substitute is returned in case
        the requested version was purged before.

        Return a ``IVersionData`` object.
        """
    def getHistory(
        history_id, countPurged: bool = True, substitute: bool = True
    ) -> None:
        """Return the history of an object by the given history id.

        If ``countPurged`` is ``True`` purged versions are returned also.
        If ``False`` purged versions aren't returned.

        If ``substitute`` is ``True`` a substitute is returned in case
        the requested version was purged before.

        Return a ``IHistory`` object.
        """
    def getModificationDate(
        history_id, selector=None, countPurged: bool = True, substitute: bool = True
    ) -> None:
        """Returns the modification date of the selected version of object
            which has the given history id.

        If ``countPurged`` is ``True`` purged versions are returned also.
        If ``False`` purged versions aren't returned.

        If ``substitute`` is ``True`` a substitute is returned in case
        the requested version was purged before.

        If selected is None, the most recent version (HEAD) is taken.
        """

class IHistory(Interface):
    """Iterable version history."""
    def __len__() -> int:
        """Return the length of the history."""
    def __getattr__(version_id) -> None:
        """Return the version of an object corresponding to the version id.

        The item returned is of ``IVersionData``.
        """
    def __iter__():
        """Iterator returning the versions.

        The iterators ``next`` method returns ``IVersionData`` objects.
        """

class IVersionData(Interface):
    """ """

    object: Incomplete
    referenced_data: Incomplete
    metadata: Incomplete

class IStreamableReference(Interface):
    """Marks an object passed to the storage by reference as streamable.

    This allows the history storage to optimize saving and retrieving by
    e.g. avoiding pickling/unpickling. This is mostly interesting for
    long streams.
    """
    def __init__(self, obj) -> None:
        """Wrap the object to be passed to the storage"""
    def getObject(self) -> None:
        """Return the object"""
    def getSize(self) -> None:
        """Return the size of the streamable object or None"""

class StorageError(Exception):
    """History storage exception."""

class StorageRetrieveError(StorageError):
    """Raised if tried to retrieve a non existent version of a resource."""

class StorageRegisterError(StorageError):
    """Raised if registering the resource failed."""

class StorageSaveError(StorageError):
    """Raised if saving a new version of a resource failed."""

class StorageUnregisteredError(StorageError):
    """Raised if trying to save an unregistered resource."""

class StoragePurgeError(StorageError):
    """Raised if tried to purge a non existent version of a resource."""
