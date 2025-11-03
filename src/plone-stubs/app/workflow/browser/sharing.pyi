from _typeshed import Incomplete
from plone.memoize.instance import clearafter
from plone.memoize.instance import memoize
from Products.Five.browser import BrowserView

AUTH_GROUP: str
STICKY: Incomplete

def merge_search_results(results, key):
    """Merge member search results.

    Based on PlonePAS.browser.search.PASSearchView.merge.
    """

class SharingView(BrowserView):
    template: Incomplete
    macro_wrapper: Incomplete
    STICKY = STICKY
    def __call__(self):
        """Perform the update and redirect if necessary, or render the page"""
    def handle_form(self):
        """
        We split this out so we can reuse this for ajax.
        Will return a boolean if it was a post or not
        """
    @memoize
    def roles(self):
        """Get a list of roles that can be managed.

        Returns a list of dicts with keys:

            - id
            - title
        """
    @memoize
    def role_settings(self):
        """Get current settings for users and groups for which settings have been made.

        Returns a list of dicts with keys:

         - id
         - title
         - type (one of 'group' or 'user')
         - roles

        'roles' is a dict of settings, with keys of role ids as returned by
        roles(), and values True if the role is explicitly set, False
        if the role is explicitly disabled and None if the role is inherited.
        """
    def can_edit_inherit(self):
        """If this method returns True, user can change role role inheritance status
        If it is False, inherit checkbox is not displayed on form
        """
    def inherited(self, context=None):
        """Return True if local roles are inherited here."""
    @memoize
    def existing_role_settings(self):
        """Get current settings for users and groups that have already got
        at least one of the managed local roles.

        Returns a list of dicts as per role_settings()
        """
    def user_search_results(self):
        """Return search results for a query to add new users.

        Returns a list of dicts, as per role_settings().
        """
    def group_search_results(self):
        """Return search results for a query to add new groups.

        Returns a list of dicts, as per role_settings().
        """
    def update_inherit(self, status: bool = True, reindex: bool = True):
        """Enable or disable local role acquisition on the context.

        Returns True if changes were made, or False if the new settings
        are the same as the existing settings.
        """
    @clearafter
    def update_role_settings(self, new_settings, reindex: bool = True):
        """Update local role settings and reindex object security if necessary.

        new_settings is a list of dicts with keys id, for the user/group id;
        type, being either 'user' or 'group'; and roles, containing the list
        of role ids that are set.

        Returns True if changes were made, or False if the new settings
        are the same as the existing settings.
        """
    def updateSharingInfo(self, search_term: str = ""): ...
