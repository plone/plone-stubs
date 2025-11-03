from _typeshed import Incomplete

logger: Incomplete
SIZE_CONST: Incomplete
SIZE_ORDER: Incomplete

def human_readable_size(size):
    """Get a human readable size string."""

def safe_int(value, default: int = 0):
    """Convert value to integer or just return 0 if we can\'t

    >>> safe_int(45)
    45

    >>> safe_int("42")
    42

    >>> safe_int("spam")
    0

    >>> safe_int([])
    0

    >>> safe_int(None)
    0

    >>> safe_int(None, default=-1)
    -1
    """

def safeToInt(value, default: int = 0): ...
def safe_text(value, encoding: str = "utf-8") -> str:
    """Converts a value to text, even it is already a text string.

    >>> test_bytes = u'Ƶ'.encode('utf-8')
    >>> safe_text('spam') == u'spam'
    True
    >>> safe_text(b'spam') == u'spam'
    True
    >>> safe_text(u'spam') == u'spam'
    True
    >>> safe_text(u'spam'.encode('utf-8')) == u'spam'
    True
    >>> safe_text(test_bytes) == u'Ƶ'
    True
    >>> safe_text(u'Æµ'.encode('iso-8859-1')) == u'Ƶ'
    True
    >>> safe_text(test_bytes, encoding='ascii') == u'Ƶ'
    True
    >>> safe_text(1) == 1
    True
    >>> print(safe_text(None))
    None
    """

def safe_bytes(value, encoding: str = "utf-8") -> bytes:
    """Convert text to bytes of the specified encoding."""

def safe_hasattr(obj, name, _marker=...):
    """Make sure we don't mask exceptions like hasattr().

    We don't want exceptions other than AttributeError to be masked,
    since that too often masks other programming errors.
    Three-argument getattr() doesn't mask those, so we use that to
    implement our own hasattr() replacement.
    """

def base_hasattr(obj, name):
    """Like safe_hasattr, but also disables acquisition."""

def safe_callable(obj):
    """Make sure our callable checks are ConflictError safe."""

def get_empty_title(context, translated: bool = True):
    """Returns string to be used for objects with no title or id"""

def pretty_title_or_id(context, obj, empty_value=...):
    """Return the best possible title or id of an item, regardless
    of whether obj is a catalog brain or an object, but returning an
    empty title marker if the id is not set (i.e. it's auto-generated).
    """

def get_installer(context, request=None): ...
def is_expired(content):
    """Find out if the object is expired (copied from skin script)"""

def get_top_request(request):
    """Get highest request from a subrequest."""

def get_top_site_from_url(context, request):
    """
    Find the first ISite object that appears in the pre-virtual-hosting URL
    path, falling back to the object pointed by the virtual hosting root.

    Use this method if you need a "root object" reference to generate URLs
    that will be used by, and will work correctly from the standpoint of,
    *browser* code (JavaScript / XML HTTP requests) after virtual hosting has
    been applied.  *Never* use this to get to a site root in Plone server code
    -- it is not appropriate for that use.

    If the current context is within a subsite within a PloneSiteRoot and no
    virtual hosting is in place, the PloneSiteRoot is returned.
    When at the same context but in a virtual hosting environment with the
    virtual host root pointing to the subsite, it returns the subsite instead
    the PloneSiteRoot.  Finally, if the virtual hosting environment points to
    a *child* of a site/subsite, that child returns instead of the site/subsite.

    For this given content structure:

    /Plone/Subsite:
      /file
      /en-US
        /folder
          /image

    It should return the following in these cases:

    - No virtual hosting
      URL path:              /Plone
      Object accessed:       /Plone
      Returns:               Plone

    - No virtual hosting
      URL path:              /Plone/Subsite
      Object accessed:       /Plone/Subsite
      Returns:               Plone

    - Virtual hosting root:  /Plone/Subsite
      URL path:              /
      Object accessed:       /Plone/Subsite
      Returns:               Subsite

    - Virtual hosting root:  /Plone/Subsite
      URL path:              /file
      Object accessd:        /Plone/Subsite/file
      Returns:               Subsite

    - Virtual hosting root:  /Plone/Subsite/en-US
      URL path:              /folder/image
      Object accessed:       /Plone/Subsite/en-US/folder/image
      Returns:               Subsite/en-US
      (in this last case -- common with p.a.multilingual and usually described
       as subdomain hosting for languages -- no Site object is visible TTW,
       so it must return the topmost visible container, since the callees
       need an object with a valid, TTW-visible URL to do their work.)
    """

def transaction_note(note) -> None:
    """Write human legible note"""

def check_id(
    context,
    id=None,
    required: int = 0,
    alternative_id=None,
    contained_by=None,
    **kwargs,
):
    """Test an id to make sure it is valid.

    This used to be in Products/CMFPlone/skins/plone_scripts/check_id.py.

    Returns an error message if the id is bad or None if the id is good.
    Parameters are as follows:

        id - the id to check

        required - if False, id can be the empty string

        alternative_id - an alternative value to use for the id
        if the id is empty or autogenerated

    Accept keyword arguments for compatibility with the fallback
    in Products.validation.

    Note: The reason the id is included is to handle id error messages for
    such objects as files and images that supply an alternative id when an
    id is auto-generated.
    If you say "There is already an item with this name in this folder"
    for an image that has the Name field populated with an autogenerated id,
    it can cause some confusion; since the real problem is the name of
    the image file name, not in the name of the autogenerated id.
    """

def get_user_friendly_types(types_list=None):
    """List of types which are considered "user friendly" for search and selection purposes.

    This is the list of types available in the portal, minus those defined in the
    `types_not_searched` property in registry, if it exists.

    If typesList is given, this is used as the base list;
    else all types from portal_types are used.
    """

def unrestricted_construct_instance(type_name, container, id, *args, **kw):
    """Create an object without performing security checks

    invokeFactory and fti.constructInstance perform some security checks
    before creating the object. Use this function instead if you need to
    skip these checks.

    This method uses
    CMFCore.TypesTool.FactoryTypeInformation._constructInstance
    to create the object without security checks.
    """

def is_truthy(value) -> bool:
    """Return `True`, if "yes" was meant, `False` otherwise."""
