from _typeshed import Incomplete
from Acquisition import Implicit

class Logger:
    def __init__(self, id, messages) -> None:
        """Initialize the logger with a name and an optional level."""
    def debug(self, msg, *args, **kwargs) -> None:
        """Log 'msg % args' with severity 'DEBUG'."""
    def info(self, msg, *args, **kwargs) -> None:
        """Log 'msg % args' with severity 'INFO'."""
    def warning(self, msg, *args, **kwargs) -> None:
        """Log 'msg % args' with severity 'WARNING'."""
    def error(self, msg, *args, **kwargs) -> None:
        """Log 'msg % args' with severity 'ERROR'."""
    def exception(self, msg, *args) -> None:
        """Convenience method for logging an ERROR with exception information."""
    def critical(self, msg, *args, **kwargs) -> None:
        """Log 'msg % args' with severity 'CRITICAL'."""
    def log(self, level, msg, *args, **kwargs) -> None:
        """Log 'msg % args' with the integer severity 'level'."""

class SetupEnviron(Implicit):
    """Context for body im- and exporter."""

    security: Incomplete
    def __init__(self) -> None: ...
    def getLogger(self, name):
        """Get a logger with the specified name, creating it if necessary."""
    def shouldPurge(self):
        """When installing, should the existing setup be purged?"""

class BaseContext(SetupEnviron):
    security: Incomplete
    def __init__(self, tool, encoding) -> None: ...
    def getSite(self):
        """See ISetupContext."""
    def getSetupTool(self):
        """See ISetupContext."""
    def getEncoding(self):
        """See ISetupContext."""
    def getLogger(self, name):
        """See ISetupContext."""
    def listNotes(self):
        """See ISetupContext."""
    def clearNotes(self) -> None:
        """See ISetupContext."""

class DirectoryImportContext(BaseContext):
    security: Incomplete
    def __init__(
        self, tool, profile_path, should_purge: bool = False, encoding=None
    ) -> None: ...
    def openDataFile(self, filename, subdir=None):
        """See IImportContext."""
    def readDataFile(self, filename, subdir=None):
        """See IImportContext."""
    def getLastModified(self, path):
        """See IImportContext."""
    def isDirectory(self, path):
        """See IImportContext."""
    def listDirectory(self, path, skip=..., skip_suffixes=...):
        """See IImportContext."""

class DirectoryExportContext(BaseContext):
    security: Incomplete
    def __init__(self, tool, profile_path, encoding=None) -> None: ...
    def openDataFile(self, filename, content_type, subdir=None):
        """See IChunkableExportContext."""
    def writeDataFile(self, filename, text, content_type, subdir=None) -> None:
        """See IExportContext."""

class TarballImportContext(BaseContext):
    security: Incomplete
    def __init__(
        self, tool, archive_bits, encoding=None, should_purge: bool = False
    ) -> None: ...
    def readDataFile(self, filename, subdir=None):
        """See IImportContext."""
    def getLastModified(self, path):
        """See IImportContext."""
    def isDirectory(self, path):
        """See IImportContext."""
    def listDirectory(self, path, skip=..., skip_suffixes=...):
        """See IImportContext."""
    def shouldPurge(self):
        """See IImportContext."""

class TarballExportContext(BaseContext):
    security: Incomplete
    def __init__(self, tool, encoding=None) -> None: ...
    def writeDataFile(self, filename, text, content_type, subdir=None) -> None:
        """See IExportContext."""
    def getArchive(self):
        """Close the archive, and return it as a big string."""
    def getArchiveFilename(self):
        """Close the archive, and return it as a big string."""

class SnapshotExportContext(BaseContext):
    security: Incomplete
    def __init__(self, tool, snapshot_id, encoding=None) -> None: ...
    def writeDataFile(self, filename, text, content_type, subdir=None) -> None:
        """See IExportContext."""
    def getSnapshotURL(self):
        """See IExportContext."""
    def getSnapshotFolder(self):
        """See IExportContext."""

class SnapshotImportContext(BaseContext):
    security: Incomplete
    def __init__(
        self, tool, snapshot_id, should_purge: bool = False, encoding=None
    ) -> None: ...
    def readDataFile(self, filename, subdir=None):
        """See IImportContext."""
    def getLastModified(self, path):
        """See IImportContext."""
    def isDirectory(self, path):
        """See IImportContext."""
    def listDirectory(self, path, skip=(), skip_suffixes=()):
        """See IImportContext."""
    def shouldPurge(self):
        """See IImportContext."""
