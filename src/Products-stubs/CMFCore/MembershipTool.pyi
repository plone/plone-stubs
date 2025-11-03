from .utils import UniqueObject
from _typeshed import Incomplete
from AccessControl.requestmethod import postonly
from OFS.Folder import Folder

logger: Incomplete

class MembershipTool(UniqueObject, Folder):
    """This tool accesses member data through an acl_users object.

    It can be replaced with something that accesses member data in a
    different way.
    """

    id: str
    meta_type: str
    zmi_icon: str
    memberareaCreationFlag: int
    security: Incomplete
    manage_options: Incomplete
    manage_overview: Incomplete
    manage_mapRoles: Incomplete
    @postonly
    def setPassword(self, password, domains=None, REQUEST=None) -> None:
        """Allows the authenticated member to set his/her own password."""
    @security.public
    def getAuthenticatedMember(self):
        """
        Returns the currently authenticated member object
        or the Anonymous User.  Never returns None.
        """
    @security.private
    def wrapUser(self, u, wrap_anon: int = 0):
        """Set up the correct acquisition wrappers for a user object.

        Provides an opportunity for a portal_memberdata tool to retrieve and
        store member data independently of the user object.
        """
    def getPortalRoles(self):
        """
        Return all local roles defined by the portal itself,
        which means roles that are useful and understood
        by the portal object
        """
    role_map: Incomplete
    @postonly
    def setRoleMapping(self, portal_role, userfolder_role, REQUEST=None):
        """
        set the mapping of roles between roles understood by
        the portal and roles coming from outside user sources
        """
    def getMappedRole(self, portal_role):
        """
        returns a role name if the portal role is mapped to
        something else or an empty string if it is not
        """
    @security.public
    def getMembersFolder(self):
        """Get the members folder object."""
    def getMemberareaCreationFlag(self):
        """
        Returns the flag indicating whether the membership tool
        will create a member area if an authenticated user from
        an underlying user folder logs in first without going
        through the join process
        """
    def setMemberareaCreationFlag(self):
        """
        sets the flag indicating whether the membership tool
        will create a member area if an authenticated user from
        an underlying user folder logs in first without going
        through the join process
        """
    @security.public
    def createMemberArea(self, member_id: str = ""):
        """Create a member area for 'member_id' or authenticated user."""
    createMemberarea = createMemberArea
    @postonly
    def deleteMemberArea(self, member_id, REQUEST=None):
        """Delete member area of member specified by member_id."""
    @security.public
    def isAnonymousUser(self):
        """
        Returns 1 if the user is not logged in.
        """
    @security.public
    def checkPermission(self, permissionName, object, subobjectName=None):
        """
        Checks whether the current user has the given permission on
        the given object or subobject.
        """
    def isMemberAccessAllowed(self, member_id):
        """Check if the authenticated user is this member or an user manager."""
    @security.public
    def credentialsChanged(self, password, REQUEST=None) -> None:
        """
        Notifies the authentication mechanism that this user has changed
        passwords.  This can be used to update the authentication cookie.
        Note that this call should *not* cause any change at all to user
        databases.
        """
    def getMemberById(self, id):
        """
        Returns the given member.
        """
    def listMemberIds(self):
        """Lists the ids of all members.  This may eventually be
        replaced with a set of methods for querying pieces of the
        list rather than the entire list at once.
        """
    def listMembers(self):
        """Gets the list of all members."""
    def searchMembers(self, search_param, search_term):
        """Search the membership"""
    def getCandidateLocalRoles(self, obj):
        """What local roles can I assign?"""
    @postonly
    def setLocalRoles(
        self, obj, member_ids, member_role, reindex: int = 1, REQUEST=None
    ) -> None:
        """Add local roles on an item."""
    @postonly
    def deleteLocalRoles(
        self, obj, member_ids, reindex: int = 1, recursive: int = 0, REQUEST=None
    ) -> None:
        """Delete local roles of specified members."""
    @security.private
    def addMember(self, id, password, roles, domains, properties=None) -> None:
        """Adds a new member to the user folder.  Security checks will have
        already been performed.  Called by portal_registration.
        """
    @postonly
    def deleteMembers(
        self,
        member_ids,
        delete_memberareas: int = 1,
        delete_localroles: int = 1,
        REQUEST=None,
    ):
        """Delete members specified by member_ids."""
    @security.public
    def getHomeFolder(self, id=None, verifyPermission: int = 0) -> None:
        """Returns a member's home folder object or None.
        Set verifyPermission to 1 to return None when the user
        doesn't have the View permission on the folder.
        """
    @security.public
    def getHomeUrl(self, id=None, verifyPermission: int = 0) -> None:
        """Returns the URL to a member's home folder or None.
        Set verifyPermission to 1 to return None when the user
        doesn't have the View permission on the folder.
        """

class HomeFolderFactoryBase:
    """Creates a home folder."""

    title: Incomplete
    description: Incomplete
    def __call__(self, id, title=None, *args, **kw): ...
    def getInterfaces(self): ...

class _BBBHomeFolderFactory(HomeFolderFactoryBase):
    """Creates a home folder."""

    description: Incomplete
    def __call__(self, id, title=None, *args, **kw): ...

BBBHomeFolderFactory: Incomplete
