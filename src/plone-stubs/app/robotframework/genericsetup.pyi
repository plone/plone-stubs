from plone.app.robotframework.remote import RemoteLibrary

class GenericSetup(RemoteLibrary):
    def apply_profile(self, name) -> None:
        """Apply named profile"""
