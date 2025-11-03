def wl_lockmapping(self, killinvalids: int = 0, create: int = 0): ...
def pluggableauth__getCSRFToken(request):
    """
    let plone.protect do it's job
    """

def pluggableauth__checkCSRFToken(
    request, token: str = "csrf_token", raises: bool = True
) -> None:
    """
    let plone.protect do it's job
    """

def marmoset_patch(func, replacement) -> None: ...
def disable_zope_csrf_checks() -> None: ...
def enable_zope_csrf_checks() -> None: ...
