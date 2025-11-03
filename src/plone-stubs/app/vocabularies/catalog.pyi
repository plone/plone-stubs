from _typeshed import Incomplete
from plone.app.vocabularies import SlicableVocabulary
from plone.memoize.instance import memoize
from zope.interface import Interface

class ISourceQueryView(Interface): ...

def parse_query(query, path_prefix: str = ""):
    """Parse the query string and turn it into a dictionary for querying the
    catalog.

    We want to find anything which starts with the given string, so we add
    a * at the end of words.

    >>> parse_query('foo')
    {'SearchableText': 'foo*'}

    If we have more than one word, each of them should have the * and
    they should be combined with the AND operator.

    >>> parse_query('foo bar')
    {'SearchableText': 'foo* AND bar*'}

    We also filter out some special characters. They are handled like
    spaces and separate words from each other.

    >>> parse_query('foo +bar some-thing')
    {'SearchableText': 'foo* AND bar* AND some* AND thing*'}

    >>> parse_query('what? (spam) *ham')
    {'SearchableText': 'what* AND spam* AND ham*'}

    You can also limit searches to paths, if you only supply the path,
    then all contents of that folder will be searched. If you supply
    additional search words, then all subfolders are searched as well.

    >>> expected = {'path': {'query': '/dummy', 'depth': 1}}
    >>> parse_query('path:/dummy') == expected
    True

    >>> expected = {'path': {'query': '/dummy'}, 'SearchableText': 'bar*'}
    >>> parse_query('bar path:/dummy') == expected
    True

    >>> expected = {'path': {'query': '/dummy'}, 'SearchableText': 'foo*'}
    >>> parse_query('path:/dummy foo') == expected
    True

    If you supply more then one path, then only the last one is used.

    >>> expected = {'path': {'query': '/spam', 'depth': 1}}
    >>> parse_query('path:/dummy path:/spam') == expected
    True

    You can also provide a prefix for the path. This is useful for virtual
    hosting.

    >>> expected = {'path': {'query': '/portal/dummy', 'depth': 1}}
    >>> parse_query('path:/dummy', path_prefix='/portal') == expected
    True

    """

class SearchableTextSource:
    """
    >>> from plone.app.vocabularies.tests.base import DummyCatalog
    >>> from plone.app.vocabularies.tests.base import create_context
    >>> from plone.app.vocabularies.tests.base import DummyTool

    >>> context = create_context()

    >>> catalog = DummyCatalog(('/1234', '/2345'))
    >>> context.portal_catalog = catalog

    >>> tool = DummyTool('portal_url')
    >>> def getPortalPath():
    ...     return '/'
    >>> tool.getPortalPath = getPortalPath
    >>> context.portal_url = tool

    >>> source = SearchableTextSource(context)
    >>> source
    <plone.app.vocabularies.catalog.SearchableTextSource object at ...>

    >>> '1234' in source, '1' in source
    (True, False)

    >>> source.search('')
    []

    >>> source.search('error')
    []

    >>> source.search('foo')
    <generator object ...>

    >>> list(source.search('foo'))
    ['1234', '2345']

    >>> list(source.search('bar path:/dummy'))
    ['/dummy', '1234', '2345']

    >>> u'' in source
    True

    >>> source = SearchableTextSource(context, default_query='default')
    >>> list(source.search(''))
    ['1234', '2345']
    """

    context: Incomplete
    base_query: Incomplete
    default_query: Incomplete
    catalog: Incomplete
    portal_tool: Incomplete
    portal_path: Incomplete
    encoding: str
    def __init__(self, context, base_query={}, default_query=None) -> None: ...
    def __contains__(self, value) -> bool:
        """Return whether the value is available in this source"""
    def search(self, query_string): ...

class SearchableTextSourceBinder:
    """Use this to instantiate a new SearchableTextSource with custom
    parameters. For example:

    target_folder = schema.Choice(
        title=_(u'Target folder'),
        description=_(u'As a path relative to the portal root'),
        required=True,
        source=SearchableTextSourceBinder({'is_folderish' : True}),
        )

    This ensures that the is_folderish=True is always in the query used.

      >>> query = {'query': 'query'}

      >>> binder = SearchableTextSourceBinder(query)
      >>> binder
      <plone.app.vocabularies.catalog.SearchableTextSourceBinder object at ...>

      >>> binder.query == query
      True

      >>> from plone.app.vocabularies.tests.base import create_context
      >>> from plone.app.vocabularies.tests.base import DummyTool

      >>> context = create_context()

      >>> tool = DummyTool('portal_catalog')
      >>> context.portal_catalog = tool

      >>> tool = DummyTool('portal_url')
      >>> def getPortalPath():
      ...     return '/'
      >>> tool.getPortalPath = getPortalPath
      >>> context.portal_url = tool

      >>> source = binder(context)
      >>> source
      <plone.app.vocabularies.catalog.SearchableTextSource object at ...>

      >>> source.base_query == query
      True
    """

    query: Incomplete
    default_query: Incomplete
    def __init__(self, query, default_query=None) -> None: ...
    def __call__(self, context): ...

