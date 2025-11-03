from _typeshed import Incomplete
from persistent import Persistent
from zope.container.contained import Contained
from zope.container.ordered import OrderedContainer

def check_rules_with_dotted_name_moved(rule) -> None:
    """Migrate on-the-fly added event dotted name
    if Plone has been migrated from any release to 4.3 release.
    Avoids any upgrade to fail when setup profile is re-imported.
    """

KEY: str

class RuleAssignment(Contained, Persistent):
    """An assignment of a rule to a context"""

    enabled: Incomplete
    bubbles: Incomplete
    def __init__(self, ruleid, enabled: bool = True, bubbles: bool = False) -> None: ...

class RuleAssignmentManager(OrderedContainer):
    """A context-specific container for rule assignments"""
    def __init__(self) -> None: ...
    def getRules(self, event, bubbled: bool = False): ...

def ruleAssignmentManagerAdapterFactory(context):
    """When adapting an IRuleAssignable, get an IRuleAssignmentManager by
    finding one in the object's annotations. The container will be created
    if necessary.
    """
