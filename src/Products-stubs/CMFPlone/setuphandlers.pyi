def addCacheHandlers(portal) -> None:
    """Add RAM and AcceleratedHTTP cache handlers"""

def purgeProfileVersions(portal) -> None:
    """
    Purge profile dependency versions.
    """

def setProfileVersion(portal) -> None:
    """
    Set profile version.
    """

def assignTitles(portal) -> None: ...
def dummy_import_step(context) -> None:
    """Dummy import step.

    The plone-final import step used to call importFinalSteps below.
    But plone-final was never guaranteed to be run as final step.  So
    more and more import steps were added to its dependencies to let it
    run later and later.  Not nice.

    With Products.GenericSetup 1.8.2, we can add a post_handler to a
    profile (and a pre_handler).  We now do that.  So the plone-final
    import step is no longer needed.  But others may depend on it, so we
    keep it for now.  This dummy import step handler is meant for
    that.
    """

def importFinalSteps(context) -> None:
    """Final Plone import steps.

    This was an import step, but is now registered as post_handler
    specifically for our main 'plone' (profiles/default) profile.
    """

def set_zsqlmethods_permissions(site) -> None:
    """The permission to use Products.ZSQLMethods only makes sense when
    ZSQLMethods is installed. In Zope 4 that is sometimes not the case.

    The following xml was taken from rolemap.xml:
    <permission name="Use Database Methods" acquire="True">
      <role name="Site Administrator"/>
    </permission>
    """

def updateWorkflowRoleMappings(context) -> None:
    """
    If an extension profile (such as the testfixture one) switches default,
    workflows, this import handler will make sure object security works
    properly.
    """

def first_weekday_setup(context) -> None:
    """Set the first day of the week based on the portal's locale."""

def timezone_setup(context) -> None:
    """Set the timezone from server locale"""
