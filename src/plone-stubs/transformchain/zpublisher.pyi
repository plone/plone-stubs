from _typeshed import Incomplete

CHARSET_RE: Incomplete

def extractEncoding(response):
    """Get the content encoding for the response body"""

def isEvilWebDAVRequest(request): ...
def applyTransform(request, body=None):
    """Apply any transforms by delegating to the ITransformer utility"""

def applyTransformOnSuccess(event):
    """Apply the transform after a successful request"""

def applyTransformOnFailure(event) -> None:
    """Apply the transform to the error html output"""

def setErrorStatusOnResponse(event) -> None: ...
