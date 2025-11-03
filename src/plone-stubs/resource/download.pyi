from zope.publisher.browser import BrowserView

class DownloadView(BrowserView):
    def __call__(self) -> None: ...
