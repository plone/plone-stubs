from _typeshed import Incomplete

HAS_ITERATE: bool
logger: Incomplete
RELATIONS_KEY: str

def rebuild_relations(context=None, flush_and_rebuild_intids: bool = False) -> None: ...
def get_relations_stats(): ...
def get_all_relations():
    """Get relations from zc.relation catalog.

    Log statistics.
    Return list of dictionaries:
        from_uuid: source UID if available else None
        to_uuid: target UID if available else None
        from_attribute: relation name
    """

def store_relations(context=None) -> None:
    """Store all relations in a annotation on the portal."""

def purge_relations(context=None) -> None:
    """Removes all entries form zc.relation catalog.

    RelationValues that were set as attribute on content are still there!
    These are removed/overwritten when restoring the relations.
    """

def restore_relations(context=None, all_relations=None) -> None:
    """Restore relations from an annotation on the portal."""

def log_relations() -> None: ...
def get_intid(obj):
    """Intid from intid-catalog"""

def get_field_and_schema_for_fieldname(field_id, portal_type):
    """Get field and its schema from a portal_type."""

def cleanup_intids(context=None) -> None: ...
def flush_intids() -> None:
    """Flush all intIds"""

def rebuild_intids() -> None:
    """Create new intIds"""
