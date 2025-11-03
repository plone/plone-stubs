from _typeshed import Incomplete
from Products.PortalTransforms.libtransforms.commandtransform import popentransform

class pdf_to_text(popentransform):
    inputs: Incomplete
    output: str
    output_encoding: str
    binaryName: str
    binaryArgs: str

def register(): ...
