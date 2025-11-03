from _typeshed import Incomplete
from plone.restapi.services import Service

FALSE_VALUES: Incomplete

class UsersDelete(Service):
    """Deletes a user."""

    params: Incomplete
    portal_membership: Incomplete
    acl_users: Incomplete
    def __init__(self, context, request) -> None: ...
    @property
    def is_zope_manager(self): ...
    def publishTraverse(self, request, name): ...
    def reply(self): ...
