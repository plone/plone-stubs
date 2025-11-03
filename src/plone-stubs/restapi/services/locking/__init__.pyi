def creator_name(userid): ...
def creator_url(userid): ...
def creation_date(timestamp): ...
def lock_info(obj):
    """Returns lock information about the given object."""

def webdav_lock(obj):
    """Returns the WebDAV LockItem"""

def is_locked(obj, request):
    """Returns true if the object is locked and the request doesn't contain
    the lock token.
    """
