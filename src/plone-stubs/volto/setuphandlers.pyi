from _typeshed import Incomplete

HAS_MULTILINGUAL: bool
NO_RICHTEXT_BEHAVIOR_CONTENT_TYPES: Incomplete

class HiddenProfiles:
    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller"""

def post_install(context) -> None:
    """Post install script"""

def uninstall(context) -> None:
    """Uninstall script"""

def post_install_coresandbox(context) -> None:
    """Post install script for multilingual fixture"""

def post_install_multilingual(context) -> None:
    """Post install script for multilingual fixture"""

def enable_pam(portal) -> None: ...
def ensure_pam_consistency(portal) -> None:
    """Makes sure that all the content in a language branch has language"""

def change_content_type_title(portal, old_name, new_name) -> None:
    """
    change_content_type_title(portal, 'News Item', 'Meldung')
    """

def disable_content_type(portal, fti_id) -> None: ...
def enable_content_type(portal, fti_id) -> None: ...
def copy_content_type(portal, name, newid, newname) -> None:
    """Create a new content type by copying an existing one"""

def add_catalog_indexes(context, wanted=None) -> None:
    """Method to add our wanted indexes to the portal_catalog."""

def add_behavior(portal_type, behavior) -> None: ...
def remove_behavior(portal_type, behavior) -> None: ...
