from _typeshed import Incomplete

class BitArray:
    bytes: Incomplete
    nbits: int
    bitsleft: int
    tostring: Incomplete
    def __init__(self, buf=None) -> None: ...
    def __getitem__(self, i): ...
    def __setitem__(self, i, val) -> None: ...
    def __len__(self) -> int: ...
    def append(self, bit) -> None:
        """Append a 1 if bit is true or 1 if it is false."""

class RiceCode:
    bits: Incomplete
    len: int
    def __init__(self, m) -> None:
        """Constructor a RiceCode for m-bit values."""
    m: Incomplete
    lower: Incomplete
    mask: Incomplete
    def init(self, m) -> None: ...
    def append(self, val) -> None:
        """Append an item to the list."""
    def __len__(self) -> int: ...
    def tolist(self):
        """Return the items as a list."""
    def tostring(self):
        """Return a binary string containing the encoded data.

        The binary string may contain some extra zeros at the end.
        """

def encode(m, l): ...
def encode_deltas(l): ...
def decode_deltas(start, enc_deltas): ...
