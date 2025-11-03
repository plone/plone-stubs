from _typeshed import Incomplete
from Acquisition import Implicit
from OFS.owner import Owned
from OFS.role import RoleManager
from OFS.Traversable import Traversable
from persistent import Persistent
from Products.CMFCore.CMFCatalogAware import CatalogAware
from Products.CMFCore.CMFCatalogAware import WorkflowAware
from Products.CMFCore.DynamicType import DynamicType

COMMENT_TITLE: Incomplete
MAIL_NOTIFICATION_MESSAGE: Incomplete
MAIL_NOTIFICATION_MESSAGE_MODERATOR: Incomplete
logger: Incomplete

class Comment(
    CatalogAware,
    WorkflowAware,
    DynamicType,
    Traversable,
    RoleManager,
    Owned,
    Implicit,
    Persistent,
):
    """A comment.

    This object attempts to be as lightweight as possible. We implement a
    number of standard methods instead of subclassing, to have total control
    over what goes into the object.
    """

    security: Incomplete
    meta_type: str
    portal_type: str
    fti_title: str
    __parent__: Incomplete
    comment_id: Incomplete
    in_reply_to: Incomplete
    title: str
    mime_type: Incomplete
    text: str
    creator: Incomplete
    creation_date: Incomplete
    modification_date: Incomplete
    author_username: Incomplete
    author_name: Incomplete
    author_email: Incomplete
    user_notification: Incomplete
    __ac_local_roles__: Incomplete
    def __init__(self) -> None: ...
    def __getattribute__(self, attr): ...
    @property
    def id(self): ...
    def getId(self): ...
    def getText(self, targetMimetype=None):
        """The body text of a comment."""
    def Title(self): ...
    def Creator(self): ...
    def Type(self): ...
    def opaqueItems(self): ...
    def opaqueIds(self): ...
    def opaqueValues(self): ...

CommentFactory: Incomplete

def notify_workflow(obj, event) -> None:
    """Tell the workflow tool when a comment is added"""

def notify_content_object(obj, event) -> None:
    """Tell the content object when a comment is added"""

def notify_content_object_deleted(obj, event) -> None:
    """Remove all comments of a content object when the content object has been
    deleted.
    """

def notify_comment_added(obj, event):
    """Notify custom discussion events when a comment is added or replied"""

def notify_comment_modified(obj, event):
    """Notify custom discussion events when a comment, or a reply, is modified"""

def notify_comment_removed(obj, event):
    """Notify custom discussion events when a comment or reply is removed"""

def notify_content_object_moved(obj, event) -> None:
    """Update all comments of a content object that has been moved."""

def notify_user(obj, event) -> None:
    """Tell users when a comment has been added.

    This method composes and sends emails to all users that have added a
    comment to this conversation and enabled user notification.

    This requires the user_notification setting to be enabled in the
    discussion control panel.
    """

def notify_moderator(obj, event) -> None:
    """Tell the moderator when a comment needs attention.

    This method sends an email to the moderator if comment moderation a new
    comment has been added that needs to be approved.

    The moderator_notification setting has to be enabled in the discussion
    control panel.

    Configure the moderator e-mail address in the discussion control panel.
    If no moderator is configured but moderator notifications are turned on,
    the site admin email (from the mail control panel) will be used.
    """
