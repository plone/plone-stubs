def reindex_language_independent(ob, event) -> None:
    """Re-index language independent object for other languages

    Language independent objects are indexed once for each language with
    different, language code post-fixed, UUID for each. When ever a language
    independent object is modified in some language, it must be re-indexed
    for all the other languages as well.

    """

def unindex_language_independent(ob, event) -> None:
    """Un-index language independent object for other languages

    Language independent objects are indexed once for each language with
    different, language code post-fixed, UUID for each. When ever a language
    independent object is removed in some language, we must un-indexed
    all the other languages as well.

    XXX: Removing any language independent folder will unindex contents of
    all language independent folders. When that happens, catalog clear
    and rebuild would restore contenst for the other folders.

    """

def reindex_object(obj) -> None: ...
def set_recursive_language(ob, language) -> None:
    """Set the language for this object and its children in a recursive
    manner

    """

def createdEvent(obj, event) -> None:
    """Subscriber to set language on the child folder

    It can be a
    - IObjectRemovedEvent - don't do anything
    - IObjectMovedEvent
    - IObjectAddedEvent
    - IObjectCopiedEvent
    """

def change_language_settings(proxy, settings) -> None: ...
