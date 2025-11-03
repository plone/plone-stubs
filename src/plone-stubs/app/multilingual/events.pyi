from _typeshed import Incomplete
from zope.interface.interfaces import IObjectEvent

class IObjectWillBeTranslatedEvent(IObjectEvent):
    """Sent before an object is translated."""

    object: Incomplete
    language: Incomplete

class IObjectTranslatedEvent(IObjectEvent):
    """Sent after an object was translated."""

    object: Incomplete
    target: Incomplete
    language: Incomplete

class ITranslationRegisteredEvent(IObjectEvent):
    """Sent after a new translation was registered.

    This is meant to be notified on low-level manager level only.
    """

    object: Incomplete
    target: Incomplete
    language: Incomplete

class ITranslationUpdatedEvent(IObjectEvent):
    """Sent after an translation was moved to point to a different object

    This is meant to be notified on low-level manager level only.
    """

    object: Incomplete
    old_object: Incomplete
    language: Incomplete

class ITranslationRemovedEvent(IObjectEvent):
    """Sent after an translation was removed.

    This is meant to be notified on low-level manager level only.
    """

    object: Incomplete
    old_object: Incomplete
    language: Incomplete

class ObjectWillBeTranslatedEvent:
    """Sent before an object is translated."""

    object: Incomplete
    language: Incomplete
    def __init__(self, context, language) -> None: ...

class ObjectTranslatedEvent:
    """Sent after an object was translated."""

    object: Incomplete
    target: Incomplete
    language: Incomplete
    def __init__(self, context, target, language) -> None: ...

class TranslationRegisteredEvent:
    """Sent after a new translation was registered."""

    object: Incomplete
    target: Incomplete
    language: Incomplete
    def __init__(self, context, target, language) -> None: ...

class TranslationUpdatedEvent:
    """Sent after an translation was moved to point to a different object"""

    object: Incomplete
    old_object: Incomplete
    language: Incomplete
    def __init__(self, context, old_object, language) -> None: ...

class TranslationRemovedEvent:
    """Sent after an translation was moved to point to a different object"""

    object: Incomplete
    old_object: Incomplete
    language: Incomplete
    def __init__(self, context, old_object, language) -> None: ...
