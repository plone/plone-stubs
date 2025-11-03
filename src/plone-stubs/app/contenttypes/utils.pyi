from _typeshed import Incomplete
from collections.abc import Generator

logger: Incomplete
DEFAULT_TYPES: Incomplete

def replace_link_variables_by_paths(context, url):
    """Take an `url` and replace the variables "${navigation_root_url}" and
    "${portal_url}" by the corresponding paths. `context` is the acquisition
    context.
    """

def get_old_class_name_string(obj):
    """Returns the current class name string."""

def get_portal_type_name_string(obj):
    """Returns the klass-attribute of the fti."""

def migrate_base_class_to_new_class(
    obj,
    indexes=None,
    old_class_name: str = "",
    new_class_name: str = "",
    migrate_to_folderish: bool = False,
): ...
def list_of_objects_with_changed_base_class(context) -> Generator[Incomplete]: ...
def changed_base_classes(context):
    """Returns dict of current and new class names ."""
