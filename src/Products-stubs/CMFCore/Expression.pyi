from _typeshed import Incomplete
from Persistence import Persistent

class Expression(Persistent):
    text: str
    security: Incomplete
    def __init__(self, text) -> None: ...
    def __call__(self, econtext): ...

def getExprContext(context, object=None): ...
def createExprContext(folder, portal, object):
    """
    An expression context provides names for TALES expressions.
    """
