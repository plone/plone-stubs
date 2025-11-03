class CatalogVocabularyFactory:
    """
    Test application of Navigation Root:

      >>> from plone.app.vocabularies.tests.base import create_context
      >>> from plone.app.vocabularies.tests.base import DummyUrlTool
      >>> from plone.app.vocabularies.tests.base import DummyCatalog
      >>> class DummyPathCatalog(DummyCatalog):
      ...     def __call__(self, **query):
      ...         if 'path' in query and 'query' in query['path']:
      ...             return [v for v in self.values() if
      ...                     v.getPath().startswith(query['path']['query'])]
      ...         return self.values()
      >>> catalog = DummyPathCatalog(['/abcd', '/defg', '/dummy/sub-site',
      ...                             '/dummy/sub-site/ghij'])
      >>> context = create_context()
      >>> context.portal_catalog = catalog
      >>> context.portal_url = DummyUrlTool(context)
      >>> factory = CatalogVocabularyFactory()

      >>> sorted(t.token for t in factory(context))
      ['/abcd', '/defg', '/dummy/sub-site', '/dummy/sub-site/ghij']

      >>> from plone.app.vocabularies.tests.base import DummyNavRoot
      >>> nav_root = DummyNavRoot('sub-site', parent=context)
      >>> [t.token for t in factory(nav_root)]
      ['/dummy/sub-site', '/dummy/sub-site/ghij']

    """
    def __call__(self, context, query=None): ...
