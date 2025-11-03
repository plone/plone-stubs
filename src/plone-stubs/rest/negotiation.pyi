def parse_accept_header(accept):
    """Parse the given Accept header ignoring any parameters and return a list
    of media type tuples.
    """

def lookup_service_id(method, accept):
    """Lookup the service id for the given request method and Accept header.
    Only Accept headers containing exactly one media type are considered for
    negotiation.
    """

def register_service(method, media_type):
    """Register a service for the given request method and media type and
    return it's service id.
    """
