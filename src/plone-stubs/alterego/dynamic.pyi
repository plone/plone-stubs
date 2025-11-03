from types import ModuleType

__all__ = ["create"]

class DynamicModule(ModuleType):
    """A module that can create objects on the fly."""
    def __getattr__(self, name): ...

def create(dotted_name): ...
