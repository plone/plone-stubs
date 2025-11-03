from _typeshed import Incomplete
from AccessControl.requestmethod import postonly
from Products.CMFCore.RegistrationTool import RegistrationTool as BaseTool
from Products.CMFPlone.PloneBaseTool import PloneBaseTool
from zope.schema import ValidationError

invalid_password_chars: Incomplete

def getValidPasswordChars(): ...

password_chars: Incomplete

def get_member_by_login_name(context, login_name, raise_exceptions: bool = True):
    """Get a member by his login name.

    If a member with this login_name as userid exists, we happily
    return that member.

    If raise_exceptions is False, we silently return None.
    """

class RegistrationTool(PloneBaseTool, BaseTool):
    """Manage through-the-web signup policies."""

    meta_type: str
    security: Incomplete
    toolicon: str
    plone_tool: int
    md5key: Incomplete
    default_member_id_pattern: str
    def __init__(self) -> None: ...
    def getPassword(self, length: int = 5, s=None): ...
    def isValidEmail(self, email): ...
    def testPasswordValidity(self, password, confirm=None): ...
    def pasValidation(self, property, password): ...
    def testPropertiesValidity(self, props, member=None): ...
    def principal_id_or_login_name_exists(self, name): ...
    def isMemberIdAllowed(self, id): ...
    def generatePassword(self): ...
    def generateResetCode(self, salt, length: int = 14): ...
    def mailPassword(self, login, REQUEST, immediate: bool = False):
        """Wrapper around mailPassword"""
    def registeredNotify(self, new_member_id): ...
    @postonly
    def editMember(
        self,
        member_id,
        properties=None,
        password=None,
        roles=None,
        domains=None,
        REQUEST=None,
    ):
        """Edit a user's properties and security settings

        o Checks should be done before this method is called using
          testPropertiesValidity and testPasswordValidity
        """

class EmailAddressInvalid(ValidationError):
    __doc__: Incomplete

def checkEmailAddress(address) -> None:
    """Check email address.

    This should catch most invalid but no valid addresses.
    """
