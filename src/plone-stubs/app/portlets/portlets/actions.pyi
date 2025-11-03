from ..portlets import base
from _typeshed import Incomplete
from plone.memoize import view as pm_view
from plone.portlets.interfaces import IPortletDataProvider

class IActionsPortlet(IPortletDataProvider):
    """A portlet that shows an action category"""

    ptitle: Incomplete
    show_title: Incomplete
    category: Incomplete
    show_icons: Incomplete
    default_icon: Incomplete

class Assignment(base.Assignment):
    """Portlet assignment.
    This is what is actually managed through the portlets UI and associated
    with columns.
    """

    ptitle: str
    show_title: bool
    category: str
    show_icons: bool
    default_icon: str
    def __init__(
        self,
        ptitle: str = "",
        show_title: bool = True,
        category: str = "",
        show_icons: bool = True,
        default_icon: str = "action_icon.png",
    ) -> None: ...
    @property
    def title(self):
        """This property is used to give the title of the portlet in the
        "manage portlets" screen.
        """

class Renderer(base.Renderer):
    """Actions portlet renderer."""

    render: Incomplete
    @property
    def available(self):
        """Override base class"""
    @property
    def title(self):
        """Portlet title"""
    @property
    def showTitle(self):
        """Show portlet title"""
    def actionLinks(self):
        """Features of action links"""
    @property
    def category(self): ...
    @pm_view.memoize
    def cachedLinks(self, actions_category, default_icon, show_icons): ...

class AddForm(base.AddForm):
    """Portlet add form.
    This is registered in configure.zcml. The schema attribute tells
    plone.autoform which fields to display. The create() method actually
    constructs the assignment that is being added.
    """

    schema = IActionsPortlet
    label: Incomplete
    description: Incomplete
    def create(self, data): ...

class EditForm(base.EditForm):
    """Portlet edit form.

    This is registered with configure.zcml. The schema attribute tells
    plone.autoform which fields to display.
    """

    schema = IActionsPortlet
