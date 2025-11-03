from _typeshed import Incomplete

def getAllowedContentTypes(context):
    """computes the list of allowed content types ...
    Here the mime types allowed in text fields are meant.

    It does so by subtracting the site property blacklist from the list of
    allowable (overall available) types.
    """

def getAllowableContentTypes(context):
    """retrieves the list of available content types (aka mime-types) ...

    ... by querying portal transforms.

    Cite from over there:
    This returns a list of mimetypes that can be used as input for textfields
    by building a list of the inputs beginning with "text/" of all
    transforms.
    """

def getForbiddenContentTypes(context):
    """Get forbidden contenttypes.

    This is a list of mime-types not allowed in text input fields.

    We used to get this from
    portal_properties.site_properties.forbidden_contenttypes
    Maybe we should have moved this to portal_registry, but no-one did.
    """

class AllowableContentTypesVocabulary:
    """Vocabulary factory for allowable content types.

    A list of mime-types that can be used as input for textfields.

      >>> from zope.component import queryUtility
      >>> from plone.app.vocabularies.tests.base import create_context
      >>> from plone.app.vocabularies.tests.base import DummyTool

      >>> name = 'plone.app.vocabularies.AllowableContentTypes'
      >>> util = queryUtility(IVocabularyFactory, name)
      >>> context = create_context()

      >>> tool = DummyTool('portal_transforms')
      >>> def listAvailableTextInputs():
      ...     return ('text/plain', 'text/spam')
      >>> tool.listAvailableTextInputs = listAvailableTextInputs
      >>> context.portal_transforms = tool

      >>> types = util(context)
      >>> types
      <zope.schema.vocabulary.SimpleVocabulary object at ...>

      >>> len(types.by_token)
      2

      >>> doc = types.by_token['text/plain']
      >>> doc.title, doc.token, doc.value
      ('text/plain', 'text/plain', 'text/plain')
    """
    def __call__(self, context): ...

AllowableContentTypesVocabularyFactory: Incomplete

class AllowedContentTypesVocabulary:
    """Vocabulary factory for allowed content types.

    A list of mime-types that is allowed to be used as input for textfields.

      >>> from zope.component import queryUtility
      >>> from plone.app.vocabularies.tests.base import create_context
      >>> from plone.app.vocabularies.tests.base import DummyTool

      >>> name = 'plone.app.vocabularies.AllowedContentTypes'
      >>> util = queryUtility(IVocabularyFactory, name)
      >>> context = create_context()

      >>> tool = DummyTool('portal_transforms')
      >>> def listAvailableTextInputs():
      ...     return ('text/plain', 'text/spam')
      >>> tool.listAvailableTextInputs = listAvailableTextInputs
      >>> context.portal_transforms = tool
      >>> types = util(context)
      >>> types
      <zope.schema.vocabulary.SimpleVocabulary object at ...>

      >>> len(types.by_token)
      2

      >>> doc = types.by_token['text/plain']
      >>> doc.title, doc.token, doc.value
      ('text/plain', 'text/plain', 'text/plain')
    """
    def __call__(self, context): ...

AllowedContentTypesVocabularyFactory: Incomplete

class PortalTypesVocabulary:
    """Vocabulary factory for portal types.

    >>> from zope.component import queryUtility
    >>> from plone.app.vocabularies.tests.base import create_context
    >>> from plone.app.vocabularies.tests.base import DummyTypeTool

    >>> name = 'plone.app.vocabularies.PortalTypes'
    >>> util = queryUtility(IVocabularyFactory, name)
    >>> context = create_context()

    >>> context.portal_types = DummyTypeTool()
    >>> types = util(context)
    >>> types
    <zope.schema.vocabulary.SimpleVocabulary object at ...>

    >>> len(types.by_token)
    2

    >>> doc = types.by_token['Document']
    >>> doc.title, doc.token, doc.value
    (u'Page', 'Document', 'Document')
    """
    def __call__(self, context): ...

PortalTypesVocabularyFactory: Incomplete

class UserFriendlyTypesVocabulary:
    """Vocabulary factory for user friendly portal types.

    >>> from zope.component import queryUtility
    >>> from plone.app.vocabularies.tests.base import create_context
    >>> from plone.app.vocabularies.tests.base import DummyTool
    >>> from plone.app.vocabularies.tests.base import DummyTypeTool

    >>> name = 'plone.app.vocabularies.UserFriendlyTypes'
    >>> util = queryUtility(IVocabularyFactory, name)
    >>> context = create_context()

    >>> context.portal_types = DummyTypeTool()
    >>> tool = DummyTool('plone_utils')
    >>> def getUserFriendlyTypes():
    ...     return ('Document', )
    >>> tool.getUserFriendlyTypes = getUserFriendlyTypes
    >>> context.plone_utils = tool

    >>> types = util(context)
    >>> types
    <zope.schema.vocabulary.SimpleVocabulary object at ...>

    >>> len(types.by_token)
    1

    >>> doc = types.by_token['Document']
    >>> doc.title, doc.token, doc.value
    (u'Page', 'Document', 'Document')
    """
    def __call__(self, context): ...

UserFriendlyTypesVocabularyFactory: Incomplete
BAD_TYPES: Incomplete

class ReallyUserFriendlyTypesVocabulary:
    """Vocabulary factory for really user friendly portal types.

    Usage:

        >>> from zope.component import queryUtility
        >>> from plone.app.vocabularies.tests.base import create_context
        >>> from plone.app.vocabularies.tests.base import DummyType
        >>> from plone.app.vocabularies.tests.base import DummyTypeTool

        >>> name = 'plone.app.vocabularies.ReallyUserFriendlyTypes'
        >>> util = queryUtility(IVocabularyFactory, name)
        >>> context = create_context()

        >>> tool = DummyTypeTool()
        >>> tool['ATBooleanCriterion'] = DummyType('Boolean Criterion')
        >>> context.portal_types = tool

        >>> types = util(context)
        >>> types
        <plone.app.vocabularies.PermissiveVocabulary object at ...>

        >>> len(types.by_token)
        2

    Containment is unenforced, to make GenericSetup import validation
    handle validation triggered by Choice.fromUnicode() on insertion:

        >>> non_friendly_type = types.getTermByToken('Plone Site')
        >>> non_friendly_type.title, non_friendly_type.token
        ('Plone Site', 'Plone Site')

        >>> doc = types.by_token['Document']
        >>> doc.title, doc.token, doc.value
        ('Page', 'Document', 'Document')
    """
    def __call__(self, context): ...

ReallyUserFriendlyTypesVocabularyFactory: Incomplete
