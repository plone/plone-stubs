from _typeshed import Incomplete
from ExtensionClass import Base

class LazyPrevBatch(Base):
    def __of__(self, parent): ...

class LazyNextBatch(Base):
    def __of__(self, parent): ...

class LazySequenceLength(Base):
    def __of__(self, parent): ...

class Batch(Base):
    """Create a sequence batch"""

    __allow_access_to_unprotected_subobjects__: int
    previous: Incomplete
    next: Incomplete
    sequence_length: Incomplete
    size: Incomplete
    start: Incomplete
    end: Incomplete
    orphan: Incomplete
    overlap: Incomplete
    first: Incomplete
    length: Incomplete
    def __init__(
        self,
        sequence,
        size,
        start: int = 0,
        end: int = 0,
        orphan: int = 0,
        overlap: int = 0,
    ) -> None:
        """Encapsulate "sequence" in batches of "size".

        Arguments: "start" and "end" are 0-based indexes into the
        sequence.  If the next batch would contain no more than
        "orphan" elements, it is combined with the current batch.
        "overlap" is the number of elements shared by adjacent
        batches.  If "size" is not specified, it is computed from
        "start" and "end".  Failing that, it is 7.

        Attributes: Note that the "start" attribute, unlike the
        argument, is a 1-based index (I know, lame).  "first" is the
        0-based index.  "length" is the actual number of elements in
        the batch.

        "sequence_length" is the length of the original, unbatched, sequence
        """
    def __getitem__(self, index): ...
    def __len__(self) -> int: ...

def opt(start, end, size, orphan, sequence): ...
