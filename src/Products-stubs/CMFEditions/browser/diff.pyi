from _typeshed import Incomplete
from Products.Five.browser import BrowserView

class DiffView(BrowserView):
    repo_tool: Incomplete
    def __init__(self, *args) -> None: ...
    def getVersion(self, version): ...
    def versionName(self, version):
        """
        Translate the version name. This is needed to allow translation when `version`
        is the string 'current'.
        """
    def versionTitle(self, version): ...
    changeset: Incomplete
    changes: Incomplete
    def __call__(self): ...
