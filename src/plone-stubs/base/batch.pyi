from _typeshed import Incomplete
from plone.batching.batch import QuantumBatch

class Batch(QuantumBatch):
    b_start_str: str
    def __init__(
        self,
        sequence,
        size,
        start: int = 0,
        end: int = 0,
        orphan: int = 0,
        overlap: int = 0,
        pagerange: int = 7,
        quantumleap: int = 0,
        b_start_str: str = "b_start",
    ) -> None: ...
    def __len__(self) -> int: ...
    def __bool__(self) -> bool: ...
    __nonzero__ = __bool__
    def initialize(self, start, end, size) -> None: ...
    def pageurl(self, formvariables, pagenumber: int = -1): ...
    def navurls(self, formvariables, navlist=None): ...
    def prevurls(self, formvariables): ...
    def nexturls(self, formvariables): ...
    prevlist: Incomplete
    nextlist: Incomplete
