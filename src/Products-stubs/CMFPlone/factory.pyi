from _typeshed import Incomplete

PLONE52MARKER: bool
PLONE60MARKER: bool
PLONE61MARKER: bool
logger: Incomplete

class NonInstallable:
    def getNonInstallableProducts(self): ...
    def getNonInstallableProfiles(self): ...

def zmi_constructor(context):
    """This is a dummy constructor for the ZMI."""

def addPloneSite(
    context,
    site_id,
    title: str = "Plone site",
    description: str = "",
    profile_id=...,
    snapshot: bool = False,
    content_profile_id=None,
    extension_ids=(),
    setup_content=None,
    default_language: str = "en",
    portal_timezone: str = "UTC",
    distribution_name=None,
    **kwargs,
):
    """Add a PloneSite to the context."""
