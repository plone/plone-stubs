from plone.restapi.services import Service

class SharingGet(Service):
    """Returns a serialized content object."""
    def reply(self): ...

class SharingPost(Service):
    def reply(self): ...
