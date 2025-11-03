from Products.Five import BrowserView

class InlineValidationView(BrowserView):
    """Validate a form and return the error message for a particular field as JSON."""
    def __call__(self, fname=None, fset=None): ...
