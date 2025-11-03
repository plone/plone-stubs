from zope.interface import Interface

class ILanguage(Interface):
    def get_language(self) -> None:
        """return the contents language"""
    def set_language(self) -> None:
        """return the contents language"""
