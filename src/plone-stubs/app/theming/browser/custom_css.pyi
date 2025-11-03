from Products.Five.browser import BrowserView

class CustomCSSView(BrowserView):
    """
    Renders custom CSS stored in registry
    """
    def __call__(self): ...
