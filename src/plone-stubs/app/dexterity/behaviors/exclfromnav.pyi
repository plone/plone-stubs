from _typeshed import Incomplete
from plone.supermodel import model
from zope.interface import Interface

class IExcludeFromNavigationDefault(Interface):
    def __call__() -> None:
        """boolean if item is by default excluded from navigation or not."""

def default_exclude_false(context):
    """provide a default adapter with the standard uses"""

def default_exclude_true(context):
    """provide a alternative adapter with opposite default as standard"""

def default_exclude(context): ...

class IExcludeFromNavigation(model.Schema):
    """Behavior interface to exclude items from navigation."""

    exclude_from_nav: Incomplete
