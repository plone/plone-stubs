from zope.interface import Interface

class IReadInterface(Interface):
    def getDirectlyProvided(self) -> None:
        """List the interfaces directly implemented by the object."""
    def getDirectlyProvidedNames(self) -> None:
        """List the names of interfaces directly implemented by the object."""
    def getAvailableInterfaces(self) -> None:
        """List the marker interfaces available for the object."""
    def getAvailableInterfaceNames(self) -> None:
        """List the names of marker interfaces available for the object."""
    def getInterfaces(self) -> None:
        """List interfaces provided by the class of the object."""
    def getInterfaceNames(self) -> None:
        """List the names of interfaces provided by the class of the object."""
    def getProvided(self) -> None:
        """List interfaces provided by the object."""
    def getProvidedNames(self) -> None:
        """List the names of interfaces provided by the object."""

class IWriteInterface(Interface):
    def update(self, add=(), remove=()) -> None:
        """Update directly provided interfaces of the object."""
    def mark(self, interface) -> None:
        """Add interface to interfaces the object directly provides."""
    def erase(self, interface) -> None:
        """Remove interfaces from interfaces the object directly provides."""

class IMarkerInterfaces(IReadInterface, IWriteInterface):
    """Provides methods for inspecting and assigning marker interfaces."""
