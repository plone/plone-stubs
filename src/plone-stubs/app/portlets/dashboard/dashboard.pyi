from plone.memoize.instance import memoize
from Products.Five.browser import BrowserView
from zope.interface import Interface

class IDashboard(Interface):
    """the dashboard display columns of portlet to the loggedin user"""

class DashboardView(BrowserView):
    """Power the dashboard"""
    def __call__(self): ...
    @property
    def auth_token(self): ...
    @memoize
    def can_edit(self): ...
    @memoize
    def empty(self): ...
