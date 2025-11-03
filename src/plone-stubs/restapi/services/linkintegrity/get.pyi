from plone.restapi.services import Service

class LinkIntegrityGet(Service):
    """
    Return a list of breaches from p.a.linkintegrity view
    """
    def reply(self): ...
