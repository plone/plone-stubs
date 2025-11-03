from OFS.ObjectManager import BeforeDeleteException
from zope.interface import Interface

class ILinkIntegrityNotificationException(Interface):
    """An exception indicating a prevented link integrity breach."""

class LinkIntegrityNotificationException(BeforeDeleteException):
    """An exception indicating a prevented link integrity breach."""
