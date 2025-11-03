from _typeshed import Incomplete
from plone.app.discussion.interfaces import _
from Products.Five.browser import BrowserView

PMF = _

class TranslationHelper(BrowserView):
    def translate(self, text: str = ""): ...
    def translate_comment_review_state(self, rs): ...

class View(BrowserView):
    """Show comment moderation view."""

    template: Incomplete
    workflowTool: Incomplete
    transitions: Incomplete
    def __init__(self, context, request) -> None: ...
    def __call__(self): ...
    def comments(self):
        """Return comments of defined review_state.

        review_state is string or list of strings.
        """
    def moderation_enabled(self):
        """Return true if a review workflow is enabled on 'Discussion Item'
        content type.

        A 'review workflow' is characterized by implementing a 'pending'
        workflow state.
        """
    @property
    def moderation_multiple_state_enabled(self):
        """Return true if a 'review multiple state workflow' is enabled on
        'Discussion Item' content type.

        A 'review multiple state workflow' is characterized by implementing
        a 'rejected' workflow state and a 'spam' workflow state.
        """
    def allowed_transitions(self, obj=None):
        """Return allowed workflow transitions for obj.

        Example: pending

        [{'id': 'mark_as_spam', 'url': 'http://localhost:8083/PloneRejected/testfolder/testpage/++conversation++default/1575415863542780/content_status_modify?workflow_action=mark_as_spam', 'icon': '', 'category': 'workflow', 'transition': <TransitionDefinition at /PloneRejected/portal_workflow/comment_review_workflow/transitions/mark_as_spam>, 'title': 'Spam', 'link_target': None, 'visible': True, 'available': True, 'allowed': True},
        {'id': 'publish',
            'url': 'http://localhost:8083/PloneRejected/testfolder/testpage/++conversation++default/1575415863542780/content_status_modify?workflow_action=publish',
            'icon': '',
            'category': 'workflow',
            'transition': <TransitionDefinition at /PloneRejected/portal_workflow/comment_review_workflow/transitions/publish>,
            'title': 'Approve',
            'link_target': None, 'visible': True, 'available': True, 'allowed': True},
        {'id': 'reject', 'url': 'http://localhost:8083/PloneRejected/testfolder/testpage/++conversation++default/1575415863542780/content_status_modify?workflow_action=reject', 'icon': '', 'category': 'workflow', 'transition': <TransitionDefinition at /PloneRejected/portal_workflow/comment_review_workflow/transitions/reject>, 'title': 'Reject', 'link_target': None, 'visible': True, 'available': True, 'allowed': True}]
        """
    def get_author_name(self, comment):
        """Format author name with suffix for anonymous users.

        Returns the author name with a suffix (Guest) appended for anonymous
        comments. The suffix is translated to the current user's language.
        """

class ModerateCommentsEnabled(BrowserView):
    def __call__(self):
        """Returns true if a 'review workflow' is enabled on 'Discussion Item'
        content type. A 'review workflow' is characterized by implementing
        a 'pending' workflow state.
        """

class DeleteComment(BrowserView):
    """Delete a comment from a conversation.

    This view is always called directly on the comment object:

      http://nohost/front-page/++conversation++default/1286289644723317/         @@moderate-delete-comment
    """
    def __call__(self): ...
    def can_delete(self, reply):
        """Returns true if current user has the 'Delete comments'
        permission.
        """

class DeleteOwnComment(DeleteComment):
    """Delete an own comment if it has no replies.

    Following conditions have to be true for a user to be able to delete his
    comments:
    * "Delete own comments" permission
    * no replies to the comment
    * Owner role directly assigned on the comment object
    """
    def could_delete(self, comment=None):
        """Returns true if the comment could be deleted if it had no replies."""
    def can_delete(self, comment=None): ...
    def __call__(self) -> None: ...

class CommentTransition(BrowserView):
    """Publish, reject, recall a comment or mark it as spam.

    This view is always called directly on the comment object:

        http://nohost/front-page/++conversation++default/1286289644723317/\\\n        @@transmit-comment
    """
    def __call__(self):
        """Call CommentTransition."""

class BulkActionsView(BrowserView):
    """Call bulk action: publish/approve, delete (, reject, recall, mark as spam).

    Each table row of the moderation view has a checkbox with the absolute
    path (without host and port) of the comment objects:

      <input type="checkbox"
             name="paths:list"
             value="/plone/front-page/++conversation++default/                       1286289644723317"
             id="cb_1286289644723317" />

    If checked, the comment path will occur in the \'paths\' variable of
    the request when the bulk actions view is called. The bulk action
    (delete, publish, etc.) will be applied to all comments that are
    included.

    The paths have to be \'traversable\':

      /plone/front-page/++conversation++default/1286289644723317

    """

    workflowTool: Incomplete
    def __init__(self, context, request) -> None: ...
    paths: Incomplete
    def __call__(self) -> None:
        """Call BulkActionsView."""
    def transmit(self, action=None) -> None:
        """Transmit all comments in the paths variable to requested review_state.

        Expects a list of absolute paths (without host and port):

        /Plone/startseite/++conversation++default/1286200010610352
        """
    def delete(self) -> None:
        """Delete all comments in the paths variable.

        Expects a list of absolute paths (without host and port):

        /Plone/startseite/++conversation++default/1286200010610352
        """
