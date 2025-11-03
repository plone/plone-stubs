from zope.interface import Interface

class IReadInterface(Interface):
    def getDirectlyProvided() -> None:
        """List the interfaces directly implemented by the object."""
    def getDirectlyProvidedNames() -> None:
        """List the names of interfaces directly implemented by the object."""
    def getAvailableInterfaces() -> None:
        """List the marker interfaces available for the object."""
    def getAvailableInterfaceNames() -> None:
        """List the names of marker interfaces available for the object."""
    def getInterfaces() -> None:
        """List interfaces provided by the class of the object."""
    def getInterfaceNames() -> None:
        """List the names of interfaces provided by the class of the object."""
    def getProvided() -> None:
        """List interfaces provided by the object."""
    def getProvidedNames() -> None:
        """List the names of interfaces provided by the object."""

class IWriteInterface(Interface):
    def update(add=(), remove=()) -> None:
        """Update directly provided interfaces of the object."""
    def mark(interface) -> None:
        """Add interface to interfaces the object directly provides."""
    def erase(interface) -> None:
        """Remove interfaces from interfaces the object directly provides."""

class IMarkerInterfaces(IReadInterface, IWriteInterface):
    """Provides methods for inspecting and assigning marker interfaces."""
