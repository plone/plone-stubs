from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer

ISO_DATE_FORMAT: str

class IBrowserLayer(IDefaultBrowserLayer):
    """plone.app.event specific browser layer."""

class IICalendarImportEnabled(Interface):
    """Marker interface for contexts, where icalendar import is enabled."""
