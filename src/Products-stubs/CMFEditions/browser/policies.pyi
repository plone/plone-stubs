from Products.Five import BrowserView

class SaveAsNewVersion(BrowserView):
    """Save as new version

    Originally a Script (Python): saveasnewversion
    """
    def __call__(self) -> None: ...

class RevertVersion(BrowserView):
    """Revert version

    Originally a Script (Python): revertversion
    """
    def __call__(self): ...
