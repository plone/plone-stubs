def __before_publishing_traverse__(self, arg1, arg2=None):
    """Pre-traversal hook that stops traversal to prevent the default view
    to be appended. Appending the default view would break REST calls.
    """
