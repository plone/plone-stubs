from zope.interface.interfaces import ObjectEvent

class SiteManagerCreatedEvent(ObjectEvent): ...
class ReorderedEvent(ObjectEvent): ...

def profileImportedEventHandler(event) -> None:
    """
    When a profile is imported with the keyword "latest", it needs to
    be reconfigured with the actual number.
    """

def removeBase(event) -> None:
    """Make Zope not to inject a <base> tag into the returned HTML
    https://dev.plone.org/ticket/13705
    """
