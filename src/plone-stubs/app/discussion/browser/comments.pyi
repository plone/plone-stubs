from _typeshed import Incomplete
from plone.app.layout.viewlets.common import ViewletBase
from plone.z3cform.fieldsets import extensible
from z3c.form import form

COMMENT_DESCRIPTION_PLAIN_TEXT: Incomplete
COMMENT_DESCRIPTION_MARKDOWN: Incomplete
COMMENT_DESCRIPTION_INTELLIGENT_TEXT: Incomplete
COMMENT_DESCRIPTION_MODERATION_ENABLED: Incomplete

class CommentForm(extensible.ExtensibleForm, form.Form):
    ignoreContext: bool
    id: Incomplete
    label: Incomplete
    fields: Incomplete
    enable_autofocus: bool
    def updateFields(self) -> None: ...
    def updateWidgets(self) -> None: ...
    def updateActions(self) -> None: ...
    def get_author(self, data): ...
    def create_comment(self, data): ...
    def handleComment(self, action) -> None: ...
    def handleCancel(self, action) -> None: ...

class CommentsViewlet(ViewletBase):
    form = CommentForm
    index: Incomplete
    def update(self) -> None: ...
    def can_reply(self):
        """Returns true if current user has the 'Reply to item' permission."""
    def can_manage(self):
        """We keep this method for <= 1.0b9 backward compatibility. Since we do
        not want any API changes in beta releases.
        """
    def can_review(self):
        """Returns true if current user has the 'Review comments' permission."""
    def can_delete_own(self, comment):
        """Returns true if the current user can delete the comment. Only
        comments without replies can be deleted.
        """
    def could_delete_own(self, comment):
        """Returns true if the current user could delete the comment if it had
        no replies. This is used to prepare hidden form buttons for JS.
        """
    def can_edit(self, reply):
        """Returns true if current user has the 'Edit comments'
        permission.
        """
    def can_delete(self, reply):
        """Returns true if current user has the 'Delete comments'
        permission.
        """
    def is_discussion_allowed(self): ...
    def comment_transform_message(self):
        """Returns the description that shows up above the comment text,
        dependent on the text_transform setting and the comment moderation
        workflow in the discussion control panel.
        """
    def has_replies(self, workflow_actions: bool = False):
        """Returns true if there are replies."""
    def get_replies(self, workflow_actions: bool = False):
        """Returns all replies to a content object.

        If workflow_actions is false, only published
        comments are returned.

        If workflow actions is true, comments are
        returned with workflow actions.
        """
    def get_commenter_home_url(self, username=None): ...
    def get_commenter_portrait(self, username=None): ...
    def anonymous_discussion_allowed(self): ...
    def edit_comment_allowed(self): ...
    def delete_own_comment_allowed(self): ...
    def show_commenter_image(self): ...
    def is_anonymous(self): ...
    def login_action(self): ...
    def format_time(self, time): ...
    def get_author_name(self, comment):
        """Format author name with suffix for anonymous users.

        Returns the author name with a suffix (Guest) appended for anonymous
        comments. The suffix is translated to the current user's language.
        """
