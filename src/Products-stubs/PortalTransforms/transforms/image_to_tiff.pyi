from _typeshed import Incomplete
from Products.PortalTransforms.libtransforms.piltransform import PILTransforms

class image_to_tiff(PILTransforms):
    inputs: Incomplete
    output: str
    format: str

def register(): ...
