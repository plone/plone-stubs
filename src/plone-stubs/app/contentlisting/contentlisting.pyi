class ContentListing:
    """An IContentListing implementation based on sequences of objects."""
    def __init__(self, sequence) -> None: ...
    def __getitem__(self, index):
        """`x.__getitem__(index)` <==> `x[index]`"""
    def __len__(self) -> int:
        """Length of the resultset is equal to the length of the underlying
        sequence.
        """
    @property
    def actual_result_count(self): ...
    def __iter__(self):
        """Let the sequence be iterable and whenever we look at an object, it
        should be a ContentListingObject.
        """
    def __contains__(self, item) -> bool:
        """`x.__contains__(item)` <==> `item in x`"""
    def __lt__(self, other):
        """`x.__lt__(other)` <==> `x < other`"""
    def __le__(self, other):
        """`x.__le__(other)` <==> `x <= other`"""
    def __eq__(self, other):
        """`x.__eq__(other)` <==> `x == other`"""
    def __hash__(self):
        """`x.__hash__()`"""
    def __ne__(self, other):
        """`x.__ne__(other)` <==> `x != other`"""
    def __gt__(self, other):
        """`x.__gt__(other)` <==> `x > other`"""
    def __ge__(self, other):
        """`x.__ge__(other)` <==> `x >= other`"""
    def __add__(self, other) -> None:
        """`x.__add__(other)` <==> `x + other`"""
    def __mul__(self, n) -> None:
        """`x.__mul__(n)` <==> `x * n`"""
    def __rmul__(self, n) -> None:
        """`x.__rmul__(n)` <==> `n * x`"""
    def __getslice__(self, i, j):
        """`x.__getslice__(i, j)` <==> `x[i:j]`
        Use of negative indices is not supported.
        No longer used in Python 3, but still part of
        zope.interface.interfaces.IReadSequence
        """

class BaseContentListingObject:
    """A baseclass for the different types of contentlistingobjects.

    To avoid duplication of the stuff that is not implementation-specific.
    """
    def __eq__(self, other):
        """For comparing two contentlistingobject"""
    def __hash__(self): ...
    def ContentTypeClass(self): ...
    def ReviewStateClass(self): ...
    def appendViewAction(self): ...
    def isVisibleInNav(self): ...
    def MimeTypeIcon(self): ...
