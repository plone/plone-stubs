from _typeshed import Incomplete

class SerializeVocabLikeToJson:
    """Base implementation to serialize vocabularies and sources to JSON.

    Implements server-side filtering as well as batching.
    """

    context: Incomplete
    request: Incomplete
    def __init__(self, context, request) -> None: ...
    def __call__(self, vocabulary_id): ...

class SerializeVocabularyToJson(SerializeVocabLikeToJson):
    """Serializes IVocabulary to JSON."""

class SerializeSourceToJson(SerializeVocabLikeToJson):
    """Serializes IIterableSource to JSON."""

class SerializeTermToJson:
    context: Incomplete
    request: Incomplete
    def __init__(self, context, request) -> None: ...
    def __call__(self): ...
