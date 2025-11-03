def registerPortletType(site, title, description, addview, for_=...) -> None:
    """Register a new type of portlet.

    site should be the local site where the registration should be made. The
    title and description should be meaningful metadata about the portlet for
    the UI.

    The addview should be the name of an add view registered, and must be
    unique.
    """

def unregisterPortletType(site, addview) -> None:
    """Unregister a portlet type.

    site is the local site where the registration was made. The addview
    should is used to uniquely identify the portlet.
    """

def hashPortletInfo(info):
    """Creates a hash from the portlet information.

    This is a bidirectional function. The hash must only contain characters
    acceptable as part of a html id.

    info is the portlet info dictionary. Hash is put into info, and
    also returned.
    """

def unhashPortletInfo(hash):
    """Creates the portlet info from the hash.

    Output is the info dictionary (containing only the
    hashed fields).
    """
