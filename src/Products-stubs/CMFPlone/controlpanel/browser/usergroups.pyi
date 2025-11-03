from _typeshed import Incomplete
from plone.autoform.form import AutoExtensibleForm
from plone.base.interfaces import IUserGroupsSettingsSchema
from plone.z3cform import layout
from Products.Five.browser import BrowserView
from z3c.form import form

class UserGroupsSettingsControlPanel(AutoExtensibleForm, form.EditForm):
    schema = IUserGroupsSettingsSchema
    id: str
    label: Incomplete
    form_name: Incomplete
    control_panel_view: str
    def handleApply(self, action) -> None: ...
    def updateActions(self) -> None: ...

class ControlPanelFormWrapper(layout.FormWrapper):
    """Use this form as the plone.z3cform layout wrapper to get the control
    panel layout.
    """

    index: Incomplete

UserGroupsSettingsPanelView: Incomplete

class UsersGroupsControlPanelView(BrowserView):
    @property
    def portal_roles(self): ...
    @property
    def many_users(self): ...
    @property
    def many_groups(self): ...
    @property
    def email_as_username(self): ...
    def makeQuery(self, **kw): ...
    def membershipSearch(
        self,
        searchString: str = "",
        searchUsers: bool = True,
        searchGroups: bool = True,
        ignore=[],
    ):
        """Search for users and/or groups, returning actual member and group items
        Replaces the now-deprecated prefs_user_groups_search.py script"""
    def atoi(self, s): ...
    @property
    def is_zope_manager(self): ...
    @property
    def show_group_listing_warning(self): ...
    @property
    def show_users_listing_warning(self): ...
