from _typeshed import Incomplete

class Chain:
    """Caching operation which chains together several other operations.

    When intercepting the response, the first chained operation to return a
    value will be used. Subsequent operations are ignored. When modifying the
    response, all operations will be called, in order.

    The names of the operations to execute are found in the ``plone.registry``
    option ``plone.caching.operations.chain.operations`` by default, and can
    be customised on a per-rule basis with
    ``plone.caching.operations.chain.${rulename}.chain``.

    The option must be a sequence type (e.g. a ``Tuple``).
    """

    title: Incomplete
    description: Incomplete
    prefix: str
    options: Incomplete
    published: Incomplete
    request: Incomplete
    def __init__(self, published, request) -> None: ...
    def interceptResponse(self, rulename, response): ...
    def modifyResponse(self, rulename, response) -> None: ...
