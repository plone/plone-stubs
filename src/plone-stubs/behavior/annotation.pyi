from _typeshed import Incomplete

class AnnotationsFactoryImpl:
    """A factory that knows how to store data in annotations.

    Each value will be stored as a primitive in the annotations under a key
    that consists of the full dotted name to the field being stored.

    This class is not sufficient as an adapter factory on its own. It must
    be initialised with the schema interface in the first place. That is the
    role of the Annotations factory below.
    """
    def __init__(self, context, schema) -> None: ...
    def __getattr__(self, name): ...
    def __setattr__(self, name, value) -> None: ...

class AnnotationStorage:
    """Behavior adapter factory class for storing data in annotations."""

    schema: Incomplete
    __component_adapts__: Incomplete
    def __init__(self, schema) -> None: ...
    def __call__(self, context): ...
