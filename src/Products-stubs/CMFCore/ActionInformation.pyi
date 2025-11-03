from _typeshed import Incomplete
from collections import UserDict
from OFS.ObjectManager import IFAwareObjectManager
from OFS.OrderedFolder import OrderedFolder
from OFS.PropertyManager import PropertyManager
from OFS.SimpleItem import SimpleItem

class ActionCategory(IFAwareObjectManager, OrderedFolder):
    """Group of Action objects."""

    security: Incomplete
    @security.private
    def listActions(self):
        """List the actions defined in this category and its subcategories."""

class Action(PropertyManager, SimpleItem):
    """Reference to an action."""

    i18n_domain: str
    link_target: str
    security: Incomplete
    manage_options: Incomplete
    id: Incomplete
    def __init__(self, id, **kw) -> None: ...
    @security.private
    def getInfoData(self):
        """Get the data needed to create an ActionInfo."""

class ActionInfo(UserDict):
    """A lazy dictionary for Action infos."""

    __allow_access_to_unprotected_subobjects__: int
    def __init__(self, action, ec) -> None: ...
    def __getitem__(self, key): ...
    def __eq__(self, other): ...
    def copy(self): ...
    def update(*args, **kwargs) -> None: ...

class ActionInformation(SimpleItem):
    """Represent a single selectable action.

    Actions generate links to views of content, or to specific methods
    of the site.  They can be filtered via their conditions.
    """

    link_target: str
    __allow_access_to_unprotected_subobjects__: int
    security: Incomplete
    def __init__(
        self,
        id,
        title: str = "",
        description: str = "",
        category: str = "object",
        condition: str = "",
        permissions=(),
        priority: int = 10,
        visible: bool = True,
        action: str = "",
        icon_expr: str = "",
        link_target: str = "",
    ) -> None:
        """Set up an instance."""
    id: Incomplete
    title: Incomplete
    description: Incomplete
    category: Incomplete
    condition: Incomplete
    permissions: Incomplete
    priority: Incomplete
    visible: Incomplete
    @security.private
    def edit(
        self,
        id=...,
        title=...,
        description=...,
        category=...,
        condition=...,
        permissions=...,
        priority=...,
        visible=...,
        action=...,
        icon_expr=...,
        link_target=...,
    ) -> None:
        """Edit the specified properties."""
    def Title(self):
        """Return the Action title."""
    def Description(self):
        """Return a description of the action."""
    @security.private
    def testCondition(self, ec):
        """Evaluate condition using context, 'ec', and return 0 or 1."""
    @security.public
    def getAction(self, ec):
        """Compute the action using context, 'ec'; return a mapping of
        info about the action.
        """
    action: Incomplete
    @security.public
    def getActionExpression(self):
        """Return the text of the TALES expression for our URL."""
    @security.private
    def setActionExpression(self, action) -> None: ...
    icon_expr: Incomplete
    @security.public
    def getIconExpression(self):
        """Return the text of the TALES expression for our icon URL."""
    @security.private
    def setIconExpression(self, icon_expr) -> None: ...
    @security.public
    def getCondition(self):
        """Return the text of the TALES expression for our condition."""
    @security.public
    def getPermissions(self):
        """Return the permission, if any, required to execute the action.

        Return an empty tuple if no permission is required.
        """
    @security.public
    def getCategory(self):
        """Return the category in which the action should be grouped."""
    @security.public
    def getVisibility(self):
        """Return whether the action should be visible in the CMF UI."""
    @security.public
    def getLinkTarget(self):
        """Return the rendered link tag's target attribute value"""
    @security.private
    def getMapping(self):
        """Get a mapping of this object's data."""
    @security.private
    def clone(self):
        """Get a newly-created AI just like us."""
    @security.private
    def getInfoData(self):
        """Get the data needed to create an ActionInfo."""

def getOAI(context, object=None): ...

class oai:
    __allow_access_to_unprotected_subobjects__: int
    isAnonymous: Incomplete
    user_id: Incomplete
    portal: Incomplete
    portal_url: Incomplete
    folder_url: Incomplete
    folder: Incomplete
    object: Incomplete
    content_url: Incomplete
    def __init__(self, tool, folder, object=None) -> None: ...
    def __getitem__(self, name): ...
