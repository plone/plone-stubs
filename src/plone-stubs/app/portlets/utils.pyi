from _typeshed import Incomplete

def assignment_mapping_from_key(
    context, manager_name, category, key, create: bool = False
):
    """Given the name of a portlet manager, the name of a category, and a
    key in that category, return the IPortletAssignmentMapping.
    Raise a KeyError if it cannot be found.
    """

def assignment_from_key(context, manager_name, category, key, name):
    """Given the name of a portlet manager, the name of a category, a
    key in that category and the name of a particular assignment, return
    the IPortletAssignment. Raise a KeyError if it cannot be found.
    """

DONT_MIGRATE: Incomplete

def convert_legacy_portlets(context) -> None:
    """Convert legacy portlets (left_slots, right_slots) in the given
    context to new-style portlets.
    """
