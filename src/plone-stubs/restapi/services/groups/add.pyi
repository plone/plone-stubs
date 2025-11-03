from plone.restapi.services import Service

class GroupsPost(Service):
    """Creates a new group."""
    @property
    def is_zope_manager(self): ...
    def reply(self): ...
