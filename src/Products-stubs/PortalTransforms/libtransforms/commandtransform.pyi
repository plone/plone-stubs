from _typeshed import Incomplete

class commandtransform:
    """abstract class for external command based transform"""

    binary: Incomplete
    def __init__(self, name=None, binary=None, **kwargs) -> None: ...
    def name(self): ...
    def initialize_tmpdir(self, data, **kwargs):
        """create a temporary directory, copy input in a file there
        return the path of the tmp dir and of the input file
        """
    def subObjects(self, tmpdir): ...
    def fixImages(self, path, images, objects) -> None: ...
    def cleanDir(self, tmpdir) -> None: ...

class popentransform:
    """abstract class for external command based transform

    Command must read from stdin and write to stdout
    """

    binaryName: str
    binaryArgs: str
    binary: Incomplete
    def __init__(self, name=None, binary=None, binaryArgs=None, **kwargs) -> None: ...
    def name(self): ...
    def convert(self, data, cache, **kwargs): ...
