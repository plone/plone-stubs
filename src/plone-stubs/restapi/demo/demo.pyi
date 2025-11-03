from Products.Five.browser import BrowserView

class InternalServerErrorView(BrowserView):
    def __call__(self) -> None: ...
