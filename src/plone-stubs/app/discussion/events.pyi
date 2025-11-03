from _typeshed import Incomplete

class DiscussionEvent:
    """Custom event"""

    object: Incomplete
    comment: Incomplete
    def __init__(self, context, comment, **kwargs) -> None: ...

class CommentAddedEvent(DiscussionEvent):
    """Event to be triggered when a Comment is added"""

class CommentModifiedEvent(DiscussionEvent):
    """Event to be triggered when a Comment is modified"""

class CommentRemovedEvent(DiscussionEvent):
    """Event to be triggered when a Comment is removed"""

class ReplyAddedEvent(DiscussionEvent):
    """Event to be triggered when a Comment reply is added"""

class ReplyModifiedEvent(DiscussionEvent):
    """Event to be triggered when a Comment reply is modified"""

class ReplyRemovedEvent(DiscussionEvent):
    """Event to be triggered when a Comment reply is removed"""

class CommentDeletedEvent(DiscussionEvent):
    """Event to be triggered when a Comment is deleted"""

class CommentPublishedEvent(DiscussionEvent):
    """Event to be triggered when a Comment is publicated"""

class CommentTransitionEvent(DiscussionEvent):
    """Event to be triggered when a Comments review_state changed."""

def auto_approve_comments(obj, event) -> None:
    """Auto-approve comments for users with 'Review comments' permission."""
