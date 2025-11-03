from _typeshed import Incomplete
from OFS.SimpleItem import SimpleItem

product_dir: Incomplete
product_prefix: Incomplete
logger: Incomplete

class PluginRegistry(SimpleItem):
    """Implement IPluginRegistry as an independent, ZMI-manageable object.

    o Each plugin type holds an ordered list of (id, wrapper) tuples.
    """

    security: Incomplete
    meta_type: str
    zmi_icon: str
    def __init__(self, plugin_type_info=()) -> None: ...
    def listPluginTypeInfo(self):
        """See IPluginRegistry."""
    def listPlugins(self, plugin_type):
        """See IPluginRegistry."""
    def getPluginInfo(self, plugin_type):
        """See IPluginRegistry."""
    def listPluginIds(self, plugin_type):
        """See IPluginRegistry."""
    def activatePlugin(self, plugin_type, plugin_id) -> None:
        """See IPluginRegistry."""
    def deactivatePlugin(self, plugin_type, plugin_id) -> None:
        """See IPluginRegistry."""
    def movePluginsTop(self, plugin_type, ids_to_move) -> None:
        """See IPluginRegistry."""
    def movePluginsUp(self, plugin_type, ids_to_move) -> None:
        """See IPluginRegistry."""
    def movePluginsDown(self, plugin_type, ids_to_move) -> None:
        """See IPluginRegistry."""
    arrow_right_gif: Incomplete
    arrow_left_gif: Incomplete
    arrow_up_gif: Incomplete
    arrow_down_gif: Incomplete
    def manage_activatePlugins(self, plugin_type, plugin_ids, RESPONSE) -> None:
        """Shim into ZMI."""
    def manage_deactivatePlugins(self, plugin_type, plugin_ids, RESPONSE) -> None:
        """Shim into ZMI."""
    def manage_movePluginsUp(self, plugin_type, plugin_ids, RESPONSE) -> None:
        """Shim into ZMI."""
    def manage_movePluginsDown(self, plugin_type, plugin_ids, RESPONSE) -> None:
        """Shim into ZMI."""
    def getAllPlugins(self, plugin_type):
        """Return a mapping segregating active / available plugins.

        'plugin_type' is the __name__ of the interface.
        """
    def removePluginById(self, plugin_id) -> None:
        """Remove a plugin from any plugin types which have it configured."""
    manage_plugins: Incomplete
    manage_active: Incomplete
    manage_twoLists: Incomplete
    manage_options: Incomplete
    manage_exportImportForm: Incomplete
    def getConfigAsXML(self):
        """Return XML representing the registry's configuration."""
    def manage_exportImport(self, updated_xml, should_purge, RESPONSE) -> None:
        """Parse XML and update the registry."""
    def manage_FTPget(self, REQUEST, RESPONSE):
        """ """
    def PUT(self, REQUEST, RESPONSE) -> None:
        """ """

def emptyPluginRegistry(ignored):
    """Return empty registry, for filling from setup profile."""
