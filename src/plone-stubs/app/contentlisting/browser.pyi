from zope.publisher.browser import BrowserView

class FolderListing(BrowserView):
    def __call__(
        self,
        batch: bool = False,
        b_size: int = 20,
        b_start: int = 0,
        orphan: int = 0,
        **kw,
    ): ...

class ContentListingCollection(BrowserView):
    def __call__(
        self, batch: bool = False, b_size: int = 20, b_start: int = 0, **kw
    ): ...
