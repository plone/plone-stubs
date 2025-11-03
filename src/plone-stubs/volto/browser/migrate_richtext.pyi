from _typeshed import Incomplete
from Products.Five import BrowserView

logger: Incomplete

class MigrateRichTextToVoltoBlocks(BrowserView):
    """Form to trigger migrating html from Richxtext fields to slate."""

    service_url: Incomplete
    purge_richtext: Incomplete
    portal_types: Incomplete
    portal_types_info: Incomplete
    slate: Incomplete
    def __call__(self): ...
    def types_with_blocks(self):
        """A list with info on all content types with existing items."""

def migrate_richtext_to_blocks(
    portal_types=None,
    service_url: str = "http://localhost:5000/html",
    fieldname: str = "text",
    purge_richtext: bool = False,
    slate: bool = True,
): ...
def get_blocks_from_richtext(
    text, service_url: str = "http://localhost:5000/html", slate: bool = True
): ...
def types_with_blocks():
    """A list of content types with volto.blocks behavior."""
