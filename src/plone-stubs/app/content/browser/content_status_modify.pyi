from _typeshed import Incomplete
from Products.Five import BrowserView

class ContentStatusModifyView(BrowserView):
    """Handles the workflow transitions of objects.

    Former Controller Python Script "content_status_modify".

    [validators]
    validators = validate_content_status_modify

    [actions]
    action.failure=traverse_to:string:content_status_history
    action.success=redirect_to_action:string:view

    """

    plone_utils: Incomplete
    def __call__(
        self,
        workflow_action=None,
        comment: str = "",
        effective_date=None,
        expiration_date=None,
        **kwargs,
    ):
        """Do a workflow action.

        The status dropdown in the toolbar has links to for example:
        content_status_modify?workflow_action=reject&_authenticator=secret
        That is the main entry into this browser view.

        When you right-click the status menu and open in a new tab,
        you end up on the content_status_history page.
        This page contains a form which posts to this view.

        In the form you can select a workflow action.
        When you select "no change" the workflow_action parameter actually contains
        the current status.  This status is naturally not in the list of allowed transitions.
        So we should be lenient here, and not complain much.

        Also, when the view is called on a default page,
        the code below tries to do the same transition on the parent folder,
        by calling this view on the parent.  This may easily fail.
        This is yet another reason to be lenient.
        Otherwise you may see both a successful portal status message
        and one with an error.

        In the form you can also add a comment and set an effective and/or expiration date.
        """
    def editContent(self, obj, effective, expiry) -> None: ...
