from ..plugins.BasePlugin import BasePlugin
from _typeshed import Incomplete
from zope.interface import Interface

class IRequestTypeSnifferPlugin(Interface):
    """Marker interface."""

def registerSniffer(iface, func) -> None: ...

manage_addRequestTypeSnifferForm: Incomplete

def addRequestTypeSnifferPlugin(dispatcher, id, title=None, REQUEST=None) -> None:
    """Add a RequestTypeSnifferPlugin to a Pluggable Auth Service."""

class RequestTypeSniffer(BasePlugin):
    """PAS plugin for detecting a Request's type"""

    meta_type: str
    zmi_icon: str
    security: Incomplete
    title: Incomplete
    def __init__(self, id, title=None) -> None: ...
    @security.private
    def sniffRequestType(self, request): ...

def webdavSniffer(request): ...
def xmlrpcSniffer(request): ...
def browserSniffer(request): ...
