from Products.Five.browser import BrowserView

class UserActionsView(BrowserView):
    """Power the useraction fallback page"""
    def user_actions(self): ...
