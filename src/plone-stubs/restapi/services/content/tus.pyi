from _typeshed import Incomplete
from plone.restapi.services import Service

TUS_OPTIONS_RESPONSE_HEADERS: Incomplete

class UploadOptions(Service):
    """TUS upload endpoint for handling OPTIONS requests without CORS."""
    def reply(self): ...

class TUSBaseService(Service):
    def __call__(self): ...
    def check_tus_version(self): ...
    def unsupported_version(self): ...
    def error(self, type, message, status: int = 400):
        """
        Set a status code (400 is the default error in the TUS
        reference server implementation) and return a plone.restapi
        conform error body.
        """

class UploadPost(TUSBaseService):
    """TUS upload endpoint for creating a new upload resource."""
    def reply(self): ...

class UploadFileBase(TUSBaseService):
    uid: Incomplete
    def __init__(self, context, request) -> None: ...
    def publishTraverse(self, request, name): ...
    def tus_upload(self): ...
    def check_add_modify_permission(self, mode) -> None: ...

class UploadHead(UploadFileBase):
    """TUS upload endpoint for handling HEAD requests"""
    def reply(self): ...

class UploadPatch(UploadFileBase):
    """TUS upload endpoint for handling PATCH requests"""
    def reply(self): ...
    def create_or_modify_content(self, tus_upload): ...

class TUSUpload:
    file_prefix: str
    expiration_period: Incomplete
    finished: bool
    uid: Incomplete
    tmp_dir: Incomplete
    filepath: Incomplete
    metadata_path: Incomplete
    def __init__(self, uid, metadata=None) -> None: ...
    def initialize(self, metadata) -> None:
        """Initialize a new TUS upload by writing its metadata to disk."""
    def length(self):
        """Returns the total upload length."""
    def offset(self):
        """Returns the current offset."""
    def write(self, infile, offset: int = 0) -> None:
        """Write to uploaded file at the given offset."""
    def open(self):
        """Open the uploaded file for reading and return it."""
    def close(self) -> None:
        """Close the uploaded file."""
    def metadata(self):
        """Returns the metadata of the current upload."""
    def cleanup(self) -> None:
        """Remove temporary upload files."""
    def cleanup_expired(self) -> None:
        """Cleanup unfinished uploads that have expired."""
    def expires(self):
        """Returns the expiration time of the current upload."""
