from _typeshed import Incomplete
from Products.CMFPlone.controlpanel.browser.usergroups import (
    UsersGroupsControlPanelView,
)

class GroupDetailsControlPanel(UsersGroupsControlPanelView):
    def get_group_property(self, prop_id): ...
    gtool: Incomplete
    gdtool: Incomplete
    regtool: Incomplete
    groupname: Incomplete
    grouproles: Incomplete
    group: Incomplete
    grouptitle: Incomplete
    def __call__(self): ...
