from Products.Five.browser import BrowserView

class i18njs(BrowserView):
    def __call__(self, domain=None, language=None): ...
