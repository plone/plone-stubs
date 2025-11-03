from _typeshed import Incomplete

class SkinsContainer:
    security: Incomplete
    def getSkinPath(self, name) -> None:
        """Convert a skin name to a skin path."""
    def getDefaultSkin(self) -> None:
        """Get the default skin name."""
    def getRequestVarname(self) -> None:
        """Get the variable name to look for in the REQUEST."""
    @security.private
    def getSkinByPath(self, path, raise_exc: int = 0):
        """Get a skin at the given path."""
    @security.private
    def getSkinByName(self, name):
        """Get the named skin."""