class QuerySearchableTextSourceView:
    """
    >>> from plone.app.vocabularies.tests.base import DummyCatalog
    >>> from plone.app.vocabularies.tests.base import create_context
    >>> from plone.app.vocabularies.tests.base import DummyTool
    >>> from plone.app.vocabularies.tests.base import Request

    >>> context = create_context()

    >>> rids = (\'/1234\', \'/2345\', \'/dummy/1234\')
    >>> tool = DummyCatalog(rids)
    >>> context.portal_catalog = tool

    >>> tool = DummyTool(\'portal_url\')
    >>> def getPortalPath():
    ...     return \'/dummy\'
    >>> tool.getPortalPath = getPortalPath
    >>> context.portal_url = tool

    >>> source = SearchableTextSource(context)
    >>> source
    <plone.app.vocabularies.catalog.SearchableTextSource object at ...>

    >>> view = QuerySearchableTextSourceView(source, Request())
    >>> view
    <plone.app.vocabularies.catalog.QuerySearchableTextSourceView object ...>

    >>> view.getValue(\'a\')
    Traceback (most recent call last):
    ...
    LookupError: a

    >>> view.getValue(\'/1234\')
    \'/1234\'

    >>> view.getTerm(None) is None
    True

    >>> view.getTerm(\'1234\')
    <plone.app.vocabularies.terms.BrowsableTerm object at ...>

    >>> view.getTerm(\'/1234\')
    <plone.app.vocabularies.terms.BrowsableTerm object at ...>

    >>> template = view.render(name=\'t\')
    >>> u\'<input name="t.query" type="text" value="" />\' in template
    True

    >>> u\'<input name="t.search" type="submit" value="Search" />\' in template
    True

    >>> request = Request(form={\'t.search\' : True, \'t.query\' : \'value\'})
    >>> view = QuerySearchableTextSourceView(source, request)
    >>> sorted(view.results(\'t\'))
    [\'\', \'\', \'/1234\']

    >>> request = Request(form={\'t.search\' : True, \'t.query\' : \'value\',
    ...                         \'t.browse.foo\' : \'/foo\'})
    >>> view = QuerySearchableTextSourceView(source, request)
    >>> sorted(view.results(\'t\'))
    [\'\', \'\', \'/1234\', \'foo\']

    Titles need to be unicode:
    >>> view.getTerm(list(view.results(\'t\'))[0]).title
    \'/foo\'
    """

    template: Incomplete
    context: Incomplete
    request: Incomplete
    def __init__(self, context, request) -> None: ...
    def getTerm(self, value): ...
    def getValue(self, token): ...
    def render(self, name): ...
    def results(self, name): ...

