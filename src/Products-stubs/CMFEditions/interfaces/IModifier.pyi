from zope.interface import Interface

class IAttributeModifier(Interface):
    """The simplest possible modifier, it indicates, which attributes
    shouldn't be copied by the archivist, but be passed to the the storage
    by reference.

    """
    def getReferencedAttributes(obj) -> None:
        """Returns attributes which should be passe dto the storage by reference.

        Returns a dict of the format ``name:attribute``.
        """
    def reattachReferencedAttributes(obj, attrs_dict) -> None:
        """Giving an obj and and an attribute dict composed by
        attribute names and values, reattach them to the obj.
        """

class ICloneModifier(Interface):
    """Modifies an object on save to or retrieval from a repository storage.

    A modifier knows how to manipulate an object being under version control
    on save to and on retrieval from the repositories storage.

    """
    def getOnCloneModifiers(obj) -> None:
        """Returns modifier callbacks being called during clone.

        Use this to manipulate objects during cloning to avoid excessive
        recursing of the clone operator eating much CPU and RAM.

        Returns a tuple consisting of a pickle peristent_id callback,
        a pickle persistent_load callback, two lists of 'IAttributeAdapter'
        objects adapting to a referenced object (inside references and
        outside references) and a name. The name may be an empty string.

        Returns just 'None' if no modifier callbacks have to be called.

        XXX Argh, this description is shit!
        """

class ISaveRetrieveModifier(Interface):
    """Modifies an object on save to or retrieval from a repository storage.

    A modifier knows how to manipulate an object being under version control
    on save to and on retrieval from the repositories storage.

    """
    def beforeSaveModifier(obj, obj_clone) -> None:
        """Modifies the object before being saved to the repos storage.

        Preprocesses the objects clone before it gets saved to
        the repositories storage. The copy is an unwrapped deep copy
        of the original object ('obj').

        Usually this hook is used to do one or more of the following
        tasks:

            - manipulate data before it get versioned
            - remove data that should not be versioned (or aren't
              versionable at all) and wasn't removed already by the
              'getOnCloneModifiers'.

        Returns a dict with metadata to be added to the sys_metadata dict
        and two lists of 'IAttributeAdapter' objects adapting to a
        'IVersionAwareReference' objects (inside references and outside
        references).

        XXX Argh, this description is shit!
        """
    def afterRetrieveModifier(obj, repo_clone, preserve=()) -> None:
        """Modifies the object after being retrieved from the repos storage.

        Postprocesses the copy of an objects version after it has been
        retrieved from the repositories storage. The repository copy is a
        reference to an unwrapped deep copy of a version previously
        saved to the repositories storage.

        Usually this hook is used to do one or more of the following
        tasks:

            - re-add data that was removed by the 'beforeSaveHook'
            - manipulate data before it get restored
            - return data that gets overwrite in this process

        It does kind of the inverse of the method ``beforeSaveModifier``.

        'obj' may be None. This signifies there is no working copy object.

        Returns:

        - a list of references to be deleted on revert (providing
          ``IReferenceAdapter``)
        - a list of attribute names being in charge of holding reference
          information (e.g. an ObjectManager with ``doc1`` and ``doc2``
          as children: ['_objects', 'doc1', 'doc2'])
        - a dictionary of the data having been preserved from being
          overwritten.
        """

class IReferenceAdapter(Interface):
    """Adapts to a references.

    Currently used to be able to remove a reference without having to
    know how.
    """
    def remove() -> None:
        """Removes the reference adapted to."""

class IModifierRegistrySet(Interface):
    """Registering and editing a modifier registry."""
    def register(id, modifier, pos: int = -1) -> None:
        """Registers a before save and after retrieve modifier.

        If no 'pos' argument is passed the modifier gets added at the
        end of the registry.
        """
    def unregister(id) -> None:
        """Unregisters a before save and after retrieve modifier.

        Unregistering can be done by passing the method the id or
        the position.
        """
    def edit(id, enabled=None, condition=None) -> None:
        """Edits a before save and after retrieve modifier.

        None values leave the respective parameter unchanged.

        The respective modifier only gets called if it is enabled and
        the 'condition' evaluates to a True value.
        """

class IModifierRegistryQuery(Interface):
    """Querying a modifier registry."""
    def get(id) -> None:
        """Returns the conditional modifier with the given id.

        Returns a 'IConditionalModifier' object.

        Raises an exception if the item doesn't exist.
        """
    def query(id, default=None) -> None:
        """Returns the condition and the modifier with the given id.

        Returns the default value if the item does not exist..
        """

class IConditionalModifier(Interface):
    """A modifier with a condition.

    The modifiers get only called if it is enabled and if a possibly
    existing implicit condition evaluates to a true value.
    """
    def __init__(id, modifier, title: str = "") -> None:
        """Initialize with a modifier.

        The conditional modifier is disabled by default.
        """
    def edit(enabled=None) -> None:
        """Modifies an existing conditional modifier.

        None values leave the respective parameter unchanged.
        """
    def isApplicable(obj, portal=None) -> None:
        """Returns True if the modifier is applicable.

        A modifier is applicable if it is enabled and if an additional
        condition evaluates to a true value.
        """
    def isEnabled() -> None:
        """Returns the enable status."""
    def getModifier() -> None:
        """Returns the modifier."""

class IConditionalTalesModifier(IConditionalModifier):
    """A modifier with a condition.

    The modifiers get only called if it is enabled and if the TALES
    condition evaluates to a true value.
    """
    def edit(enabled=None, condition=None) -> None:
        """Modifies an existing conditional TALES modifier.

        'condition' is a TALES expression.

        None values leave the respective parameter unchanged.
        """
    def getTalesCondition() -> None:
        """Returns the TALES expression."""

class IBulkEditableModifierRegistry(Interface):
    """A extension of a modifier registry that allows bulk editing.

    Used for management screens.
    """
    def listModifiers() -> None:
        """Returns the subscribers in string format for use in forms.

        Returns a list of dictionaries with the following keys:

            id -- the id of the subscriber
            pos -- the position of the subscriber in the history
            before_save -- a string representation of the "before save
                           subscriber"
            after_retrieve -- a string representation of the "after
                              retrieve subscriber"
            on_clone -- a string representation of the "on clone"
                        modifier.
            editable -- A flag signalizing if the subscribers are
                        editable
        """
    def setModifiers(ids, pos, before_save, after_retrieve, on_clone) -> None:
        """Replaces all the subscribers passed

        Use this to set all subscribers at once from a form.
        """

class ModifierException(Exception):
    """A base class for exceptions thrown by modifiers which wish to abort
    a save operation"""

class FileTooLargeToVersionError(ModifierException):
    """A simple exception indicating that an object contained a file
    object that was too large to support versioning, and that versioning
    will be aborted as a result"""
