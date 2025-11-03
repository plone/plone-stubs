def assign_rule(
    container, rule_id, enabled: bool = True, bubbles: bool = True, insert_before=None
) -> None:
    """Assign
       @param string rule_id
       rule to
       @param object container
    with options
       @param bool enabled
       @param bool bubbles (apply in subfolders)
       @param string insert-before
    """

def unassign_rule(container, rule_id) -> None:
    """Remove
    @param string rule_id
    rule from
    @param object container
    """

def edit_rule_assignment(container, rule_id, bubbles=None, enabled=None) -> None:
    """Change a property of an assigned rule
    @param object container
    @param string rule_id
    @param bool enabled
    @param bool bubbles (apply in subfolders)
    """
