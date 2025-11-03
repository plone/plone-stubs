from Products.Five import BrowserView

NAMESPACE: str

class ModelEditorView(BrowserView):
    """Editor view."""
    @property
    def escaped_model_source(self): ...
    def modelSource(self): ...
    @property
    def model_source(self): ...
    def authorized(self, context, request): ...
    def __call__(self):
        """View and eventually save the form."""
