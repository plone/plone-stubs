from _typeshed import Incomplete
from zope.interface.declarations import ObjectSpecificationDescriptor

class WrapperSpecification(ObjectSpecificationDescriptor):
    """A __providedBy__ decorator that returns the interfaces provided by
    the wrapped object when asked.
    """
    def __get__(self, inst, cls=None): ...

class IndexableObjectWrapper:
    """A simple wrapper for indexable objects that will delegate to IIndexer
    adapters as appropriate.
    """

    __providedBy__: Incomplete
    def __init__(self, object, catalog) -> None: ...
    def __getattr__(self, name): ...
