from .basetool import IPloneBaseTool
from _typeshed import Incomplete

class IInterfaceTool(IPloneBaseTool):
    """This tool exposes the interface package for TTW applications,
    by accepting a dotted name of an interface and exporting the
    IInterface API"""

    id: Incomplete
    def objectImplements(obj, dotted_name) -> None:
        """Asserts if an object implements a given interface"""
    def classImplements(obj, dotted_name) -> None:
        """Asserts if an object's class implements a given interface"""
    def namesAndDescriptions(dotted_name, all: int = 0) -> None:
        """Returns a list of pairs (name, description) for a given
        interface"""
