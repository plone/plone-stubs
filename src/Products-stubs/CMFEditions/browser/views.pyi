from _typeshed import Incomplete
from Products.Five import BrowserView

class UpdateVersionOnEditView(BrowserView):
    def success(self) -> None: ...
    def __call__(self): ...

class UpdateVersionBeforeEditView(BrowserView):
    def success(self): ...
    def __call__(self): ...

class FileDownloadVersionView(BrowserView):
    def __call__(self): ...

class VersionImageTagView(BrowserView):
    def __call__(self): ...

class VersionsHistoryForm(BrowserView):
    def checkUpToDate(self, history):
        """Check if Up To Date.

        This used to be a Script (Python): checkUpToDate
        """
    def can_diff(self):
        """Return True if content is diffable"""

css_path: Incomplete
COMPARE_CSS: Incomplete

class CompareCSS(BrowserView):
    """Formerly skins/CMFEditions/compare.css.dtml

    Should be a browser resource, but I don't want to change plone.app.iterate just now.
    That will further complicate an already complex PR.
    """
    def __call__(self): ...
