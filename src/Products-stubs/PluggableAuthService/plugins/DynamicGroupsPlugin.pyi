from ..plugins.BasePlugin import BasePlugin
from ..utils import csrf_only
from _typeshed import Incomplete
from AccessControl.requestmethod import postonly
from OFS.Cache import Cacheable
from OFS.Folder import Folder
from OFS.PropertyManager import PropertyManager
from OFS.SimpleItem import SimpleItem
from zope.interface import Interface

class IDynamicGroupsPlugin(Interface):
    """Marker interface."""

manage_addDynamicGroupsPluginForm: Incomplete

def addDynamicGroupsPlugin(dispatcher, id, title: str = "", RESPONSE=None) -> None:
    """Add a DGP to 'dispatcher'."""

class DynamicGroupDefinition(SimpleItem, PropertyManager):
    """Represent a single dynamic group."""

    meta_type: str
    security: Incomplete
    title: Incomplete
    description: Incomplete
    active: Incomplete
    def __init__(self, id, predicate, title, description, active) -> None: ...
    def __call__(self, principal, request=None):
        """Evaluate our expression to determine whether 'principal' belongs."""
    manage_options: Incomplete

class DynamicGroupsPlugin(Folder, BasePlugin, Cacheable):
    """Define groups via business rules.

    o Membership in a candidate group is established via a predicate,
      expressed as a TALES expression.  Names available to the predicate
      include:

      'group' -- the dynamic group definition object itself

      'plugin' -- this plugin object

      'principal' -- the principal being tested.

      'request' -- the request object.
    """

    meta_type: str
    zmi_icon: str
    security: Incomplete
    title: Incomplete
    def __init__(self, id, title: str = "") -> None: ...
    def getGroupsForPrincipal(self, principal, request=None):
        """See IGroupsPlugin."""
    def enumerateGroups(
        self, id=None, exact_match: bool = False, sort_by=None, max_results=None, **kw
    ):
        """See IGroupEnumerationPlugin."""
    def listGroupIds(self):
        """Return a list of IDs for the dynamic groups we manage."""
    def getGroupInfo(self, group_id, raise_keyerror: bool = True):
        """Return a mappings describing one dynamic group we manage.

        o If 'raise_keyerror' is True, raise KeyError if we don't have an
          existing group definition for 'group_ id'.  Otherwise, return
          None.

        o Keys include:

          'id' -- the group's ID

          'predicate' -- the TALES expression defining group membership

          'active' -- boolean flag:  is the group currently active?
        """
    def listGroupInfo(self):
        """Return a list of mappings describing the dynamic groups we manage.

        o Keys include:

          'id' -- the group's ID

          'predicate' -- the TALES expression defining group membership

          'active' -- boolean flag:  is the group currently active?
        """
    @security.private
    def addGroup(
        self,
        group_id,
        predicate,
        title: str = "",
        description: str = "",
        active: bool = True,
    ) -> None:
        """Add a group definition.

        o Raise KeyError if we have an existing group definition
          for 'group_id'.
        """
    @security.private
    def updateGroup(
        self, group_id, predicate, title=None, description=None, active=None
    ) -> None:
        """Update a group definition.

        o Raise KeyError if we don't have an existing group definition
          for 'group_id'.

        o Don't update 'title', 'description', or 'active' unless supplied.
        """
    @security.private
    def removeGroup(self, group_id) -> None:
        """Remove a group definition.

        o Raise KeyError if we don't have an existing group definition
          for 'group_id'.
        """
    manage_options: Incomplete
    manage_groups: Incomplete
    @csrf_only
    @postonly
    def manage_addGroup(
        self,
        group_id,
        title,
        description,
        predicate,
        active: bool = True,
        RESPONSE=None,
        REQUEST=None,
    ) -> None:
        """Add a group via the ZMI."""
    @csrf_only
    @postonly
    def manage_updateGroup(
        self,
        group_id,
        predicate,
        title=None,
        description=None,
        active: bool = True,
        RESPONSE=None,
        REQUEST=None,
    ) -> None:
        """Update a group via the ZMI."""
    @csrf_only
    @postonly
    def manage_removeGroups(self, group_ids, RESPONSE=None, REQUEST=None) -> None:
        """Remove one or more groups via the ZMI."""

class _DynamicGroupFilter:
    def __init__(self, id=None, **kw) -> None: ...
    def __call__(self, group_info): ...
