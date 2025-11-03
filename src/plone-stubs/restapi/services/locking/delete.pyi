from plone.restapi.services import Service

class Lock(Service):
    """Unlock an object"""
    def reply(self): ...
