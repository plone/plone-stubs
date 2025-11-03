from _typeshed import Incomplete
from plone.contentrules.rule.interfaces import IRuleEventType
from zope.componentvocabulary.vocabulary import UtilityVocabulary

_: Incomplete

class EventTypesVocabulary(UtilityVocabulary):
    """A vocabulary for event interfaces that can be selected for the 'event'
    attribute of an IRule.
    An internationalized version of UtilityVocabulary
    """

    interface = IRuleEventType
    nameOnly: Incomplete
    def __init__(self, context, **kw) -> None: ...
