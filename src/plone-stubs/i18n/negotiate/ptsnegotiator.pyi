from _typeshed import Incomplete

def getAcceptedHelper(self, request, kind: str = "language"):
    """this is patched on prefs classes which don't define the getAccepted
    classes but define the deprecated getPreferredLanguages method"""

def registerLangPrefsMethod(prefs, kind: str = "language") -> None: ...
def getLangPrefs(env, kind: str = "language"):
    """get highest priority method for kind"""

def lang_normalize(lang):
    """filter"""

def str_lower(aString):
    """filter"""

def str_strip(aString):
    """filter"""

def type_accepted(available, preferred): ...
def lang_accepted(available, preferred): ...

class BrowserAccept:
    filters: Incomplete
    def __init__(self, request) -> None: ...
    def getAccepted(self, request, kind: str = "content-type"): ...

class CookieAccept:
    filters: Incomplete
    def __init__(self, request) -> None: ...
    def getAccepted(self, request, kind: str = "language"): ...

def setCookieLanguage(request, lang, REQUEST=None):
    """sets the language to a cookie

    request - the request object
    lang - language as string like de or pt_BR (it's normalizd)
    """

class Negotiator:
    tests: Incomplete
    def negotiate(self, choices, request, kind: str = "content-type"): ...
    def getLanguage(self, langs, request): ...
    def getLanguages(self, request): ...

negotiator: Incomplete

def negotiate(langs, request): ...

class PTSLanguages:
    """Languages adapter that chooses languages for the zope.i18n machinery.

    This used to be part of Products.Five.i18n.
    """

    context: Incomplete
    def __init__(self, context) -> None: ...
    def getPreferredLanguages(self): ...
