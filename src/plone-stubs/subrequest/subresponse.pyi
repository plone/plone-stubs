from _typeshed import Incomplete
from ZPublisher.HTTPResponse import HTTPResponse

class SubResponse(HTTPResponse):
    stdout: Incomplete
    def setBody(self, body, title: str = "", is_error: int = 0, **kw):
        """Accept either a stream iterator or a string as the body."""
    def outputBody(self) -> None:
        """Output the response body."""
    def getBody(self):
        """Return the body, however it was written."""
