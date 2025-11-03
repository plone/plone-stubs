from _typeshed import Incomplete

RESOLVEUID_RE: Incomplete

def resolve_uid(path):
    """Resolves a resolveuid URL into a tuple of absolute URL and catalog brain.

    If the original path is not found (including external URLs),
    it will be returned unchanged and the brain will be None.
    """

def uid_to_url(path): ...
def get_portal_type_title(portal_type): ...
