from _typeshed import Incomplete
from OFS.CopySupport import CopyError as CopyError
from zExceptions import BadRequest as BadRequest
from zExceptions import NotFound as NotFound
from zExceptions import ResourceLockedError as ResourceLockedError

security: Incomplete

class SkinPathError(Exception):
    """Invalid skin path error."""