class KeywordsVocabulary:
    """Vocabulary factory listing all catalog keywords from the 'Subject' index

    >>> from plone.app.vocabularies.tests.base import DummyCatalog
    >>> from plone.app.vocabularies.tests.base import create_context
    >>> from plone.app.vocabularies.tests.base import DummyContent
    >>> from plone.app.vocabularies.tests.base import Request
    >>> from Products.PluginIndexes.KeywordIndex.KeywordIndex import KeywordIndex  # noqa

    >>> context = create_context()

    First test bytes vocabularies
    >>> rids = ('/1234', '/2345', '/dummy/1234')
    >>> tool = DummyCatalog(rids)
    >>> context.portal_catalog = tool
    >>> index = KeywordIndex('Subject')
    >>> done = index._index_object(
    ...     1,
    ...     DummyContent('ob1', [b'foo', b'bar', b'baz']), attr='Subject'
    ... )
    >>> done = index._index_object(
    ...     2,
    ...     DummyContent(
    ...         'ob2',
    ...         [b'blee', b'bar', u'non-åscii'.encode('utf8')]),
    ...         attr='Subject',
    ... )
    >>> tool.indexes['Subject'] = index
    >>> vocab = KeywordsVocabulary()
    >>> result = vocab(context)

    Value type is kept ...
    >>> expected = [b'bar', b'baz', b'blee', b'foo', u'non-åscii'.encode('utf8')]
    >>> sorted(result.by_value) == expected
    True

    but tokens are base64 encoded text
    >>> expected = ['YmF6', 'YmFy', 'YmxlZQ==', 'Zm9v', 'bm9uLcOlc2NpaQ==']
    >>> sorted(result.by_token) == expected
    True

    >>> result.getTermByToken(expected[-1]).title == u'non-åscii'
    True

    Testing unicode vocabularies
    First clear the index. Comparing bytes to str objects fails.
    >>> index.clear()
    >>> done = index._index_object(
    ...     1,
    ...     DummyContent('obj1', [u'äüö', u'nix']), attr='Subject'
    ... )
    >>> tool.indexes['Subject'] = index
    >>> vocab = KeywordsVocabulary()
    >>> result = vocab(context)
    >>> expected = ['bml4', 'w6TDvMO2']
    >>> sorted(result.by_token) == expected
    True
    >>> set(result.by_value) == {u'nix', u'äüö'}
    True
    >>> result.getTermByToken(expected[0]).title == u'nix'
    True

    """

    keyword_index: str
    path_index: str
    def section(self, context):
        """gets section from which subjects are used."""
    catalog: Incomplete
    def all_keywords(self, kwfilter): ...
    def keywords_of_section(self, section, kwfilter):
        """Valid keywords under the given section."""
    def __call__(self, context, query=None): ...

KeywordsVocabularyFactory: Incomplete

class CatalogVocabulary(SlicableVocabulary):
    @classmethod
    def fromItems(cls, query, context, *interfaces): ...
    fromValues = fromItems
    @classmethod
    def createTerm(cls, brain, context): ...
    query: Incomplete
    def __init__(self, query, *interfaces) -> None: ...
    @property
    @memoize
    def catalog(self): ...
    @property
    @memoize
    def brains(self): ...
    def __iter__(self): ...
    def __contains__(self, value) -> bool: ...
    def __len__(self) -> int: ...
    def __getitem__(self, index): ...
    def getTerm(self, value): ...
    getTermByToken = getTerm

def request_query_cache_key(func, vocab): ...

