from _typeshed import Incomplete

class BaseBatch:
    """A sequence batch splits up a large number of items over multiple pages"""

    size: int
    first: int
    start: int
    end: int
    numpages: int
    pagenumber: int
    pagerange: int
    orphan: int
    overlap: int
    b_start_str: str
    beyond: bool
    def __init__(
        self,
        sequence,
        size,
        start: int = 0,
        end: int = 0,
        orphan: int = 0,
        overlap: int = 0,
        pagerange: int = 7,
    ) -> None:
        """Encapsulate sequence in batches of size
        sequence  - the data to batch.
        size      - the number of items in each batch.
        start     - the first element of sequence to include in batch
                    (0-index)
        end       - the last element of sequence to include in batch
                    (0-index, optional)
        orphan    - the next page will be combined with the current page
                    if it does not contain more than orphan elements
        overlap   - the number of overlapping elements in each batch
        pagerange - the number of pages to display in the navigation
        """
    pagesize: Incomplete
    length: Incomplete
    last: Incomplete
    def initialize(self, start, end, size) -> None:
        """Calculate effective start, end, length and pagesize values"""
    @property
    def navlist(self):
        """Pagenumber list for creating batch links"""
    def getPagenumber(self): ...
    def setPagenumber(self, pagenumber) -> None:
        """Set pagenumber and update batch accordingly"""
    @classmethod
    def fromPagenumber(
        cls, items, pagesize: int = 20, pagenumber: int = 1, navlistsize: int = 5
    ):
        """Create new page from sequence and pagenumber"""
    @property
    def sequence_length(self):
        """Effective length of sequence"""
    def __len__(self) -> int:
        """Alias of `sequence_length`"""
    @property
    def next(self):
        """Next batch page"""
    @property
    def previous(self):
        """Previous batch page"""
    def __getitem__(self, index):
        """Get item from batch"""
    @property
    def firstpage(self):
        """First page of batch

        Always 1
        """
    @property
    def lastpage(self):
        """Last page of batch"""
    @property
    def islastpage(self):
        """True, if page is last page."""
    @property
    def items_on_page(self):
        """Alias for `length`"""
    @property
    def multiple_pages(self):
        """`True`, if batch has more than one page."""
    @property
    def previouspage(self):
        """Previous page"""
    @property
    def nextpage(self):
        """Next page"""
    @property
    def items_not_on_page(self):
        """Items of sequence outside of batch"""
    @property
    def next_item_count(self):
        """Number of elements in next batch"""
    @property
    def has_next(self):
        """Batch has next page"""
    @property
    def show_link_to_first(self):
        """First page is in navigation list"""
    @property
    def show_link_to_last(self):
        """Last page is in navigation list"""
    @property
    def before_last_page_not_in_navlist(self): ...
    @property
    def has_previous(self): ...
    @property
    def previous_pages(self): ...
    @property
    def next_pages(self): ...
    @property
    def second_page_not_in_navlist(self): ...

class QuantumBatch(BaseBatch):
    """A batch with quantum leaps for quicker navigation of large resultsets.

    (e.g. next 1 10 100 ... results )
    """

    quantumleap: bool
    leapback: Incomplete
    leapforward: Incomplete
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
    ) -> None:
        """
        quantumleap - 0 or 1 to indicate if bigger increments should be used
                      in the navigation list for big results.
        """
    def initialize(self, start, end, size) -> None: ...

Batch = BaseBatch
