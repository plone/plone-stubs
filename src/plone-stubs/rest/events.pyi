def mark_as_api_request(request, accept) -> None:
    """Mark a request as IAPIRequest if there's a service registered for the
    actual request method and Accept header.
    """

def subscriber_mark_as_api_request(event) -> None:
    """Subscriber to mark a request as IAPIRequest (see mark_as_api_request)"""
