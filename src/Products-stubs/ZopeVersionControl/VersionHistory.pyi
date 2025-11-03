from _typeshed import Incomplete
from Acquisition import Implicit
from Persistence import Persistent

MAX32: Incomplete

class VersionHistory(Implicit, Persistent):
    """A version history maintains the information about the changes
    to a particular version-controlled resource over time."""

    id: Incomplete
    def __init__(self, history_id, object) -> None: ...
    security: Incomplete
    @security.public
    def getId(self): ...
    @security.private
    def addLogEntry(self, version_id, action, path=None, message: str = "") -> None:
        """Add a new log entry associated with this version history."""
    @security.private
    def getLogEntries(self):
        """Return a sequence of the log entries for this version history."""
    @security.private
    def getLabels(self): ...
    @security.private
    def labelVersion(self, version_id, label, force: int = 0) -> None:
        """Associate a particular version in a version history with the
        given label, removing any existing association with that label
        if force is true, or raising an error if force is false and
        an association with the given label already exists."""
    @security.private
    def createBranch(self, branch_id, version_id):
        """Create a new branch associated with the given branch_id. The
        new branch is rooted at the version named by version_id."""
    @security.private
    def createVersion(self, object, branch_id):
        """Create a new version in the line of descent named by the given
        branch_id, returning the newly created version object."""
    @security.private
    def hasVersionId(self, version_id):
        """Return true if history contains a version with the given id."""
    @security.private
    def isLatestVersion(self, version_id, branch_id):
        """Return true if version id is the latest in its branch."""
    @security.private
    def getLatestVersion(self, branch_id):
        """Return the latest version object within the given branch, or
        None if the branch contains no versions."""
    @security.private
    def findBranchId(self, version_id):
        """Given a version id, return the id of the branch of the version.
        Note that we cheat, since we can find this out from the id."""
    @security.private
    def getVersionById(self, version_id):
        """Return the version object named by the given version id, or
        raise a VersionControlError if the version is not found."""
    @security.private
    def getVersionByLabel(self, label):
        """Return the version associated with the given label, or None
        if no version matches the given label."""
    @security.private
    def getVersionByDate(self, branch_id, timestamp):
        """Return the last version committed in the given branch on or
        before the given time value. The timestamp should be a float
        (time.time format) value in UTC."""
    @security.private
    def getVersionIds(self, branch_id=None):
        """Return a sequence of version ids for the versions in this
        version history. If a branch_id is given, only version ids
        from that branch will be returned. Note that the sequence
        of ids returned does not include the id of the branch root."""

class BranchInfo(Implicit, Persistent):
    """A utility class to hold branch (line-of-descent) information. It
    maintains the name of the branch, the version id of the root of
    the branch and indices to allow for efficient lookups."""

    security: Incomplete
    date_created: Incomplete
    m_order: Incomplete
    m_date: Incomplete
    name: Incomplete
    root: Incomplete
    def __init__(self, name, root) -> None: ...
    @security.public
    def getId(self):
        """Return the name of the object as string."""
    @security.private
    def append(self, version) -> None:
        """Append a version to the branch information. Note that this
        does not store the actual version, but metadata about the
        version to support ordering and date lookups."""
    @security.private
    def versionIds(self):
        """Return a newest-first sequence of version ids in the branch."""
    @security.private
    def latest(self):
        """Return the version id of the latest version in the branch."""
    def __len__(self) -> int: ...
