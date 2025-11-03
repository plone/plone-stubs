from plone.app.i18n.locales.browser.selector import LanguageSelector

def addQuery(request, url, exclude=..., **extras):
    """Adds the incoming GET query to the end of the url
    so that is propagated through the redirect hoops
    """

def get_root_request(request):
    """If in a subrequest, go up to the root request and return it"""

def getPostPath(context, request):
    """Finds the path to be added at the end of a context.

    This is useful because you might have a view or even something more long
    (form and widget traversing) at the very end of the absolute_url
    of a translated item.
    When you get the translated item absolute_url,
    you want to also have the eventual views etc ported over:
    this function does that.
    """

NOT_TRANSLATED_YET_TEMPLATE: str

class LanguageSelectorViewlet(LanguageSelector):
    """Language selector for translatable content."""
    def languages(self): ...
