from _typeshed import Incomplete
from Products.CMFPlone.controlpanel.browser.usergroups import (
    UsersGroupsControlPanelView,
)

logger: Incomplete

class UsersOverviewControlPanel(UsersGroupsControlPanelView):
    searchString: Incomplete
    searchResults: Incomplete
    newSearch: bool
    def __call__(self): ...
    def doSearch(self, searchString): ...
    def manageUser(self, users=[], resetpassword=[], delete=[]) -> None: ...
    def deleteMembers(self, member_ids) -> None: ...
