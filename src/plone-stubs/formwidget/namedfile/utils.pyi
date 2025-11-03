from _typeshed import Incomplete
from plone.base.interfaces import IImagingSchema as IImagingSchema
from plone.formwidget.namedfile.interfaces import (
    IFileUploadTemporaryStorage as IFileUploadTemporaryStorage,
)
from plone.registry.interfaces import IRegistry as IRegistry

FILE_UPLOAD_MAP_KEY: str
FILE_UPLOAD_EXPIRATION_TIME: Incomplete
FALLBACK_DATE: Incomplete
CLEANUP_INTERVAL: int

def is_file_upload(item): ...

class FileUploadTemporaryStorage:
    context: Incomplete
    def __init__(self, context) -> None: ...
    @property
    def upload_map(self): ...
    def cleanup(self, force: bool = False) -> None: ...

def get_scale_infos(): ...
