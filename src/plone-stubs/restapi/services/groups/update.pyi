from _typeshed import Incomplete
from plone.restapi.services import Service

class GroupsPatch(Service):
    """Update an existing group with users, roles, groups, title and description.

    Args:
        data (dict): dictionary of
        id: str
        users: dict: The users object is a mapping of a user_id and a boolean indicating adding or removing from the group.
        roles: list of str
        groups: list of str
        title: str
        description: str

    Raises:
        BadRequest: No group with this id exists.

    Response:
        HTTP/1.1 204 No Content
    """

    params: Incomplete
    def __init__(self, context, request) -> None: ...
    @property
    def is_zope_manager(self): ...
    def can_update(self, group, users, roles, groups): ...
    def publishTraverse(self, request, name): ...
    def reply(self): ...
