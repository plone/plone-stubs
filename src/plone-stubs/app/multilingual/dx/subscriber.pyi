from _typeshed import Incomplete

class LanguageIndependentModifier:
    """Class to handle dexterity editions."""

    canonical: Incomplete
    def __call__(self, content, event) -> None:
        """Called by the event system."""
    def bypass_security_checks(self): ...
    def handle_modified(self, content) -> None: ...
    def reindex_translation(self, translation) -> None:
        """Once the modification is done, reindex translation"""
    def get_all_translations(self, content):
        """Return all translations excluding the just modified content"""

handler: Incomplete
