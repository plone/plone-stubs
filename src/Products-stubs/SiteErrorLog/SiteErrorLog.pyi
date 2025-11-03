from _typeshed import Incomplete
from OFS.SimpleItem import SimpleItem

LOG: Incomplete
use_error_logging: str
log_to_event_log: str
temp_logs: Incomplete
cleanup_lock: Incomplete

class SiteErrorLog(SimpleItem):
    """Site error log class.  You can put an error log anywhere in the tree
    and exceptions in that area will be posted to the site error log.
    """

    meta_type: str
    id: str
    zmi_icon: str
    zmi_show_add_dialog: bool
    keep_entries: int
    copy_to_zlog: bool
    security: Incomplete
    manage_options: Incomplete
    manage_main: Incomplete
    showEntry: Incomplete
    @security.private
    def manage_beforeDelete(self, item, container) -> None: ...
    @security.private
    def manage_afterAdd(self, item, container) -> None: ...
    def forgetEntry(self, id, REQUEST=None) -> None:
        """Removes an entry from the error log."""
    @security.private
    def raising(self, info):
        """Log an exception.

        Called by SimpleItem's exception handler.
        Returns the url to view the error log entry
        """
    def getProperties(self): ...
    def checkEventLogPermission(self): ...
    def setProperties(
        self, keep_entries, copy_to_zlog: int = 0, ignored_exceptions=(), RESPONSE=None
    ) -> None:
        """Sets the properties of this site error log."""
    def getLogEntries(self):
        """Returns the entries in the log, most recent first.

        Makes a copy to prevent changes.
        """
    def getLogEntryById(self, id):
        """Returns the specified log entry.

        Makes a copy to prevent changes.  Returns None if not found.
        """
    def getLogEntryAsText(self, id, RESPONSE=None):
        """Returns the specified log entry.

        Makes a copy to prevent changes.  Returns None if not found.
        """

def manage_addErrorLog(dispatcher, RESPONSE=None) -> None:
    """Add a site error log to a container."""

def IPubFailureSubscriber(event) -> None:
    """Handles an IPubFailure event triggered by the WSGI Publisher.
    This handler forwards the event to the SiteErrorLog object
    closest to the published object that the error occured with,
    it logs no error if no published object was found.
    """
