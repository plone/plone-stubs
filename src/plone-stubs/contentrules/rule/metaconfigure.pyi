def ruleConditionDirective(
    _context,
    name,
    title,
    addview,
    editview=None,
    description: str = "",
    for_=...,
    event=...,
    schema=None,
    factory=None,
) -> None:
    """Register a utility for IRuleCondition based on the parameters in the
    zcml directive
    """

def ruleActionDirective(
    _context,
    name,
    title,
    addview,
    editview=None,
    description: str = "",
    for_=...,
    event=...,
    schema=None,
    factory=None,
) -> None:
    """Register a utility for IRuleAction based on the parameters in the
    zcml directive
    """
