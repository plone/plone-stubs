from _typeshed import Incomplete

class MetaDataFieldsVocabulary:
    """Vocabulary factory for metadata fields

    >>> from zope.component import queryUtility
    >>> from plone.app.vocabularies.tests.base import DummyCatalog
    >>> from plone.app.vocabularies.tests.base import create_context

    >>> context = create_context()

    >>> catalog = DummyCatalog(())
    >>> catalog.schema = lambda: ['ModificationDate', 'review_state', 'SomethingNew']
    >>> context.portal_catalog = catalog

    >>> name = 'plone.app.vocabularies.MetadataFields'
    >>> util = queryUtility(IVocabularyFactory, name)

    >>> fields = util(context)
    >>> fields
    <zope.schema.vocabulary.SimpleVocabulary object at ...>

    >>> len(fields.by_token)
    3

    >>> modification_date = fields.by_token['ModificationDate']
    >>> modification_date.title, modification_date.token, modification_date.value
    (u'Last modified', 'ModificationDate', 'ModificationDate')
    """
    def __call__(self, context): ...

MetaDataFieldsVocabularyFactory: Incomplete

def get_field_label(field): ...
