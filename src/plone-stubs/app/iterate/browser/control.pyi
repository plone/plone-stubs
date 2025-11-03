from plone.memoize.view import memoize
from Products.Five.browser import BrowserView

class Control(BrowserView):
    """Information about whether iterate can operate.

    This is a public view, referenced in action condition expressions.
    """
    def checkin_allowed(self):
        """Check if a checkin is allowed"""
    def checkout_allowed(self):
        """Check if a checkout is allowed."""
    @memoize
    def cancel_allowed(self):
        """Check to see if the user can cancel the checkout on the
        given working copy
        """
