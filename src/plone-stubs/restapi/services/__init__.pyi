from plone.rest import Service as RestService

class Service(RestService):
    """Base class for Plone REST API services"""

    content_type: str
    def render(self): ...
    def check_permission(self) -> None: ...
    def reply(self):
        """Process the request and return a JSON serializable data structure or
        the no content marker if the response body should be empty.
        """
    def reply_no_content(self, status: int = 204): ...
