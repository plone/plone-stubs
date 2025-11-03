from _typeshed import Incomplete
from z3c.form.interfaces import IWidget
from zope.interface import Interface

class INamedFileWidget(IWidget):
    allow_nochange: Incomplete
    filename: Incomplete
    filename_encoded: Incomplete
    file_size: Incomplete
    download_url: Incomplete

class INamedImageWidget(INamedFileWidget):
    width: Incomplete
    height: Incomplete
    thumb_tag: Incomplete
    alt: Incomplete

class IFileUploadTemporaryStorage(Interface):
    upload_map: Incomplete
    def cleanup() -> None: ...

class IScaleGenerateOnSave(Interface): ...
