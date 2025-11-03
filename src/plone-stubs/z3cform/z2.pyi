from zope import interface

class IFixedUpRequest(interface.Interface):
    """Marker interface used to ensure we don't fix up the request twice"""

class IProcessedRequest(interface.Interface):
    """Marker interface used to ensure we don't process the request inputs
    twice.
    """

def processInputs(request, charsets=None) -> None:
    """Process the values in request.form to decode strings to unicode, using
    the passed-in list of charsets. If none are passed in, look up the user's
    preferred charsets. The default is to use utf-8.
    """

def switch_on(view, request_layer=...) -> None:
    """Fix up the request and apply the given layer. This is mainly useful
    in Zope < 2.10 when using a wrapper layout view.
    """
