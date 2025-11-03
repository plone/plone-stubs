from _typeshed import Incomplete

def register_method_for_preflight(method, service_id) -> None:
    """Register the given method for preflighting with the given service_id."""

def lookup_preflight_service_id(method):
    """Lookup a service id for the given preflighted method."""

class CORSPolicy:
    context: Incomplete
    request: Incomplete
    def __init__(self, context, request) -> None: ...
    def process_simple_request(self):
        """Process the current request as a simple CORS request by setting the
        appropriate access control headers. Returns True if access control
        headers were set.
        """
    def process_preflight_request(self):
        """Process the current request as a CORS preflight request by setting
        the appropriate access control headers. Returns True if access
        control headers were set.
        """
