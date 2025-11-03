def modify_query_to_enforce_navigation_root(query):
    """enforce a search in the current navigation root

    if not already a path was given we search only for contents in the current
    IVavigationRoot.
    """
