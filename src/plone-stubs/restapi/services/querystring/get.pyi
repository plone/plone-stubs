from plone.restapi.services import Service

class QuerystringGet(Service):
    """Returns the querystring configuration.

    This basically does the same thing as the '@@querybuilderjsonconfig'
    view from p.a.querystring, but exposes the config via the REST API.
    """
    def reply(self): ...
