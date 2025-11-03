from _typeshed import Incomplete

JOIN_CONST: Incomplete

class UserRegistrationFieldsVocabulary:
    """Returns list of fields available for registration form.

    It gets fields from z3c.form adopted Registration form schema.
    FormExtender fields are not included.

      >>> from zope.component import queryUtility
      >>> from zope.schema.interfaces import IVocabularyFactory

      >>> name = 'plone.app.users.user_registration_fields'
      >>> util = queryUtility(IVocabularyFactory, name)

      >>> fields = util(None)
      >>> fields
      <zope.schema.vocabulary.SimpleVocabulary object at ...>

      >>> len(fields.by_token)
      10
      >>> values = [k.value for k in fields]
      >>> sorted(values)
      ['description', 'email', 'fullname', 'home_page', 'location', 'mail_me', 'password', 'password_ctl', 'portrait', 'username']

      >>> email = fields.by_token['email']
      >>> email.title, email.token, email.value
      ('email', 'email', 'email')

    """
    def __call__(self, context): ...

UserRegistrationFieldsVocabularyFactory: Incomplete

class GroupIdVocabulary:
    """
    Return vocab of groups to add new user to.

      >>> from zope.component import queryUtility
      >>> from zope.schema.interfaces import IVocabularyFactory
      >>> from Products.CMFPlone.utils import get_portal
      >>> from Products.CMFCore.utils import getToolByName

      >>> groups_tool = getToolByName(get_portal(), \'portal_groups\')
      >>> groups_tool.addGroup(
      ...     \'fancygroup\', [], [],
      ...     title=\'Group Title\',
      ...     description="Group Description",
      ... )
      True

      >>> name = \'plone.app.users.group_ids\'
      >>> util = queryUtility(IVocabularyFactory, name)

      >>> fields = util(get_portal())
      >>> fields
      <zope.schema.vocabulary.SimpleVocabulary object at ...>

      >>> [k.value for k in fields] # doctest: +NORMALIZE_WHITESPACE
      [\'fancygroup\', \'Reviewers\', \'Site Administrators\']
      >>> [k.title for k in fields] # doctest: +NORMALIZE_WHITESPACE
      [\'Group Title (fancygroup)\', \'Reviewers\', \'Site Administrators\']

    """
    def __call__(self, context): ...

GroupIdVocabularyFactory: Incomplete
