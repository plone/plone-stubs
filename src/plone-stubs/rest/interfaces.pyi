from Products.CMFCore.interfaces import (
    IShouldAllowAcquiredItemPublication as IShouldAllowAcquiredItemPublication,
)
from zope.interface import Interface

class IAPIRequest(Interface):
    """Marker for API requests."""

class IService(Interface):
    """Marker for REST services."""

class ICORSPolicy(Interface):
    """Provides methods for processing simple and preflight CORS requests by
    adding access control headers.
    """
    def process_simple_request() -> None:
        """Process a simple request"""
    def process_preflight_request() -> None:
        """Process a preflight request"""

class IShouldAllowAcquiredItemPublication(Interface): ...
