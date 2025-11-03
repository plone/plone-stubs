from zope.interface import Interface

class IRequest(Interface):
    """Base Request Interface

    ??? Add methods from BaseRequest?
    """

class IHTTPRequest(IRequest):
    """HTTP Request"""

class IBrowserRequest(IHTTPRequest):
    """Browser Request"""

class IWebDAVRequest(IHTTPRequest):
    """WebDAV Request"""

class IXMLRPCRequest(IHTTPRequest):
    """XML-RPC Request"""
