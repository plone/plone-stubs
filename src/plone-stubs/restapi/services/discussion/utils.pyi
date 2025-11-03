def edit_comment_allowed(): ...
def can_edit(comment):
    """Returns true if current user has the 'Edit comments'
    permission.
    """

def permission_exists(permission_id): ...
def can_view(context):
    """Returns true if current user has the 'View comments' permission."""

def can_review(comment):
    """Returns true if current user has the 'Review comments' permission."""

def can_reply(comment):
    """Returns true if current user has the 'Reply to item' permission."""

def can_delete(comment):
    """Returns true if current user has the 'Delete comments'
    permission.
    """

def delete_own_comment_allowed(): ...
def can_delete_own(comment):
    """Returns true if the current user could delete the comment if it had
    no replies. This is used to prepare hidden form buttons for JS.
    """
