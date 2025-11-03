from _typeshed import Incomplete
from Products.PortalTransforms.libtransforms.commandtransform import commandtransform

class pdf_to_html(commandtransform):
    inputs: Incomplete
    output: str
    output_encoding: str
    binaryName: str
    binaryArgs: str
    def __init__(self) -> None: ...
    def convert(self, data, cache, **kwargs): ...
    def invokeCommand(self, tmpdir, fullname): ...

def register(): ...
