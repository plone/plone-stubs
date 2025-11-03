from plone.restapi.services import Service

class Logout(Service):
    """Handles logout by invalidating the JWT"""
    def reply(self): ...
