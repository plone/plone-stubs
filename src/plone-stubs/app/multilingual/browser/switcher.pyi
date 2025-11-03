from Products.Five import BrowserView

class LanguageSwitcher(BrowserView):
    def __call__(self) -> None:
        """Redirect to the preferred language top-level folder.

        If no folder for preferred language exists, redirect to default
        language.

        Copy from LinguaPlone
        """
