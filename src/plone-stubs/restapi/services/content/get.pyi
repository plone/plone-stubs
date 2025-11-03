from plone.restapi.services import Service

class ContentGet(Service):
    """Returns a serialized content object."""
    def reply(self): ...
