from plone.restapi.services import Service

class Lock(Service):
    """Lock information about the current lock"""
    def reply(self): ...
