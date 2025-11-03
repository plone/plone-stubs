from plone.formwidget.namedfile import utils as utils
from plone.formwidget.namedfile.interfaces import INamedFileWidget as INamedFileWidget
from plone.formwidget.namedfile.interfaces import INamedImageWidget as INamedImageWidget
from plone.namedfile.file import NamedFile as NamedFile
from plone.namedfile.file import NamedImage as NamedImage
from plone.namedfile.interfaces import INamed as INamed
from plone.namedfile.interfaces import INamedField as INamedField
from plone.namedfile.utils import safe_basename as safe_basename
from z3c.form.converter import BaseDataConverter

class NamedDataConverter(BaseDataConverter):
    def toWidgetValue(self, value): ...
    def toFieldValue(self, value): ...

def b64encode_file(filename, data): ...
def b64decode_file(value): ...

class Base64Converter(BaseDataConverter):
    def toWidgetValue(self, value): ...
    def toFieldValue(self, value): ...