class StaticCatalogVocabulary(CatalogVocabulary):
    """Catalog Vocabulary for static queries of content based on a fixed query.
    Intended for use in a zope.schema, e.g.:

        my_relation = RelationChoice(
            title="Custom Relation",
            vocabulary=StaticCatalogVocabulary({
                "portal_type": "Document",
                "review_state": "published",
            })
        )

    Can be used with TextLine values (to store a UUID) or
    Relation/RelationChoice values (to create a z3c.relationfield style
    relation). This vocabulary will work with a variety of selection widgets,
    and provides a text search method to work with the
    plone.app.z3cform.widgets.select.AjaxSelectWidget.

    This vocabulary can be used to make a named vocabulary with a factory
    function:

        from zope.interface import provider
        from zope.schema.interfaces import IVocabularyFactory


        @provider(IVocabularyFactory)
        def my_vocab_factory(context):
            return StaticCatalogVocabulary({
                \'portal_type\': \'Event\',
                \'path\': \'/\'.join(context.getPhysicalPath())
            })

    The default item title looks like "Object Title (/path/to/object)", but this
    can be customized by passing a format string as the "title_template"
    parameter. The format string has "brain" and "path" arguments available:

        MY_VOCABULARY = StaticCatalogVocabulary(
            {\'portal_type\': \'Event\'},
            title_template="{brain.Type}: {brain.Title} at {path}"
        )

    When using this vocabulary for dynamic queries, e.g. with the
    AjaxSelectWidget, you can customize the index searched using the
    "text_search_index" parameter. By default it uses the "SearchableText"
    index, but you could have your vocabulary search on "Title" instead:

        from plone.autoform import directives
        from plone.app.z3cform.widgets.select import AjaxSelectFieldWidget


        directives.widget(
            \'my_relation\',
            AjaxSelectFieldWidget,
            vocabulary=StaticCatalogVocabulary(
                {\'portal_type\': \'Event\'},
                text_search_index="Title",
                title_template="{brain.Type}: {brain.Title} at {path}"
            )
        )

    This vocabulary lazily caches the result set for the base query on the
    request to optimize performance.

    Here are some doctests::

      >>> from plone.app.vocabularies.tests.base import DummyCatalog
      >>> from plone.app.vocabularies.tests.base import create_context
      >>> from plone.app.vocabularies.tests.base import DummyTool

      >>> context = create_context()

      >>> catalog = DummyCatalog((\'/1234\', \'/2345\'))
      >>> context.portal_catalog = catalog

      >>> tool = DummyTool(\'portal_url\')
      >>> def getPortalPath():
      ...     return \'/\'
      >>> tool.getPortalPath = getPortalPath
      >>> context.portal_url = tool

      >>> vocab = StaticCatalogVocabulary({\'portal_type\': [\'Document\']})
      >>> vocab
      <plone.app.vocabularies.catalog.StaticCatalogVocabulary object at ...>

      >>> vocab.search(\'\')
      <zope.schema.vocabulary.SimpleVocabulary object at ...>
      >>> list(vocab.search(\'\'))
      []

      >>> vocab.search(\'foo\')
      <zope.schema.vocabulary.SimpleVocabulary object at ...>

      >>> [(t.title, t.value) for t in vocab.search(\'foo\')]
      [(\'BrainTitle (/1234)\', \'/1234\'), (\'BrainTitle (/2345)\', \'/2345\')]

    We strip out the site path from the rendered path in the title template:

      >>> catalog = DummyCatalog((\'/site/1234\', \'/site/2345\'))
      >>> context.portal_catalog = catalog
      >>> vocab = StaticCatalogVocabulary({\'portal_type\': [\'Document\']})
      >>> [(t.title, t.value) for t in vocab.search(\'bar\')]
      [(\'BrainTitle (/site/1234)\', \'/site/1234\'),
       (\'BrainTitle (/site/2345)\', \'/site/2345\')]

      >>> context.__name__ = \'site\'
      >>> vocab = StaticCatalogVocabulary({\'portal_type\': [\'Document\']})
      >>> [(t.title, t.value) for t in vocab.search(\'bar\')]
      [(\'BrainTitle (/1234)\', \'/site/1234\'),
       (\'BrainTitle (/2345)\', \'/site/2345\')]

    The title template can be customized:

      >>> vocab.title_template = "{url} {brain.UID} - {brain.Title} {path}"
      >>> [(t.title, t.value) for t in vocab.search(\'bar\')]
      [(\'proto:/site/1234 /site/1234 - BrainTitle /1234\', \'/site/1234\'),
       (\'proto:/site/2345 /site/2345 - BrainTitle /2345\', \'/site/2345\')]

    """

    title_template: str
    text_search_index: str
    query: Incomplete
    def __init__(self, query, text_search_index=None, title_template=None) -> None: ...
    @property
    @memoize
    def nav_root_path(self): ...
    def get_brain_path(self, brain): ...
    @staticmethod
    def get_request(): ...
    @property
    def brains(self): ...
    def createTerm(self, brain, context=None): ...
    def search(self, query):
        """Required by plone.app.content.browser.vocabulary for simple queryable
        vocabs, e.g. for AJAXSelectWidget."""

class CatalogSource:
    """Catalog source for use with Choice fields.

    When instantiating the source, you can pass keyword arguments
    which will become the catalog query used to find terms.

    e.g.:

      image = Choice(
          title=u'Image',
          source=CatalogSource(portal_type='Image'),
          )

    The `__contains__` method is used during validation to
    make sure the selected item is found with the specified query.

    The `search_catalog` method is used by plone.app.widgets
    to retrieve catalog brains for this source's query augmented by
    input from the user interacting with the widget.

    Tests:

      >>> from plone.app.vocabularies.tests.base import create_context
      >>> from OFS.SimpleItem import SimpleItem
      >>> class DummyCatalog(SimpleItem):
      ...     def __init__(self, values):
      ...         self.values = values
      ...     def __call__(self, query):
      ...         if 'foo' in query and query['foo'] == 'bar':
      ...             return self.values
      >>> context = create_context()
      >>> context.portal_catalog = DummyCatalog(['asdf'])
      >>> source = CatalogSource(foo='bar')

      >>> 'asdf' in source
      True

      >>> source.search_catalog({'foo': 'baz'})
      ['asdf']

    """

    query: Incomplete
    def __init__(self, context=None, **query) -> None: ...
    def __contains__(self, value) -> bool:
        """used during validation to make sure the selected item is found with
        the specified query.

        value can be either a string (hex value of uuid or path) or a plone
        content object.
        """
    def search_catalog(self, user_query): ...
