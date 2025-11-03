from _typeshed import Incomplete

class AvailableContentLanguageVocabulary:
    """Vocabulary factory for available content languages in the portal.

    >>> from zope.component import queryUtility
    >>> from plone.app.vocabularies.tests.base import create_context
    >>> from plone.app.vocabularies.tests.base import DummyTool

    >>> name = 'plone.app.vocabularies.AvailableContentLanguages'
    >>> util = queryUtility(IVocabularyFactory, name)
    >>> context = create_context()

    >>> len(util(context))  # 'en' is given as default now
    1

    >>> tool = DummyTool('portal_languages')
    >>> def getAvailableLanguages():
    ...     return dict(en=dict(name='English', native='English'),
    ...                 de=dict(name='German', native='Deutsch'))
    >>> tool.getAvailableLanguages = getAvailableLanguages
    >>> context.portal_languages = tool

    >>> languages = util(context)
    >>> languages
    <zope.schema.vocabulary.SimpleVocabulary object at ...>

    >>> len(languages.by_token)
    2

    >>> de = languages.by_token['de']
    >>> de.title, de.token, de.value
    ('Deutsch', 'de', 'de')
    """
    def __call__(self, context): ...

AvailableContentLanguageVocabularyFactory: Incomplete

class SupportedContentLanguageVocabulary:
    """Vocabulary factory for supported content languages in the portal.

    >>> from zope.component import queryUtility
    >>> from plone.app.vocabularies.tests.base import create_context
    >>> from plone.app.vocabularies.tests.base import DummyTool

    >>> name = 'plone.app.vocabularies.SupportedContentLanguages'
    >>> util = queryUtility(IVocabularyFactory, name)
    >>> context = create_context()

    >>> len(util(context))
    0

    >>> tool = DummyTool('portal_languages')
    >>> def listSupportedLanguages():
    ...     return [('en', 'English'), ('de', 'German')]
    >>> tool.listSupportedLanguages = listSupportedLanguages
    >>> def getAvailableLanguages():
    ...     return dict(en=dict(name='English', native='English'),
    ...                 de=dict(name='German', native='Deutsch'))
    >>> tool.getAvailableLanguages = getAvailableLanguages
    >>> context.portal_languages = tool

    >>> languages = util(context)
    >>> languages
    <zope.schema.vocabulary.SimpleVocabulary object at ...>

    >>> len(languages.by_token)
    2

    >>> de = languages.by_token['de']
    >>> de.title, de.token, de.value
    ('Deutsch', 'de', 'de')
    """
    def __call__(self, context): ...

SupportedContentLanguageVocabularyFactory: Incomplete
