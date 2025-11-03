from _typeshed import Incomplete
from Products.PluggableAuthService.plugins.LocalRolePlugin import LocalRolePlugin

def manage_addLocalRolesManager(dispatcher, id, title=None, RESPONSE=None) -> None:
    """
    add a local roles manager
    """

manage_addLocalRolesManagerForm: Incomplete

class LocalRolesManager(LocalRolePlugin):
    """Class incorporating local role storage with
    PlonePAS-specific local role permission checking.
    """

    meta_type: str
    security: Incomplete
    title: Incomplete
    def __init__(self, id, title=None) -> None: ...
    def getRolesInContext(self, user, object): ...
    def checkLocalRolesAllowed(self, user, object, object_roles): ...
    def getAllLocalRolesInContext(self, context): ...
