class UniqueResourceLookup:
    """Unique resource ruleset lookup.

    Returns 'plone.stableResource' for requests marked with
    IUniqueResourceRequest.
    """
    def __init__(self, published, request) -> None: ...
    def __call__(self): ...
