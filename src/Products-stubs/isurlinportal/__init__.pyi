from _typeshed import Incomplete

ALLOWED_SCHEMAS: Incomplete
BAD_URL_PARTS: Incomplete
allowed_ascii: Incomplete

def safe_url_first_char(url): ...
def get_external_sites(context=None): ...
def isURLInPortal(self, url, context=None):
    """Check if a given url is on the same host and contains the portal path.

    This is used to ensure that login forms can determine relevant
    referrers (i.e. in portal).  Also return true for some relative
    urls if context is passed in to allow for url parsing. When context
    is not provided, assume that relative urls are in the portal. It is
    assumed that http://portal is the same portal as https://portal.

    External sites listed in 'allow_external_login_sites' of
    site_properties are also considered within the portal to allow for
    single sign on.
    """
