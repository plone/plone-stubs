from AccessControl.users import UnrestrictedUser as BaseUnrestrictedUser
from collections.abc import Generator
from contextlib import contextmanager

class UnrestrictedUser(BaseUnrestrictedUser):
    """Unrestricted user that still has an id."""
    def getId(self):
        """Return the ID of the user."""

@contextmanager
def elevated_privileges(context) -> Generator[None]:
    """Temporarily elevate current user's privileges.

    See http://docs.plone.org/develop/plone/security/permissions.html
    for more documentation on this code.

    """
