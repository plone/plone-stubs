from _typeshed import Incomplete
from zope.interface import Interface

logger: Incomplete

class IStreamedResponse(Interface):
    """Marker applied when we intercepted a streaming response. This allows
    us to avoid applying the same rules twice, since the normal hook may also
    be executed for streaming responses (albeit on a seemingly empty body,
    and after the response has been sent).
    """

class Intercepted(Exception):
    """Exception raised in order to abort regular processing before the
    published resource (e.g. a view) is called, and render a specific response
    body and status provided by an intercepting caching operation instead.
    """

    responseBody: Incomplete
    status: Incomplete
    def __init__(self, status: int = 304, responseBody: str = "") -> None: ...

class InterceptorResponse:
    """View for the Intercepted exception, serving to return an empty
    response in the case of an intercepted response.
    """

    context: Incomplete
    request: Incomplete
    def __init__(self, context, request) -> None: ...
    def __call__(self): ...

def intercept(event) -> None:
    """Invoke the interceptResponse() method of a caching operation, if one
    can be found.

    To properly abort request processing, this will raise an exception. The
    actual response (typically an empty response) is then set via a view on
    the exception. We set and lock the response status to avoid defaulting to
    a 404 exception.
    """

class MutatorTransform:
    """Transformation using plone.transformchain.

    This is registered at order 12000, i.e. "late". A typical transform
    chain order may include:

    * lxml transforms (e.g. plone.app.blocks, collectivexdv) => 8000-8999
    * gzip => 10000
    * caching => 12000

    This transformer is uncommon in that it doesn\'t actually change the
    response body. Instead, we look up caching operations which can modify
    response headers and perform other caching functions.
    """

    order: int
    published: Incomplete
    request: Incomplete
    def __init__(self, published, request) -> None: ...
    def transformUnicode(self, result, encoding) -> None: ...
    def transformBytes(self, result, encoding) -> None: ...
    def transformIterable(self, result, encoding) -> None: ...
    def mutate(self) -> None: ...

def modifyStreamingResponse(event) -> None:
    """Invoke the modifyResponse() method of a caching operation, if one
    can be found, for a streaming response (one using response.write()).
    """
