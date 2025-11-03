from _typeshed import Incomplete
from Products.PluggableAuthService.plugins.BasePlugin import BasePlugin

_: Incomplete
manage_addPasswordPolicyForm: Incomplete

def manage_addPasswordPolicyPlugin(
    self, id, title: str = "", RESPONSE=None, schema=None, **kw
):
    """
    Create an instance of a password validation plugin.
    """

class PasswordPolicyPlugin(BasePlugin):
    """Simple Password Policy to enforce a minimum password length."""

    meta_type: str
    security: Incomplete
    min_chars: int
    id: Incomplete
    title: Incomplete
    def __init__(self, id, title: str = "") -> None:
        """Create a default plone password policy"""
    @security.private
    def validateUserInfo(self, user, set_id, set_info):
        """See IValidationPlugin. Used to validate password property"""
