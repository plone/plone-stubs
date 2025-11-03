from _typeshed import Incomplete
from AccessControl.requestmethod import postonly
from Products.CMFCore.MemberDataTool import MemberAdapter as BaseMemberAdapter
from Products.CMFCore.MemberDataTool import MemberDataTool as BaseTool

class MemberDataTool(BaseTool):
    """PAS-specific implementation of memberdata tool."""

    meta_type: str
    security: Incomplete
    toolicon: str
    portraits: Incomplete
    def __init__(self) -> None: ...
    @security.private
    def pruneMemberDataContents(self) -> None:
        """
        Compare the user IDs stored in the member data
        tool with the list in the actual underlying acl_users
        and delete anything not in acl_users
        """
    def purgeMemberDataContents(self):
        """
        Delete ALL MemberData information. This is required for us as we change
        the MemberData class.
        """
    @security.private
    def updateMemberDataContents(self):
        """Update former MemberData objects to new MemberData objects"""
    @security.private
    def searchMemberDataContents(self, search_param, search_term):
        """
        Search members.
        This is the same as CMFCore except that it doesn't check term case.
        """
    @security.public
    def searchFulltextForMembers(self, s): ...
    def canAddMemberData(self): ...
    @postonly
    def deleteMemberData(self, member_id, REQUEST=None):
        """Delete member data of specified member."""

class MemberData(BaseMemberAdapter):
    security: Incomplete
    id: Incomplete
    def __init__(self, user, tool) -> None: ...
    def setMemberProperties(
        self, mapping, force_local: int = 0, force_empty: bool = False
    ):
        """PAS-specific method to set the properties of a
        member. Ignores 'force_local', which is not reliably present.
        """
    def getProperty(self, id, default=...):
        """PAS-specific method to fetch a user's properties. Looks
        through the ordered property sheets.
        """
    @security.public
    def hasProperty(self, propname):
        """Does the member have the given property?"""
    def getPassword(self) -> None:
        """Returns None. Present to avoid NotImplementedError."""
    def canDelete(self):
        """True iff user can be removed from the Plone UI."""
    def canPasswordSet(self):
        """True iff user can change password."""
    def passwordInClear(self):
        """True iff password can be retrieved in the clear (not hashed.)

        False for PAS. It provides no API for getting passwords,
        though it would be possible to add one in the future.
        """
    def canWriteProperty(self, prop_name):
        """True iff the member/group property named in 'prop_name'
        can be changed.
        """
    def canAddToGroup(self, group_id):
        """True iff member can be added to group."""
    def canRemoveFromGroup(self, group_id):
        """True iff member can be removed from group."""
    def canAssignRole(self, role_id):
        """True iff member can be assigned role. Role id is string."""
    @security.private
    def setSecurityProfile(self, password=None, roles=None, domains=None) -> None:
        """Set the user's basic security profile"""
    @security.public
    def has_permission(self, permission, object): ...
    @security.public
    def getGroups(self): ...
    @security.public
    def getUserId(self): ...
