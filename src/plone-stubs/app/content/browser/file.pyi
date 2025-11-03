from _typeshed import Incomplete
from Products.Five.browser import BrowserView

logger: Incomplete
possible_tus_options: Incomplete
TUS_ENABLED: bool
tus_settings: Incomplete
name: Incomplete
tmp_file_dir: Incomplete

class FileUploadView(BrowserView):
    """
    Handle file uploads with potential
    special handling of TUS resumable uploads
    """

    tus_uid: Incomplete
    def __contains__(self, uid) -> bool: ...
    __doc__: str
    def __getitem__(self, uid): ...
    def __call__(self): ...

class AllowUploadView(BrowserView):
    def __call__(self):
        """Return JSON structure to indicate if File or Image uploads are
        allowed in the current container.
        """
