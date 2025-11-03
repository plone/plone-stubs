from _typeshed import Incomplete
from collections.abc import Generator
from Products.Five.browser import BrowserView

class Checkout(BrowserView):
    index: Incomplete
    def containers(self) -> Generator[Incomplete]:
        """Get a list of potential containers"""
    def __call__(self): ...
