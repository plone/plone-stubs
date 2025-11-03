def uuidToPhysicalPath(uuid):
    """Given a UUID, attempt to return the absolute path of the underlying
    object. Will return None if the UUID can't be found.

    This version is four times faster than the original.

    Note: the user may not be authorized to view the object at this path.
    It is up to the caller to check this, if needed.
    """

def uuidToURL(uuid):
    """Given a UUID, attempt to return the absolute URL of the underlying
    object. Will return None if the UUID can't be found.

    Note: the user may not be authorized to view the object at the url.
    It is up to the caller to check this, if needed.
    """

def uuidToObject(uuid, unrestricted: bool = False):
    """Given a UUID, attempt to return a content object. Will return
    None if the UUID can't be found.

    Note: the user may not be authorized to view the object.
    It is up to the caller to check this, if needed.

    If the author is authorised to view the object, unrestricted flag should be set to True
    """

def uuidToCatalogBrain(uuid):
    """Given a UUID, attempt to return a catalog brain.

    Note: the user may not be authorized to view the object for this brain.
    It is up to the caller to check this, if needed.
    """
