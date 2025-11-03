from _typeshed import Incomplete

LOGGER: Incomplete

class Transformer:
    """Delegate the opportunity to transform the response to multiple,
    ordered adapters.
    """
    def __call__(self, request, result, encoding): ...
