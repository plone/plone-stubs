from .utils import ImportConfiguratorBase

METADATA_XML: str

class ProfileMetadata(ImportConfiguratorBase):
    """Extracts profile metadata from metadata.xml file."""
    def __init__(self, path, encoding=None, product=None) -> None: ...
    def __call__(self): ...
