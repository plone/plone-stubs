from _typeshed import Incomplete
from Products.CMFCore.MembershipTool import MembershipTool as BaseTool

default_portrait: str
logger: Incomplete

class MembershipTool(BaseTool):
    """PAS-based customization of MembershipTool."""

    meta_type: str
    toolicon: str
    personal_id: str
    portrait_id: str
    default_portrait: str
    memberarea_type: str
    membersfolder_id: str
    memberareaCreationFlag: bool
    security: Incomplete
    user_search_keywords: Incomplete
    manage_options: Incomplete
    manage_mapRoles: Incomplete
    manage_portrait_fix: Incomplete
    def manage_setMemberAreaType(self, type_name, REQUEST=None) -> None:
        """ZMI method to set the home folder type by its type name."""
    def manage_setMembersFolderById(self, id, REQUEST=None) -> None:
        """ZMI method to set the members folder object by its id."""
    def setMemberAreaType(self, type_name) -> None:
        """Sets the portal type to use for new home folders."""
    def setMembersFolderById(self, id: str = "") -> None:
        """Set the members folder object by its id."""
    @security.public
    def getMembersFolder(self):
        """Get the members folder object."""
    @security.private
    def addMember(self, id, password, roles, domains, properties=None) -> None:
        """Adds a new member to the user folder.

        Security checks will have already been performed.  Called by
        portal_registration.  This one specific to PAS. PAS ignores
        domains. Adding members with login_name also not yet
        supported.
        """
    def searchForMembers(self, REQUEST=None, **kw):
        """Hacked up version of Plone searchForMembers.

        The following properties can be provided:
        - name
        - email
        - last_login_time
        - before_specified_time
        - roles (any role will cause a match)
        - groupname

        This is an \'AND\' request.

        Simple name searches are "fast".
        """
    @security.public
    def createMemberarea(self, member_id=None, minimal=None) -> None:
        """
        Create a member area for 'member_id' or the authenticated
        user, but don't assume that member_id is url-safe.
        """
    createMemberArea = createMemberarea
    @security.public
    def getMemberInfo(self, memberId=None): ...
    @security.public
    def getHomeFolder(self, id=None, verifyPermission: int = 0):
        """Return a member's home folder object, or None.

        Specially instrumented for URL-quoted-member-id folder
        names.
        """
    def getHomeUrl(self, id=None, verifyPermission: int = 0):
        """Return the URL to a member's home folder, or None."""
    @security.public
    def getPersonalFolder(self, member_id=None):
        """
        returns the Personal Item folder for a member
        if no Personal Folder exists will return None
        """
    @security.public
    def getPersonalPortrait(self, id=None, verifyPermission: int = 0):
        """Return a members personal portrait.

        Modified from CMFPlone version to URL-quote the member id.
        """
    def deletePersonalPortrait(self, id=None):
        """deletes the Portrait of a member."""
    def changeMemberPortrait(self, portrait, id=None) -> None:
        """update the portrait of a member.

        We URL-quote the member id if needed.

        Note that this method might be called by an anonymous user who
        is getting registered.  This method will then be called from
        plone.app.users and this is fine.  When called from restricted
        python code or with a curl command by a hacker, the
        declareProtected line will kick in and prevent use of this
        method.
        """
    def listMembers(self):
        """Gets the list of all members.
        THIS METHOD MIGHT BE VERY EXPENSIVE ON LARGE USER FOLDERS AND MUST
        BE USED WITH CARE! We plan to restrict its use in the future (ie.
        force large requests to use searchForMembers instead of listMembers,
        so that it will not be possible anymore to have a method returning
        several hundred of users :)
        """
    def listMemberIds(self):
        """Lists the ids of all members.  This may eventually be
        replaced with a set of methods for querying pieces of the
        list rather than the entire list at once.
        """
    def testCurrentPassword(self, password):
        """test to see if password is current"""
    def setPassword(self, password, domains=None, REQUEST=None) -> None:
        """Allows the authenticated member to set his/her own password."""
    setPassword: Incomplete
    def getCandidateLocalRoles(self, obj):
        """What local roles can I assign?
        Override the CMFCore version so that we can see the local roles on
        an object, and so that local managers can assign all roles locally.
        """
    def loginUser(self, REQUEST=None) -> None:
        """Handle a login for the current user.

        This method takes care of all the standard work that needs to be
        done when a user logs in:
        - clear the copy/cut/paste clipboard
        - PAS credentials update
        - sending a logged-in event
        - storing the login time
        - create the member area if it does not exist
        """
    def logoutUser(self, REQUEST=None) -> None:
        """Process a user logout.

        This takes care of all the standard logout work:
        - ask the user folder to logout
        - expire a skin selection cookie
        - invalidate a Zope session if there is one
        """
    def immediateLogout(self) -> None:
        """Log the current user out immediately.  Used by logout.py so that
        we do not have to do a redirect to show the logged out status."""
    @security.public
    def setLoginTimes(self):
        """Called by logged_in to set the login time properties
        even if members lack the "Set own properties" permission.

        The return value indicates if this is the first logged
        login time.
        """
    def getBadMembers(self):
        """Will search for members with bad images in the portal_memberdata
        delete their portraits and return their member ids"""
