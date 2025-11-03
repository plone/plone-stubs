from _typeshed import Incomplete

DEFAULT_BATCH_SIZE: int

class HypermediaBatch:
    request: Incomplete
    b_start: Incomplete
    b_size: Incomplete
    batch: Incomplete
    def __init__(self, request, results) -> None: ...
    def __iter__(self):
        """Iterate over items in current batch."""
    @property
    def items_total(self):
        """Return the number of total items in underlying sequence."""
    @property
    def canonical_url(self):
        """Return the canonical URL to the batched collection-like resource,
        preserving query string params, but stripping all batching related
        params from it.
        """
    @property
    def current_batch_url(self): ...
    @property
    def links(self):
        """Get a dictionary with batching links."""
