from _typeshed import Incomplete

PMF: Incomplete

class RolesVocabulary:
    """Vocabulary factory for roles in the portal

    >>> from zope.component import queryUtility
    >>> from plone.app.vocabularies.tests.base import create_context
    >>> from plone.app.vocabularies.tests.base import DummyTool

    >>> name = 'plone.app.vocabularies.Roles'
    >>> util = queryUtility(IVocabularyFactory, name)
    >>> context = create_context()

    >>> len(util(context))
    0

    >>> tool = DummyTool('portal_membership')
    >>> def getPortalRoles():
    ...    return ('Anonymous', 'Authenticated', 'Manager', 'Ploonies')
    >>> tool.getPortalRoles = getPortalRoles
    >>> context.portal_membership = tool

    >>> roles = util(context)
    >>> roles
    <zope.schema.vocabulary.SimpleVocabulary object at ...>

    >>> len(roles.by_token)
    4

    >>> manager = roles.by_token['Manager']
    >>> manager.title, manager.token, manager.value
    (u'Manager', 'Manager', 'Manager')
    """
    def __call__(self, context): ...

RolesVocabularyFactory: Incomplete

class PermissionsVocabulary:
    """Vocabulary factory for permissions."""
    def __call__(self, context): ...

PermissionsVocabularyFactory: Incomplete
