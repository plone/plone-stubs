from _typeshed import Incomplete
from Products.Five.browser import BrowserView

class LanguageSelector(BrowserView):
    """Language selector.

    >>> ls = LanguageSelector(None, dict(), None, None)
    >>> ls
    <plone.app.i18n.locales.browser.selector.LanguageSelector object at ...>

    >>> ls.update()
    >>> ls.available()
    False
    >>> ls.languages()
    []
    >>> ls.showFlags()
    False

    >>> class Tool(object):
    ...     use_cookie_negotiation = False
    ...     supported_langs = ['de', 'en', 'ar']
    ...     always_show_selector = False
    ...
    ...     def __init__(self, **kw):
    ...         self.__dict__.update(kw)
    ...         self.showFlags = True
    ...
    ...     def getSupportedLanguages(self):
    ...         return self.supported_langs
    ...
    ...     def getAvailableLanguageInformation(self):
    ...         return dict(en={'selected' : True}, de={'selected' : False},
    ...                     nl={'selected' : True}, ar={'selected': True})
    ...
    ...     def getLanguageBindings(self, request):
    ...         # en = selected by user, nl = default, [] = other options
    ...         return ('en', 'nl', [])
    ...
    ...     def showSelector(self):
    ...         return bool(self.use_cookie_negotiation or self.always_show_selector)

    >>> ls.tool = Tool()
    >>> ls.available()
    False

    >>> ls.tool = Tool(use_cookie_negotiation=True)
    >>> ls.available()
    True

    >>> result = [{'code': 'en', 'selected': True}, {'code': 'ar', 'selected': False},
    ...           {'code': 'nl', 'selected': False}]
    >>> ls.languages() == result
    True

    >>> ls.showFlags()
    True

    >>> ls.tool = Tool(use_cookie_negotiation=True)
    >>> ls.available()
    True

    >>> ls.tool = Tool(always_show_selector=True)
    >>> ls.available()
    True

    >>> from zope.interface import implementer
    >>> from OFS.interfaces import IItem
    >>> @implementer(IItem)
    ... class Dummy(object):
    ...     def getPortalObject(self):
    ...         return self
    ...     def absolute_url(self):
    ...         return 'absolute url'

    >>> context = Dummy()
    >>> context.portal_url = Dummy()
    >>> ls = LanguageSelector(context, dict(), None, None)
    >>> ls.portal_url()
    'absolute url'
    """

    view: Incomplete
    manager: Incomplete
    def __init__(self, context, request, view, manager) -> None: ...
    tool: Incomplete
    def update(self) -> None: ...
    def available(self) -> bool: ...
    def portal_url(self): ...
    def languages(self):
        """Returns list of languages."""
    def showFlags(self):
        """Do we use flags?."""
