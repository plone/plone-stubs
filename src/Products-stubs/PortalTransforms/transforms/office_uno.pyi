from _typeshed import Incomplete
from Products.PortalTransforms.libtransforms.commandtransform import commandtransform

class document(commandtransform):
    outputfile: Incomplete
    def __init__(self, name, data) -> None:
        """Initialization: create tmp work directory and copy the
        document into a file"""
    def convert(self) -> None:
        """Convert the document"""
    def html(self): ...
