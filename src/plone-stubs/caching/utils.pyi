def lookupOptions(type_, rulename, default=None):
    """Look up all options for a given caching operation type, returning
    a dictionary. The keys of the dictionary will be the items in the
    ``options`` tuple of an ``ICachingOperationType``.

    ``type`` should either be a ``ICachingOperationType`` instance or the name
    of one.

    ``rulename`` is the name of the rule being executed.

    ``default`` is the default value to use for options that cannot be found.
    """

def lookupOption(prefix, rulename, option, default=None, _registry=None):
    """Look up an option for a particular caching operation.

    The idea is that a caching operation may read configuration options from
    plone.registry according to the following rules:

    * If ${prefix}.${rulename}.${option} exists, get that
    * Otherwise, if ${prefix}.${option} exists, get that
    * Otherwise, return ``default``

    This allows an operation to have a default setting, as well as a per-rule
    override.
    """

def findOperation(request): ...
