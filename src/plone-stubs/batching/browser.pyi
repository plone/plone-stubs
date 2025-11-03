from _typeshed import Incomplete
from Products.Five import BrowserView

BatchTemplate: Incomplete
BootstrapBatchTemplate: Incomplete

class BatchMacrosView(BrowserView):
    @property
    def macros(self): ...

class BatchView(BrowserView):
    """View class for browser navigation  (classic)"""

    index = BatchTemplate
    batch: Incomplete
    batchformkeys: Incomplete
    minimal_navigation: bool
    def __call__(self, batch, batchformkeys=None, minimal_navigation: bool = False): ...
    def make_link(self, pagenumber) -> None: ...

class BootstrapBatchView(BatchView):
    index = BootstrapBatchTemplate

class PloneBatchView(BatchView):
    def make_link(self, pagenumber=None, omit_params=["ajax_load"]): ...

class PloneBootstrapBatchView(BootstrapBatchView, PloneBatchView): ...
