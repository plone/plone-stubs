from zope.schema.vocabulary import SimpleVocabulary

class SlicableVocabulary:
    """
    A tokenized vocabulary in which the results can be sliced.
    This class does not implement a complete vocabulary. Instead you use
    this class as a mixin to your vocabulary class.
    This mixin class expects to be used with something resembling
    a SimpleVocabulary. It accesses internal members like _terms
    """
    def __init__(self, terms=[], *interfaces) -> None: ...
    def __getitem__(self, start, stop=None): ...
    def __len__(self) -> int: ...

class PermissiveVocabulary(SimpleVocabulary):
    """
    Permissive vocabulary for cases of integer-keyed choices or cases
    where vocabulary may mutate later in a transaction to include a
    newly inserted value.
    """
    def __contains__(self, value) -> bool: ...
    def getTermByToken(self, token):
        """
        this works around z3c.form.widget.SequenceWidget.extract()
        pseudo-validation (which is broken for a permissive vocabulary).
        """
