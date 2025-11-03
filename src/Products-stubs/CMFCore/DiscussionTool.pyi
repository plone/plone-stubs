from .ActionProviderBase import ActionProviderBase
from .utils import UniqueObject
from _typeshed import Incomplete
from Acquisition import Implicit
from OFS.SimpleItem import SimpleItem

class OldDiscussable(Implicit):
    """
    Adapter for PortalContent to implement "old-style" discussions.
    """

    security: Incomplete
    content: Incomplete
    def __init__(self, content) -> None: ...
    def createReply(self, title, text, REQUEST, RESPONSE) -> None:
        """
        Create a reply in the proper place
        """
    def getReplyLocationAndID(self, REQUEST): ...
    def getReplyResults(self):
        """
        Return the ZCatalog results that represent this object's replies.

        Often, the actual objects are not needed.  This is less expensive
        than fetching the objects.
        """
    def getReplies(self):
        """
        Return a sequence of the DiscussionResponse objects which are
        associated with this Discussable
        """
    def quotedContents(self):
        """
        Return this object's contents in a form suitable for inclusion
        as a quote in a response.
        """

class DiscussionTool(UniqueObject, SimpleItem, ActionProviderBase):
    id: str
    meta_type: str
    zmi_icon: str
    security: Incomplete
    manage_options: Incomplete
    manage_overview: Incomplete
    @security.public
    def getDiscussionFor(self, content):
        """Gets the PortalDiscussion object that applies to content."""
    @security.public
    def isDiscussionAllowedFor(self, content):
        """
        Returns a boolean indicating whether a discussion is
        allowed for the specified content.
        """
