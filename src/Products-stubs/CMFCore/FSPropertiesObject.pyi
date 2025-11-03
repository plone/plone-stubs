from .FSObject import FSObject
from _typeshed import Incomplete
from OFS.PropertyManager import PropertyManager

class FSPropertiesObject(FSObject, PropertyManager):
    """FSPropertiesObjects simply hold properties."""

    meta_type: str
    manage_options: Incomplete
    security: Incomplete
    manage_main: Incomplete
    def manage_doCustomize(
        self, folder_path, RESPONSE=None, root=None, obj=None
    ) -> None:
        """Makes a ZODB Based clone with the same data.

        Calls _createZODBClone for the actual work.
        """
    def __of__(self, parent): ...
