from zope.interface import Interface

class IErrorRaisedEvent(Interface):
    """
    An event that contains an error
    """

class ErrorRaisedEvent(dict): ...
