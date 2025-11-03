from _typeshed import Incomplete
from Products.Five.browser import BrowserView

class Macros:
    macro_pages: Incomplete
    aliases: Incomplete
    def __getitem__(self, key): ...

class StandardMacros(BrowserView, Macros):
    macro_pages: Incomplete
