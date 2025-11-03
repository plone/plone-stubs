from _typeshed import Incomplete
from zope.interface import Interface

class IBehaviorAssignable(Interface):
    """An object will be adapted to this interface to determine if it supports
    one or more behaviors.

    There is no default implementation of this adapter. The mechanism for
    assigning behaiors to an object or type of object is application specific.
    """
    def supports(behavior_interface) -> None:
        """Determine if the context supports the given behavior, returning
        True or False.
        """
    def enumerateBehaviors() -> None:
        """Return an iterable of all the IBehaviors supported by the context."""

class IBehavior(Interface):
    """A description of a behavior. These should be registered as named
    utilities. There should also be an adapter factory registered, probably
    using IBehaviorAdapterFactory.
    """

    title: Incomplete
    description: Incomplete
    name: Incomplete
    interface: Incomplete
    marker: Incomplete
    factory: Incomplete

class IBehaviorAdapterFactory(Interface):
    """An adapter factory that wraps a given behavior's own factory. By
    registering an adapter from Interface (or some other general source) to
    the behavior's interface that uses this factory, we can easily support
    the following semantics:

        context = SomeObject()
        behavior_adapter = ISomeBehavior(context, None)

     The ISomeBehavior adapter factory (i.e. the object providing
     IBehaviorAdapterFactory) will return None if
     IBehaviorAssignable(context).supports(ISomeBehavior) is False, or if
     the context cannot be adapted to IBehaviorAssignable at all.
    """

    behavior: Incomplete
    def __call__(context) -> None:
        """Invoke the behavior-specific factory if the context can be adapted
        to IBehaviorAssignable and
        IBehaviorAssignable(context).supports(self.behavior.interface) returns
        True.
        """

class ISchemaAwareFactory(Interface):
    """Marker interface for factories that should be initialised with a
    schema. The factory must be a callable that takes the schema as an
    argument and returns another callable that can create appropriate behavior
    factories on demand.

    See annotation.py for an example.
    """
