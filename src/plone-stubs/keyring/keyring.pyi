from _typeshed import Incomplete
from persistent.list import PersistentList

def GenerateSecret(length: int = 64): ...

class Keyring(PersistentList):
    __parent__: Incomplete
    last_rotation: int
    def __init__(self, size: int = 5) -> None: ...
    def __iter__(self): ...
    def clear(self) -> None: ...
    def rotate(self) -> None: ...
    def fill(self) -> None:
        """
        add missing keys
        """
    @property
    def current(self): ...
    def random(self):
        """
        since we could be on a rotation boundary,
        only rotate one less than the total
        """
