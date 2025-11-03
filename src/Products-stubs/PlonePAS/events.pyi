from Products.PluggableAuthService.events import PASEvent

class UserLoggedInEvent(PASEvent):
    """Plone Implementation of the logged in event

    PAS Event
    """

class UserInitialLoginInEvent(UserLoggedInEvent):
    """Implementation of the initial logged in event

    Plone only event!
    """

class UserLoggedOutEvent(PASEvent):
    """Plone Implementation of the logged out event

    PAS Event
    """
