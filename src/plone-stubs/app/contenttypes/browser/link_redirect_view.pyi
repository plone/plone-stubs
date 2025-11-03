from _typeshed import Incomplete
from Products.Five.browser import BrowserView

NON_REDIRECTABLE_URL_SCHEMES: Incomplete
NON_RESOLVABLE_URL_SCHEMES: Incomplete

def normalize_uid_from_path(url=None):
    """
    Args:
        url (string): a path or orl

    Returns:
        tuple: tuple of (uid, fragment) a fragment is an anchor id e.g. #head1
    """

class LinkRedirectView(BrowserView):
    index: Incomplete
    @property
    def can_edit(self): ...
    def __call__(self):
        """Redirect to the Link target URL, if and only if:
        - redirect_links property is enabled in
          configuration registry
        - the link is of a redirectable type (no mailto:, etc)
        - AND current user doesn't have permission to edit the Link"""
    def url(self):
        """Returns the url with link variables replaced."""
    def display_link(self):
        """Format the url for display"""
    def absolute_target_url(self):
        """Compute the absolute target URL."""
