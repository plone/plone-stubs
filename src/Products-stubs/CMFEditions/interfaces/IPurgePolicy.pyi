from zope.interface import Interface

class IPurgePolicy(Interface):
    """Purge Policy

    Purge versions in a history according a policy. The methods declared
    are called by a ``IStorage`` implementation.
    """
    def beforeSaveHook(history_id, obj, metadata={}) -> None:
        """Purge Versions from the History According a Policy

        The Policy has full control over the whole history of the resource
        and may decide to purge or alter versions in the history.

        Called before the current version is saved to the storage.
        The metadata passed is the metadata that was passed to the
        ``save`` method.

        Return True if ``obj`` has to be saved by the ``IStorage``
        implementation. Return ``False`` if the object has to be discarded.
        """
    def retrieveSubstitute(history_id, selector, default=None) -> None:
        """Return a selected version of an object or a substitute

        Called by the storage if the object to be retrieved was purged.
        Implement the policy in case a client tries to retrieve a purged
        version.

        Return a substitute of ``IVersionData`` type.
        """
