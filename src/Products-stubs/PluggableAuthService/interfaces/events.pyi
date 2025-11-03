from _typeshed import Incomplete
from zope.interface import Interface

class IPASEvent(Interface):
    """An event related to a PAS principal."""

    principal: Incomplete

class IPrincipalAddedToGroupEvent(IPASEvent):
    """A principal has been added to a group."""

    group_id: Incomplete

class IPrincipalRemovedFromGroupEvent(IPASEvent):
    """A principal has been removed from a group."""

    group_id: Incomplete

class IPrincipalCreatedEvent(IPASEvent):
    """A new principal has been created."""

class IUserLoggedInEvent(IPASEvent):
    """A user logged in."""

class IUserLoggedOutEvent(IPASEvent):
    """A user logged out."""

class IPrincipalDeletedEvent(IPASEvent):
    """A user has been removed."""

class ICredentialsUpdatedEvent(IPASEvent):
    """A principal has changed her password.

    Sending this event will cause a PAS user folder to trigger its active
    credential update plugins.
    """

    password: Incomplete

class IPropertiesUpdatedEvent(IPASEvent):
    """A principals properties have been updated."""

    properties: Incomplete

class IGroupCreatedEvent(IPASEvent):
    """A group has been created."""

class IGroupDeletedEvent(IPASEvent):
    """A group has been removed."""
