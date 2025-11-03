from _typeshed import Incomplete

def normalize_version(version): ...

class UpgradeRegistry:
    """Registry of upgrade steps, by profile.

    Registry keys are profile ids.

    Each registry value is a nested mapping:
      - id -> step for single steps
      - id -> [ (id1, step1), (id2, step2) ] for nested steps
    """
    def __init__(self) -> None: ...
    def __getitem__(self, key): ...
    def keys(self): ...
    def clear(self) -> None: ...
    def getUpgradeStepsForProfile(self, profile_id):
        """Return the upgrade steps mapping for a given profile, or
        None if there are no steps registered for a profile matching
        that id.
        """
    def getUpgradeStep(self, profile_id, step_id):
        """Returns the specified upgrade step for the specified
        profile, or None if it doesn't exist.
        """

class UpgradeEntity:
    """
    Base class for actions to be taken during an upgrade process.
    """

    id: Incomplete
    title: Incomplete
    source: Incomplete
    dest: Incomplete
    description: Incomplete
    checker: Incomplete
    sortkey: Incomplete
    profile: Incomplete
    def __init__(
        self, title, profile, source, dest, desc, checker=None, sortkey: int = 0
    ) -> None: ...
    def versionMatch(self, source, dest=None): ...
    def isProposed(self, tool, source, dest=None):
        """Check if a step can be applied.

        False means already applied or does not apply.
        True means can be applied.
        """

class UpgradeStep(UpgradeEntity):
    """A step to upgrade a component."""

    handler: Incomplete
    def __init__(
        self,
        title,
        profile,
        source,
        dest,
        desc,
        handler,
        checker=None,
        sortkey: int = 0,
    ) -> None: ...
    def doStep(self, tool) -> None: ...

class UpgradeDepends(UpgradeEntity):
    """A specialized upgrade step that re-runs a particular import
    step from the profile.
    """

    import_profile: Incomplete
    import_steps: Incomplete
    run_deps: Incomplete
    purge: Incomplete
    def __init__(
        self,
        title,
        profile,
        source,
        dest,
        desc,
        import_profile=None,
        import_steps=[],
        run_deps: bool = False,
        purge: bool = False,
        checker=None,
        sortkey: int = 0,
    ) -> None: ...
    PROFILE_PREFIX: str
    def doStep(self, tool) -> None: ...

def listProfilesWithUpgrades(): ...
def listUpgradeSteps(tool, profile_id, source, dest=None, quick: bool = False):
    """Lists upgrade steps available from a given version, for a given
    profile id.

    If 'quick' is True, we return a simple boolean True when we have found the
    first matching upgrade step.  This is useful when you only want to know
    if there is at least one upgrade step.  This is used by
    tool.hasUpgradeSteps.
    """
