from _typeshed import Incomplete

class LanguageBinding:
    """Helper which holding language infos in request."""

    security: Incomplete
    __allow_access_to_unprotected_subobjects__: int
    DEFAULT_LANGUAGE: Incomplete
    LANGUAGE: Incomplete
    LANGUAGE_LIST: Incomplete
    def getLanguageBindings(self):
        """Returns the bound languages.

        (language, default_language, languages_list)
        """

def setLanguageBinding(request): ...
def onRequest(object, event):
    """Set Language headers in the request."""

class LanguageUtility:
    exclude_paths: Incomplete
    exclude_exts: Incomplete
    @property
    def settings(self): ...
    @property
    def use_combined_language_codes(self): ...
    @property
    def supported_langs(self): ...
    @property
    def showFlags(self): ...
    def getSupportedLanguages(self):
        """Returns a list of supported language codes."""
    def listSupportedLanguages(self):
        """Returns a list of supported language names."""
    def getAvailableLanguages(self):
        """Returns the dictionary of available languages."""
    def getCcTLDInformation(self): ...
    def listAvailableLanguages(self):
        """Returns sorted list of available languages (code, name)."""
    def listAvailableLanguageInformation(self):
        """Returns list of available languages."""
    def getAvailableLanguageInformation(self):
        """Returns the dictionary of available languages."""
    def getDefaultLanguage(self):
        """Returns the default language. D"""
    def setDefaultLanguage(self, langCode) -> None:
        """Sets the default language. D"""
    def getNameForLanguageCode(self, langCode):
        """Returns the name for a language code."""
    def getFlagForLanguageCode(self, langCode):
        """Returns the name of the flag for a language code."""
    def addSupportedLanguage(self, langCode) -> None:
        """Registers a language code as supported."""
    def removeSupportedLanguages(self, langCodes) -> None:
        """Unregisters language codes from supported."""
    def setLanguageCookie(self, lang=None, request=None, noredir=None):
        """Sets a cookie for overriding language negotiation."""
    def getLanguageCookie(self, request):
        """Gets the preferred cookie language."""
    def getPreferredLanguage(self, request=None):
        """Gets the preferred site language."""
    def getPathLanguage(self, request):
        """Checks if a language is part of the current path."""
    def getContentLanguage(self, request):
        """Checks the language of the current content if not folderish."""
    def getCcTLDLanguages(self, request): ...
    def getSubdomainLanguages(self, request): ...
    def getRequestLanguages(self, request):
        """Parses the request and return language list."""
    def getLanguageBindings(self, request):
        """Returns the bound languages.

        (language, default_language, languages_list)
        """
    def getAvailableCountries(self):
        """Returns the dictionary of available countries."""
    def listAvailableCountries(self):
        """Returns the sorted list of available countries (code, name)."""
    def getNameForCountryCode(self, countryCode):
        """Returns the name for a country code."""
    def isAnonymousUser(self): ...
    def showSelector(self):
        """Returns True if the selector viewlet should be shown."""

class PrefsForPTS:
    """A preference to hook into PTS."""

    languages: Incomplete
    pref: Incomplete
    def __init__(self, context) -> None: ...
    def getPreferredLanguages(self):
        """Returns the list of the bound languages."""
