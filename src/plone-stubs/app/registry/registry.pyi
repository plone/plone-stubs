from _typeshed import Incomplete
from OFS.SimpleItem import SimpleItem
from plone.registry import registry

class Registry(registry.Registry, SimpleItem):
    """A Zope 2 style registry"""

    id: Incomplete
    title: Incomplete
    def __init__(self, id, title=None) -> None: ...
