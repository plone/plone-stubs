from Products.PortalTransforms.libtransforms.commandtransform import commandtransform
from win32com.client import constants as constants
from win32com.client import gencache as gencache

class document(commandtransform):
    def __init__(self, name, data) -> None:
        """Initialization: create tmp work
        directory and copy the document into a file"""
    def convert(self) -> None: ...
    def html(self): ...
