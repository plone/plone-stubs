from _typeshed import Incomplete

class TranslationManager:
    context: Incomplete
    tg: Incomplete
    pcatalog: Incomplete
    def __init__(self, context) -> None: ...
    def get_id(self, context):
        """If an object is created via portal factory we don't get a id, we
        have to wait till the object is really created.
        TODO: a better check if we are in the portal factory!
        """
    def get_tg(self, context):
        """If an object is created via portal factory we don't get a id, we
        have to wait till the object is really created.
        TODO: a better check if we are in the portal factory!
        """
    def query_canonical(self): ...
    def register_translation(self, language, content) -> None:
        """register a translation for an existing content"""
    def update(self) -> None:
        """Update the adapted item.

        If unregistered, register a Translation-Grouup (TG) for it and exit.

        Check that there aren't two translations on the same language
        This is to be used for changing the contexts language.
        If there is already an item in the same language,
        Remove the other items TG information and make the current adapted
        context the active language for the current TG.

        """
    def add_translation(self, language):
        """see interfaces"""
    def add_translation_delegated(self, language):
        """
        Creation is delegated to factory/++add++
        Lets return the url where we are going to create the translation
        """
    def remove_translation(self, language) -> None:
        """see interfaces"""
    def get_translation(self, language):
        """see interfaces"""
    def get_restricted_translation(self, language):
        """see interfaces"""
    def get_translations(self):
        """see interfaces"""
    def get_restricted_translations(self):
        """see interfaces"""
    def get_translated_languages(self):
        """see interfaces"""
    def has_translation(self, language):
        """see interfaces"""
