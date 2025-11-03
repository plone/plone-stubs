from _typeshed import Incomplete
from Acquisition import Implicit
from email.generator import BytesGenerator
from email.message import Message
from OFS.role import RoleManager
from OFS.SimpleItem import Item
from Persistence import Persistent

queue_threads: Incomplete
LOG: Incomplete
CHARSET_RE: Incomplete

class MailHostError(Exception): ...

manage_addMailHostForm: Incomplete

def manage_addMailHost(
    self,
    id,
    title: str = "",
    smtp_host: str = "localhost",
    localhost: str = "localhost",
    smtp_port: int = 25,
    timeout: float = 1.0,
    REQUEST=None,
) -> None:
    """Add a MailHost into the system."""

add = manage_addMailHost

class MailBase(Implicit, Item, RoleManager):
    """a mailhost...?"""

    meta_type: str
    zmi_icon: str
    manage: Incomplete
    manage_main: Incomplete
    index_html: Incomplete
    security: Incomplete
    smtp_uid: str
    smtp_pwd: str
    smtp_queue: bool
    smtp_queue_directory: str
    force_tls: bool
    implicit_tls: bool
    lock: Incomplete
    manage_options: Incomplete
    id: Incomplete
    title: Incomplete
    smtp_host: Incomplete
    smtp_port: Incomplete
    def __init__(
        self,
        id: str = "",
        title: str = "",
        smtp_host: str = "localhost",
        smtp_port: int = 25,
        force_tls: bool = False,
        implicit_tls: bool = False,
        smtp_uid: str = "",
        smtp_pwd: str = "",
        smtp_queue: bool = False,
        smtp_queue_directory: str = "/tmp",
    ) -> None:
        """Initialize a new MailHost instance."""
    def manage_makeChanges(
        self,
        title,
        smtp_host,
        smtp_port,
        smtp_uid: str = "",
        smtp_pwd: str = "",
        smtp_queue: bool = False,
        smtp_queue_directory: str = "/tmp",
        force_tls: bool = False,
        implicit_tls: bool = False,
        REQUEST=None,
    ):
        """Make the changes."""
    def sendTemplate(
        trueself,
        self,
        messageTemplate,
        statusTemplate=None,
        mto=None,
        mfrom=None,
        encode=None,
        REQUEST=None,
        immediate: bool = False,
        charset=None,
        msg_type=None,
    ): ...
    def send(
        self,
        messageText,
        mto=None,
        mfrom=None,
        subject=None,
        encode=None,
        immediate: bool = False,
        charset=None,
        msg_type=None,
    ) -> None: ...
    scheduledSend = send
    def simple_send(
        self, mto, mfrom, subject, body, immediate: bool = False
    ) -> None: ...
    def queueLength(self):
        """return length of mail queue"""
    def queueThreadAlive(self):
        """return True/False is queue thread is working"""
    def queueNonDeliveryMode(self):
        """Return the queue delivery mode as a boolean flag

        Returns:
            - ``True`` if the queue is in queue-only non-delivery mode
            - ``False`` if the queue is in active delivery mode
        """
    def manage_restartQueueThread(self, action: str = "start", REQUEST=None):
        """Restart the queue processor thread"""

class MailHost(Persistent, MailBase):
    """persistent version"""

ENCODERS: Incomplete

def as_bytes(msg): ...

class FixedBytesGenerator(BytesGenerator): ...

class FixedMessage(Message):
    def as_bytes(self, unixfrom: bool = False, policy=None): ...

fixed_policy: Incomplete
