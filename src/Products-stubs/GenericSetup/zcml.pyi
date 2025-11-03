from _typeshed import Incomplete
from zope.interface import Interface

class IRegisterProfileDirective(Interface):
    """Register profiles with the global registry."""

    name: Incomplete
    title: Incomplete
    description: Incomplete
    directory: Incomplete
    provides: Incomplete
    for_: Incomplete
    pre_handler: Incomplete
    post_handler: Incomplete

def registerProfile(
    _context,
    name: str = "default",
    title=None,
    description=None,
    directory=None,
    provides=...,
    for_=None,
    pre_handler=None,
    post_handler=None,
) -> None:
    """Add a new profile to the registry."""

class IExportStepDirective(Interface):
    name: Incomplete
    title: Incomplete
    description: Incomplete
    handler: Incomplete

def exportStep(context, name, handler, title=None, description=None) -> None: ...

class IImportStepDirective(Interface):
    """Register import steps with the global registry."""

    name: Incomplete
    title: Incomplete
    description: Incomplete
    handler: Incomplete

class IImportStepDependsDirective(Interface):
    name: Incomplete

class importStep:
    context: Incomplete
    discriminator: Incomplete
    name: Incomplete
    handler: Incomplete
    title: Incomplete
    description: Incomplete
    dependencies: Incomplete
    def __init__(self, context, name, title, description, handler) -> None:
        """Add a new import step to the registry."""
    def depends(self, context, name) -> None: ...
    def __call__(self) -> None: ...

class IUpgradeStepsDirective(Interface):
    """
    Define multiple upgrade steps without repeating all of the parameters
    """

    source: Incomplete
    destination: Incomplete
    sortkey: Incomplete
    profile: Incomplete

class IUpgradeStepsStepSubDirective(Interface):
    """
    Subdirective to IUpgradeStepsDirective
    """

    title: Incomplete
    description: Incomplete
    handler: Incomplete
    checker: Incomplete

class IUpgradeStepDirective(IUpgradeStepsDirective, IUpgradeStepsStepSubDirective):
    """
    Define a standalone upgrade step
    """

class IUpgradeDependsSubDirective(Interface):
    """
    Define a profile import step dependency of an upgrade process
    (i.e. a profile step that should be reimported when performing an
    upgrade due to a profile change.
    """

    title: Incomplete
    description: Incomplete
    import_profile: Incomplete
    import_steps: Incomplete
    run_deps: Incomplete
    purge: Incomplete

class IUpgradeDependsDirective(IUpgradeStepsDirective, IUpgradeDependsSubDirective):
    """
    Define a standalone upgrade profile import step dependency
    """

def upgradeStep(
    _context,
    title,
    profile,
    handler,
    description=None,
    source: str = "*",
    destination: str = "*",
    sortkey: int = 0,
    checker=None,
) -> None: ...
def upgradeDepends(
    _context,
    title,
    profile,
    description=None,
    import_profile=None,
    import_steps=[],
    source: str = "*",
    destination: str = "*",
    run_deps: bool = False,
    purge: bool = False,
    checker=None,
    sortkey: int = 0,
) -> None: ...

class upgradeSteps:
    """
    Allows nested upgrade steps.
    """

    profile: Incomplete
    source: Incomplete
    dest: Incomplete
    sortkey: Incomplete
    id: Incomplete
    def __init__(
        self,
        _context,
        profile,
        source: str = "*",
        destination: str = "*",
        sortkey: int = 0,
    ) -> None: ...
    def upgradeStep(
        self, _context, title, handler, description=None, checker=None
    ) -> None:
        """nested upgradeStep directive"""
    def upgradeDepends(
        self,
        _context,
        title,
        description=None,
        import_profile=None,
        import_steps=[],
        run_deps: bool = False,
        purge: bool = False,
        checker=None,
    ) -> None:
        """nested upgradeDepends directive"""
    def __call__(self): ...
