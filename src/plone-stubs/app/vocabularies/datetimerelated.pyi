from _typeshed import Incomplete

PLMF: Incomplete

def TimezonesFactory(context, query=None):
    """Vocabulary for all timezones.

    This are all timezones supported by pytz.
    """

def CommonTimezonesFactory(context, query=None):
    """Vocabulary for common timezones.

    This are the timezones a user would choose from in a form.
    """

def AvailableTimezonesFactory(context, query=None):
    """Vocabulary for available timezones, as set by in the controlpanel."""

WEEKDAY_PREFIXES: Incomplete

def WeekdaysFactory(context):
    """Vocabulary for Weekdays - full name

    Usage:
    ------

    Get vocabulary for all seven days:

        >>> from zope.component import queryUtility
        >>> from plone.app.vocabularies.tests.base import create_context

        >>> name = 'plone.app.vocabularies.Weekdays'
        >>> util = queryUtility(IVocabularyFactory, name)
        >>> context = create_context()

        >>> len(util(context))
        7

    Containment is unenforced, as numeric tokens are used, a permissive
    vocabulary type is in use (to make GenericSetup profile
    import happy):

        >>> assert '1' in util(context)
        >>> assert 1 in util(context)

    Term values are all integers:

        >>> assert all(map(lambda t: type(t.value) is int, util(context)))

    Term titles are i18n labels:

        >>> util(context).by_token['0'].title
        u'weekday_mon'
    """

def WeekdaysAbbrFactory(context):
    """Vocabulary for Weekdays - abbreviated (3 char)

    Usage:
    ------

    Get vocabulary for all seven days:

        >>> from zope.component import queryUtility
        >>> from plone.app.vocabularies.tests.base import create_context

        >>> name = 'plone.app.vocabularies.WeekdaysAbbr'
        >>> util = queryUtility(IVocabularyFactory, name)
        >>> context = create_context()

        >>> len(util(context))
        7

    Containment is unenforced, as numeric tokens are used, a permissive
    vocabulary type is in use (to make GenericSetup profile
    import happy):

        >>> assert '1' in util(context)
        >>> assert 1 in util(context)

    Term values are all integers:

        >>> assert all(map(lambda t: type(t.value) is int, util(context)))

    Term titles are i18n labels:

        >>> util(context).by_token['0'].title
        u'weekday_mon_abbr'
    """

def WeekdaysShortFactory(context):
    """Vocabulary for Weekdays - Short (2 char)

    Usage:
    ------

    Get vocabulary for all seven days:

        >>> from zope.component import queryUtility
        >>> from plone.app.vocabularies.tests.base import create_context

        >>> name = 'plone.app.vocabularies.WeekdaysShort'
        >>> util = queryUtility(IVocabularyFactory, name)
        >>> context = create_context()

        >>> len(util(context))
        7

    Containment is unenforced, as numeric tokens are used, a permissive
    vocabulary type is in use (to make GenericSetup profile
    import happy):

        >>> assert '1' in util(context)
        >>> assert 1 in util(context)

    Term values are all integers:

        >>> assert all(map(lambda t: type(t.value) is int, util(context)))

    Term titles are i18n labels:

        >>> util(context).by_token['0'].title
        u'weekday_mon_short'
    """

MONTH_PREFIXES: Incomplete

def MonthFactory(context):
    """Vocabulary for Month. Full name

    Usage:

        >>> from zope.component import queryUtility
        >>> from plone.app.vocabularies.tests.base import create_context

        >>> name = 'plone.app.vocabularies.Month'
        >>> util = queryUtility(IVocabularyFactory, name)
        >>> context = create_context()

        >>> len(util(context))
        12

    Containment is unenforced, as numeric tokens are used, a permissive
    vocabulary type is in use (to make GenericSetup profile
    import happy):

        >>> assert '1' in util(context)
        >>> assert 1 in util(context)

    Term values are all integers:

        >>> assert all(map(lambda t: type(t.value) is int, util(context)))
    """

def MonthAbbrFactory(context):
    """Vocabulary for Month. Abbreviated Name (3 char)

    Usage:

        >>> from zope.component import queryUtility
        >>> from plone.app.vocabularies.tests.base import create_context

        >>> name = 'plone.app.vocabularies.MonthAbbr'
        >>> util = queryUtility(IVocabularyFactory, name)
        >>> context = create_context()

        >>> len(util(context))
        12

    Containment is unenforced, as numeric tokens are used, a permissive
    vocabulary type is in use (to make GenericSetup profile
    import happy):

        >>> assert '1' in util(context)
        >>> assert 1 in util(context)

    Term values are all integers:

        >>> assert all(map(lambda t: type(t.value) is int, util(context)))
    """
