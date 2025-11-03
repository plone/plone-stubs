from _typeshed import Incomplete

__all__ = ["memoize", "memoize_contextless"]

class ViewMemo:
    key: str
    def memoize(self, func): ...
    def memoize_contextless(self, func): ...

memoize: Incomplete
memoize_contextless: Incomplete
