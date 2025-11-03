from plone.app.robotframework.remote import RemoteLibrary

class I18N(RemoteLibrary):
    def set_default_language(self, language=None) -> None:
        """Change portal default language"""
    def translate(self, msgid, *args, **kwargs):
        """Return localized string for given msgid"""
