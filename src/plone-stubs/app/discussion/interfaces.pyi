from _typeshed import Incomplete
from zope.interface import Interface
from zope.interface.common.mapping import IIterableMapping
from zope.interface.interfaces import IObjectEvent

DISCUSSION_ANNOTATION_KEY: str

def isEmail(value): ...

class IConversation(IIterableMapping):
    """A conversation about a content object.

    This is a persistent object in its own right and manages all comments.

    The dict interface allows access to all comments. They are stored by
    long integer key, in the order they were added.

    Note that __setitem__() is not supported - use addComment() instead.
    However, comments can be deleted using __delitem__().

    To get replies at the top level, adapt the conversation to IReplies.

    The conversation can be traversed to via the ++comments++ namespace.
    For example, path/to/object/++comments++/123 retrieves comment 123.

    The __parent__ of the conversation (and the acquisition parent during
    traversal) is the content object. The conversation is the __parent__
    (and acquisition parent) for all comments, regardless of threading.
    """

    total_comments: Incomplete
    last_comment_date: Incomplete
    commentators: Incomplete
    public_commentators: Incomplete
    def addComment(comment) -> None:
        """Adds a new comment to the list of comments, and returns the
        comment id that was assigned. The comment_id property on the comment
        will be set accordingly.
        """
    def __delitem__(key) -> None:
        """Delete the comment with the given key. The key is a long id."""
    def getComments(start: int = 0, size=None) -> None:
        """Return an iterator of comment objects for rendering.

        The 'start' parameter is the id of the comment from which to start the
        batch. If no such comment exists, the next higher id will be used.
        This means that you can use max key from a previous batch + 1 safely.

        The 'size' parameter is the number of comments to return in the
        batch.

        The comments are returned in creation date order, in the exact batch
        size specified.
        """
    def getThreads(start: int = 0, size=None, root: int = 0, depth=None) -> None:
        """Return a batch of comment objects for rendering.

        The 'start' parameter is the id of the comment from which to start
        the batch. If no such comment exists, the next higher id will be used.
        This means that you can use max key from a previous batch + 1 safely.
        This should be a root level comment.

        The 'size' parameter is the number of threads to return in the
        batch. Full threads are always returned (although you can stop
        consuming the iterator if you want to abort).

        'root', if given, is the id of the comment to which reply
        threads will be found. 'root' itself is not included. If not given,
        all threads are returned.

        If 'depth' is given, it can be used to limit the depth of threads
        returned. For example, depth=1 will return only direct replies.

        Comments are returned as an iterator of dicts with keys 'comment',
        the comment, 'id', the comment id, and 'depth', which is 0 for
        top-level comments, 1 for their replies, and so on. The list is
        returned in depth-first order.
        """

class IReplies(IIterableMapping):
    """A set of related comments in reply to a given content object or
    another comment.

    Adapt a conversation or another comment to this interface to obtain the
    direct replies.
    """
    def addComment(comment) -> None:
        """Adds a new comment as a child of this comment, and returns the
        comment id that was assigned. The comment_id property on the comment
        will be set accordingly.
        """
    def __delitem__(key) -> None:
        """Delete the comment with the given key. The key is a long id."""

class IComment(Interface):
    """A comment.

    Comments are indexed in the catalog and subject to workflow and security.
    """

    portal_type: Incomplete
    __parent__: Incomplete
    comment_id: Incomplete
    in_reply_to: Incomplete
    author_username: Incomplete
    author_name: Incomplete
    author_email: Incomplete
    title: Incomplete
    mime_type: Incomplete
    text: Incomplete
    user_notification: Incomplete
    creator: Incomplete
    creation_date: Incomplete
    modification_date: Incomplete

class ICaptcha(Interface):
    """Captcha/ReCaptcha text field to extend the existing comment form."""

    captcha: Incomplete

class IDiscussionSettings(Interface):
    """Global discussion settings. This describes records stored in the
    configuration registry and obtainable via plone.registry.
    """

    globally_enabled: Incomplete
    anonymous_comments: Incomplete
    anonymous_email_enabled: Incomplete
    moderation_enabled: Incomplete
    edit_comment_enabled: Incomplete
    delete_own_comment_enabled: Incomplete
    text_transform: Incomplete
    captcha: Incomplete
    show_commenter_image: Incomplete
    moderator_notification_enabled: Incomplete
    moderator_email: Incomplete
    user_notification_enabled: Incomplete

class IDiscussionLayer(Interface):
    """Request marker installed via browserlayer.xml."""

class ICommentingTool(Interface):
    """For backwards-compatibility.

    This can be removed once we no longer support upgrading from versions
    of Plone that had a portal_discussion tool.
    """

class IDiscussionEvent(IObjectEvent):
    """Discussion custom event"""

class ICommentAddedEvent(IDiscussionEvent):
    """Comment added"""

class ICommentModifiedEvent(IDiscussionEvent):
    """Comment modified"""

class ICommentRemovedEvent(IDiscussionEvent):
    """Comment removed"""

class IReplyAddedEvent(IDiscussionEvent):
    """Comment reply added"""

class IReplyModifiedEvent(IDiscussionEvent):
    """Comment reply modified"""

class IReplyRemovedEvent(IDiscussionEvent):
    """Comment reply removed"""

class ICommentPublishedEvent(IDiscussionEvent):
    """Notify user on comment publication"""

class ICommentDeletedEvent(IDiscussionEvent):
    """Notify user on comment delete"""

class ICommentTransitionEvent(IDiscussionEvent):
    """Notify user on comment transition / change of review_state."""
