from _typeshed import Incomplete
from Products.CMFPlone.controlpanel.browser.usergroups import (
    UsersGroupsControlPanelView,
)

class UserMembershipControlPanel(UsersGroupsControlPanelView):
    userid: Incomplete
    gtool: Incomplete
    mtool: Incomplete
    member: Incomplete
    searchResults: Incomplete
    searchString: str
    newSearch: bool
    groups: Incomplete
    def update(self) -> None: ...
    def __call__(self): ...
    def getGroups(self): ...
    def getPotentialGroups(self, searchString): ...
