from plone.app.robotframework.remote import RemoteLibrary

class Users(RemoteLibrary):
    def create_user(self, *args, **kwargs) -> None:
        """Create user with given details and return its id"""
