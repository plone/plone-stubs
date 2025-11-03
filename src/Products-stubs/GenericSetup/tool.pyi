from _typeshed import Incomplete
from OFS.Folder import Folder

IMPORT_STEPS_XML: str
EXPORT_STEPS_XML: str
TOOLSET_XML: str
DEPENDENCY_STRATEGY_UPGRADE: str
DEPENDENCY_STRATEGY_REAPPLY: str
DEPENDENCY_STRATEGY_NEW: str
DEPENDENCY_STRATEGY_IGNORE: str
DEFAULT_DEPENDENCY_STRATEGY = DEPENDENCY_STRATEGY_UPGRADE
UNKNOWN: str
generic_logger: Incomplete

def exportStepRegistries(context) -> None:
    """Built-in handler for exporting import / export step registries."""

def importToolset(context) -> None:
    """Import required / forbidden tools from XML file."""

def exportToolset(context) -> None:
    """Export required / forbidden tools to XML file."""

class SetupTool(Folder):
    """Profile-based site configuration manager."""

    meta_type: str
    zmi_icon: str
    zmi_show_add_dialog: bool
    security: Incomplete
    id: Incomplete
    def __init__(self, id) -> None: ...
    def getEncoding(self):
        """See ISetupTool."""
    def getBaselineContextID(self):
        """See ISetupTool."""
    def setBaselineContext(self, context_id, encoding=None) -> None:
        """See ISetupTool."""
    def getExcludeGlobalSteps(self):
        """See ISetupTool."""
    def setExcludeGlobalSteps(self, value) -> None:
        """See ISetupTool."""
    def applyContextById(self, context_id, encoding=None) -> None: ...
    def applyContext(self, context, encoding=None) -> None: ...
    def getImportStepRegistry(self):
        """See ISetupTool."""
    def getExportStepRegistry(self):
        """See ISetupTool."""
    def getImportStep(self, step, default=None):
        """Simple wrapper to query both the global and local step registry."""
    def getSortedImportSteps(self): ...
    def getImportStepMetadata(self, step, default=None):
        """Simple wrapper to query both the global and local step registry."""
    def getExportStep(self, step, default=None):
        """Simple wrapper to query both the global and local step registry."""
    def listExportSteps(self): ...
    def listImportSteps(self): ...
    def getExportStepMetadata(self, step, default=None):
        """Simple wrapper to query both the global and local step registry."""
    def getToolsetRegistry(self):
        """See ISetupTool."""
    def runImportStepFromProfile(
        self, profile_id, step_id, run_dependencies: bool = True, purge_old=None
    ):
        """See ISetupTool."""
    def runAllImportStepsFromProfile(
        self,
        profile_id,
        purge_old=None,
        ignore_dependencies: bool = False,
        archive=None,
        blacklisted_steps=None,
        dependency_strategy=None,
    ):
        """See ISetupTool."""
    def runExportStep(self, step_id):
        """See ISetupTool."""
    def runAllExportSteps(self):
        """See ISetupTool."""
    def createSnapshot(self, snapshot_id):
        """See ISetupTool."""
    def compareConfigurations(
        self,
        lhs_context,
        rhs_context,
        missing_as_empty: bool = False,
        ignore_blanks: bool = False,
        skip=...,
    ):
        """See ISetupTool."""
    def markupComparison(self, lines):
        """See ISetupTool."""
    manage_options: Incomplete
    manage_tool: Incomplete
    def manage_updateToolProperties(
        self, context_id, exclude_global_steps: bool = False, RESPONSE=None
    ) -> None:
        """Update the tool's settings."""
    manage_importSteps: Incomplete
    manage_fullImport: Incomplete
    manage_tarballImport: Incomplete
    def manage_importSelectedSteps(self, ids, run_dependencies, context_id=None):
        """Import the steps selected by the user."""
    def manage_importAllSteps(self, context_id=None, dependency_strategy=None):
        """Import all steps."""
    def manage_importExtensions(self, RESPONSE, profile_ids=()):
        """Import all steps for the selected extension profiles."""
    def manage_importTarball(self, tarball, submitted=None, purge_old=None):
        """Import steps from the uploaded tarball."""
    manage_exportSteps: Incomplete
    def manage_exportSelectedSteps(self, ids, RESPONSE):
        """Export the steps selected by the user."""
    def manage_exportAllSteps(self, RESPONSE):
        """Export all steps."""
    manage_upgrades: Incomplete
    upgradeStepMacro: Incomplete
    manage_snapshots: Incomplete
    def listSnapshotInfo(self):
        """Return a list of mappings describing available snapshots.

        o Keys include:

          'id' -- snapshot ID

          'title' -- snapshot title or ID

          'url' -- URL of the snapshot folder
        """
    def listProfileInfo(self, for_=None):
        """Return a list of mappings describing registered profiles.
        Base profile is listed first, extensions are sorted.

        o Keys include:

          'id' -- profile ID

          'title' -- profile title or ID

          'description' -- description of the profile

          'path' -- path to the profile within its product

          'product' -- name of the registering product
        """
    def listContextInfos(self, order_by: str = "sortable_title"):
        """List registered profiles and snapshots."""
    def getProfileImportDate(self, profile_id):
        """See ISetupTool."""
    def manage_createSnapshot(self, RESPONSE, snapshot_id=None):
        """Create a snapshot with the given ID.

        o If no ID is passed, generate one.
        """
    manage_showDiff: Incomplete
    def manage_downloadDiff(self, lhs, rhs, missing_as_empty, ignore_blanks, RESPONSE):
        """Crack request vars and call compareConfigurations.

        o Return the result as a 'text/plain' stream, suitable for framing.
        """
    def manage_compareConfigurations(self, lhs, rhs, missing_as_empty, ignore_blanks):
        """Crack request vars and call compareConfigurations."""
    manage_stepRegistry: Incomplete
    def manage_deleteImportSteps(self, ids, request=None) -> None:
        """Delete selected import steps."""
    def manage_deleteExportSteps(self, ids, request=None) -> None:
        """Delete selected export steps."""
    def getLastVersionForProfile(self, profile_id):
        """Return the last upgraded version for the specified profile."""
    def setLastVersionForProfile(self, profile_id, version) -> None:
        """Set the last upgraded version for the specified profile."""
    def unsetLastVersionForProfile(self, profile_id) -> None:
        """Unset the last upgraded version for the specified profile."""
    def getVersionForProfile(self, profile_id):
        """Return the registered filesystem version for the specified
        profile.
        """
    def purgeProfileVersions(self) -> None:
        """Purge the profile upgrade versions."""
    def profileExists(self, profile_id):
        """Check if a profile exists."""
    def profilesExist(self, profile_ids):
        """Check if all profiles exist."""
    def getProfileInfo(self, profile_id): ...
    def getDependenciesForProfile(self, profile_id, ignore_broken: bool = False):
        """
        If ignore_broken is True, return all referenced dependencies.
        Otherwise fail, if referenced dependency does not exist.
        """
    def getBrokenDependencies(self, profile_id):
        """Return referenced dependency-ids, which do not exist."""
    def hasBrokenDependencies(self, profile_id): ...
    def listProfilesWithUpgrades(self): ...
    def listUpgrades(
        self, profile_id, show_old: bool = False, dest=None, simple: bool = False
    ):
        """Get the list of available upgrades for a profile.

        With 'show_old=True', we show all upgrades, also ones that have been
        applied already.  Otherwise we take the last installed profile version
        as minimum source.

        When 'dest' is given, this is the maximum destination.  We do not
        report steps that upgrade to a higher destination.  We report steps
        that go in the right direction, even if there is no step that brings
        you to this exact version.

        By default we return a list of dictionaries, and sub lists of
        dictionaries. Each dictionary has information on one upgrade step.
        When simple=True we instead return a flat list with only upgrade steps.
        """
    def hasUpgrades(self, profile_id):
        """Does the profile have upgrade steps?"""
    def hasPendingUpgrades(self, profile_id=None):
        """Are upgrade steps pending?

        Pending means: a not yet applied upgrade step for an already
        applied profile.

        With a profile_id, we only check the given profile.

        Without a profile_id, we check if there is any profile at all
        that has an upgrade available.
        """
    def listProfilesWithPendingUpgrades(self):
        """List profile ids with pending upgrade steps.

        Pending means: a not yet applied upgrade step for an already
        applied profile.
        """
    def listUptodateProfiles(self):
        """List profile ids without pending upgrade steps.

        Pending means: a not yet applied upgrade step for an already
        applied profile.

        We ignore profiles that have no upgrade steps at all.
        """
    def manage_doUpgrades(self, request=None) -> None:
        """Perform all selected upgrade steps."""
    def upgradeProfile(self, profile_id, dest=None, quiet: bool = False) -> None:
        """Upgrade a profile.

        Apply all upgrade steps.

        When 'dest' is given, only update to that version.  If the
        version is not found, give a warning and do nothing.

        When 'quiet' is True, we do not complain when we cannot do anything.

        If the profile was not applied previously (last version for
        profile is unknown) we do nothing.
        """
    def getProfileDependencyChain(self, profile_id, seen=None): ...

addSetupToolForm: Incomplete

def addSetupTool(dispatcher, RESPONSE) -> None:
    """ """
