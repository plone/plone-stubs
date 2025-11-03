from _typeshed import Incomplete
from Acquisition import Explicit
from plone.formwidget.namedfile import utils as utils
from plone.formwidget.namedfile.converter import b64decode_file as b64decode_file
from plone.formwidget.namedfile.interfaces import (
    IFileUploadTemporaryStorage as IFileUploadTemporaryStorage,
)
from plone.formwidget.namedfile.interfaces import INamedFileWidget as INamedFileWidget
from plone.formwidget.namedfile.interfaces import INamedImageWidget as INamedImageWidget
from plone.namedfile.browser import Download as DownloadBase
from plone.namedfile.file import NamedBlobFile as NamedBlobFile
from plone.namedfile.file import NamedBlobImage as NamedBlobImage
from plone.namedfile.file import NamedFile as NamedFile
from plone.namedfile.file import NamedImage as NamedImage
from plone.namedfile.interfaces import INamed as INamed
from plone.namedfile.interfaces import INamedBlobFileField as INamedBlobFileField
from plone.namedfile.interfaces import INamedBlobImageField as INamedBlobImageField
from plone.namedfile.interfaces import INamedFileField as INamedFileField
from plone.namedfile.interfaces import INamedImage as INamedImage
from plone.namedfile.interfaces import INamedImageField as INamedImageField
from plone.namedfile.utils import safe_basename as safe_basename
from plone.namedfile.utils import set_headers as set_headers
from plone.namedfile.utils import stream_data as stream_data
from z3c.form.browser.file import FileWidget

class NamedFileWidget(Explicit, FileWidget):
    klass: str
    value: Incomplete
    @property
    def accept(self): ...
    @property
    def is_uploaded(self): ...
    @property
    def file_upload_id(self): ...
    @property
    def allow_nochange(self): ...
    @property
    def filename(self): ...
    @property
    def file_size(self): ...
    @property
    def file_content_type(self): ...
    @property
    def file_icon(self): ...
    @property
    def filename_encoded(self): ...
    @property
    def download_url(self): ...
    def action(self): ...
    def extract(self, default=...): ...

class NamedImageWidget(NamedFileWidget):
    klass: str
    @property
    def width(self): ...
    @property
    def height(self): ...
    @property
    def thumb_tag(self): ...
    @property
    def alt(self): ...

class Download(DownloadBase):
    filename: Incomplete
    def __init__(self, context, request) -> None: ...
    def publishTraverse(self, request, name): ...
    def __call__(self): ...

def NamedFileFieldWidget(field, request): ...
def NamedImageFieldWidget(field, request): ...
