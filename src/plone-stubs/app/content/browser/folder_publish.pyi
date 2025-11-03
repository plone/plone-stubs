from zope.publisher.browser import BrowserView

class FolderPublishView(BrowserView):
    """Publish objects from a folder.

    Originally: Products/CMFPlone/skins/plone_scripts/folder_publish.cpy
    Called by content_status_history, in plone.app.content.
    """
    def __call__(
        self,
        workflow_action=None,
        paths=None,
        comment: str = "No comment",
        expiration_date=None,
        effective_date=None,
        include_children: bool = False,
    ): ...
    def transition_objects_by_paths(
        self,
        workflow_action,
        paths,
        comment: str = "",
        expiration_date=None,
        effective_date=None,
        include_children: bool = False,
        handle_errors: bool = True,
    ):
        """Originally this was in plone_utils.transitionObjectsByPaths.

        This was deprecated since 2015, so we copied it here.
        """
    def redirect(self) -> None: ...
