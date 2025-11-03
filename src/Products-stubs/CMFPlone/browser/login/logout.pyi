from Products.Five.browser import BrowserView
from zope.interface import Interface

class ILoggedOutView(Interface): ...

class LogoutView(BrowserView):
    def __call__(self) -> None: ...

class LoggedOutView(BrowserView):
    def __call__(self): ...
