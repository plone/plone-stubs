from _typeshed import Incomplete

class NextPrevious:
    """Facade with more pythonic interface"""

    context: Incomplete
    parent: Incomplete
    nextprev: Incomplete
    enabled: Incomplete
    def __init__(self, context) -> None: ...
    @property
    def next(self):
        """return info about the next item in the container"""
    @property
    def previous(self):
        """return info about the previous item in the container"""
