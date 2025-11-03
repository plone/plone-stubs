from plone.restapi.services import Service

class Renew(Service):
    """Renew authentication token"""
    def reply(self): ...
