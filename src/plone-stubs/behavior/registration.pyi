from _typeshed import Incomplete

REGISTRATION_REPR: str

class BehaviorRegistration:
    title: Incomplete
    description: Incomplete
    interface: Incomplete
    marker: Incomplete
    factory: Incomplete
    name: Incomplete
    former_dotted_names: Incomplete
    def __init__(
        self,
        title,
        description,
        interface,
        marker,
        factory,
        name=None,
        former_dotted_names: str = "",
    ) -> None: ...

class BehaviorRegistrationNotFound(Exception):
    """Exception thrown if behavior registration lookup fails."""

def lookup_behavior_registration(
    name=None, identifier=None, warn_about_fallback: bool = True
):
    """Look up behavior registration either by name or interface identifier.
       Fall back to checking the former_dotted_names if the lookup is not
       successful.

    ``ValueError`` is thrown if function call is incomplete.
    ``BehaviorRegistrationNotFound`` is thrown if lookup fails.
    """
