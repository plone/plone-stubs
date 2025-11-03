from _typeshed import Incomplete
from Products.CMFPlone.controlpanel.browser.usergroups import (
    UsersGroupsControlPanelView,
)

class GroupsOverviewControlPanel(UsersGroupsControlPanelView):
    searchString: Incomplete
    searchResults: Incomplete
    newSearch: bool
    def __call__(self): ...
    def doSearch(self, searchString):
        """Search for a group by id or title"""
    def manageGroup(self, groups=None, delete=None) -> None: ...
