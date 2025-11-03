from _typeshed import Incomplete
from Products.CMFPlone.controlpanel.browser.usergroups import (
    UsersGroupsControlPanelView,
)

class GroupMembershipControlPanel(UsersGroupsControlPanelView):
    groupname: Incomplete
    gtool: Incomplete
    mtool: Incomplete
    group: Incomplete
    grouptitle: Incomplete
    canAddUsers: bool
    groupquery: Incomplete
    groupkeyquery: Incomplete
    searchResults: Incomplete
    searchString: str
    newSearch: bool
    groupMembers: Incomplete
    def update(self) -> None: ...
    def __call__(self): ...
    def isGroup(self, itemName): ...
    def getMembers(self): ...
    def getPotentialMembers(self, searchString): ...
