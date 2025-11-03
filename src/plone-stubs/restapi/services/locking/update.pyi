from plone.restapi.services import Service

class Lock(Service):
    """Refresh the lock of an object"""
    def reply(self): ...
