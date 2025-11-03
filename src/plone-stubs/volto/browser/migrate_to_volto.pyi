from _typeshed import Incomplete
from Products.Five import BrowserView

logger: Incomplete

class MigrateToVolto(BrowserView):
    """Basically a configurable upgrade-step to prepare a existing site for Volto."""

    service_url: Incomplete
    migrate_folders: Incomplete
    migrate_default_pages: Incomplete
    purge_richtext: Incomplete
    slate: Incomplete
    def __call__(self): ...
    def install_plone_volto(self) -> None: ...
    def migrate_to_folderish(self) -> None:
        """Migrate default itemish content to folderish"""
    def do_migrate_folders(self) -> None:
        """Migrate Folders to FolderisDocument."""
    def migrate_collections(self) -> None:
        """Migrate Collections to FolderisDocument with Listing Blocks
        Collections that are default pages are already removed when this runs.
        """
    def do_migrate_default_page(self, obj):
        """This assumes the obj is already a FolderishDocument"""
    def convert_richtext(self) -> None:
        """Get richtext for all content that has it and set as blocks."""
    def installed_addons(self): ...

def generate_listing_block(obj): ...
def generate_listing_block_from_collection(obj, move_relative_path: bool = False):
    """Transform collection query and setting to listing block."""

def make_document(
    obj, service_url: str = "http://localhost:5000/html", slate: bool = True
):
    """Convert any item to a FolderishDocument"""

def export_relations(obj): ...
