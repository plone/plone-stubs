from plone.app.robotframework.remote import RemoteLibrary

class AutoLogin(RemoteLibrary):
    def enable_autologin_as(self, *args) -> None:
        """Add and configure DomainAuthHelper PAS-plugin to login
        all anonymous users from localhost as a special *Remote User* with
        one or more given roles. Examples of use::

            Enable autologin as  Manager
            Enable autologin as  Site Administrator
            Enable autologin as  Member  Contributor

        """
    def set_autologin_username(self, username) -> None:
        """Update autologin mapping with the given username"""
    def disable_autologin(self) -> None:
        """Clear DomainAuthHelper's map to effectively 'logout' user
        after 'autologin_as'. Example of use::

            Disable autologin

        """
