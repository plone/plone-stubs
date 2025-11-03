from _typeshed import Incomplete
from AccessControl.requestmethod import postonly
from OFS.SimpleItem import SimpleItem
from Products.CMFCore.utils import UniqueObject
from Products.CMFPlone.PloneBaseTool import PloneBaseTool

CEILING_DATE: Incomplete
FLOOR_DATE: Incomplete
BAD_CHARS: Incomplete
EMAIL_RE: Incomplete
EMAIL_CUTOFF_RE: Incomplete
METADATA_DCNAME: Incomplete
METADATA_DC_AUTHORFIELDS: Incomplete

class PloneTool(PloneBaseTool, UniqueObject, SimpleItem):
    """Various utility methods."""

    id: str
    meta_type: str
    toolicon: str
    security: Incomplete
    plone_tool: int
    field_prefix: str
    def setMemberProperties(self, member, REQUEST=None, **properties) -> None: ...
    @security.public
    def getSiteEncoding(self):
        """Get the the site encoding, which is utf-8."""
    @security.private
    def getMailHost(self):
        """Gets the MailHost."""
    @security.public
    def validateSingleNormalizedEmailAddress(self, address): ...
    @security.public
    def validateSingleEmailAddress(self, address): ...
    @security.public
    def validateEmailAddresses(self, addresses): ...
    @security.public
    def editMetadata(
        self,
        obj,
        allowDiscussion=None,
        title=None,
        subject=None,
        description=None,
        contributors=None,
        effective_date=None,
        expiration_date=None,
        format=None,
        language=None,
        rights=None,
        **kwargs,
    ): ...
    @security.public
    def contentEdit(self, obj, **kwargs) -> None: ...
    @security.public
    def availableMIMETypes(self): ...
    def getWorkflowChainFor(self, object): ...
    def getIconFor(self, category, id, default=..., context=None): ...
    def getReviewStateTitleFor(self, obj): ...
    def changeOwnershipOf(
        self, object, userid, recursive: int = 0, REQUEST=None
    ) -> None:
        """Changes the ownership of an object."""
    changeOwnershipOf: Incomplete
    @security.public
    def urlparse(self, url): ...
    @security.public
    def urlunparse(self, url_tuple): ...
    def exceptionString(self): ...
    def logException(self) -> None: ...
    @security.public
    def createSitemap(self, context, request=None): ...
    def typesToList(self): ...
    @security.public
    def createBreadCrumbs(self, context, request=None): ...
    @security.public
    def good_id(self, id): ...
    @security.public
    def bad_chars(self, id): ...
    @security.public
    def getInheritedLocalRoles(self, context): ...
    @security.public
    def isDefaultPage(self, obj, request=None): ...
    @security.public
    def getDefaultPage(self, obj, request=None): ...
    @security.public
    def addPortalMessage(self, message, type: str = "info", request=None) -> None: ...
    @security.public
    def showPortalMessages(self, request=None): ...
    @security.public
    def browserDefault(self, obj): ...
    @security.public
    def isStructuralFolder(self, obj):
        """Checks if a given object is a "structural folder".

        That is, a folderish item which does not explicitly implement
        INonStructuralFolder to declare that it doesn\'t wish to be treated
        as a folder by the navtree, the tab generation etc.
        """
    @security.public
    def acquireLocalRoles(self, obj, status: int = 1, REQUEST=None) -> None: ...
    acquireLocalRoles: Incomplete
    @security.public
    def isLocalRoleAcquired(self, obj): ...
    @security.public
    def getOwnerName(self, obj): ...
    @security.public
    def normalizeString(self, text): ...
    @security.public
    def listMetaTags(self, context): ...
    @security.public
    def getUserFriendlyTypes(self, typesList=None): ...
    @security.public
    def reindexOnReorder(self, parent) -> None: ...
    @security.public
    def getEmptyTitle(self, translated: bool = True): ...
    @security.public
    def pretty_title_or_id(self, obj, empty_value=...): ...
    @security.public
    def getMethodAliases(self, typeInfo): ...
    @security.public
    @postonly
    def deleteObjectsByPaths(self, paths, handle_errors: bool = True, REQUEST=None): ...
    @security.public
    def renameObjectsByPaths(
        self, paths, new_ids, new_titles, handle_errors: bool = True, REQUEST=None
    ): ...
    renameObjectsByPaths: Incomplete
