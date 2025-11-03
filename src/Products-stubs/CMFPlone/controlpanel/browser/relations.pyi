from _typeshed import Incomplete
from Products.Five.browser import BrowserView

logger: Incomplete

class RelationsRebuildControlpanel(BrowserView):
    done: bool
    def __call__(
        self, rebuild: bool = False, flush_and_rebuild_intids: bool = False
    ): ...

class RelationsInspectControlpanel(BrowserView):
    relation: Incomplete
    inspect_backrelation: Incomplete
    relations: Incomplete
    def __call__(self, relation=None, inspect_backrelation: bool = False): ...
