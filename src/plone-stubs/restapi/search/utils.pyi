def unflatten_dotted_dict(dct):
    """Reconstructs nesting for a dict that has been flattened to one level.

    Further nesting is indicated by dots in the key names: Keys will be merged
    together into sub-dicts based on their longest common prefix.

    Example:

    >>> dct = {
    ...     'a.b.X': 1,
    ...     'a.b.Y': 2,
    ...     'a.foo': 3,
    ...     'bar': 4,
    ... }
    >>>
    >>> unflatten_dotted_dict(dct)

    {'a': {'b': {'X': 1,
                 'Y': 2},
           'foo': 3},
     'bar': 4}
    """
