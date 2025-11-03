from _typeshed import Incomplete
from zope.interface import Interface

class ISourceQueryView(Interface): ...

class UsersSource:
    """
    >>> from plone.app.vocabularies.tests.base import create_context
    >>> from plone.app.vocabularies.tests.base import DummyTool

    >>> context = create_context()

    >>> tool = DummyTool('acl_users')
    >>> users = ('user1', 'user2')
    >>> def getUserById(value, default):
    ...     return value in users and value or default
    >>> tool.getUserById = getUserById
    >>> def searchUsers(fullname=None):
    ...     return [dict(userid=u) for u in users]
    >>> tool.searchUsers = searchUsers
    >>> context.acl_users = tool

    >>> source = UsersSource(context)
    >>> source
    <plone.app.vocabularies.users.UsersSource object at ...>

    >>> len(source.search(None))
    2

    >>> 'user1' in source, 'noone' in source
    (True, False)

    >>> source.get('user1'), source.get('noone')
    ('user1', None)
    """

    context: Incomplete
    users: Incomplete
    def __init__(self, context) -> None: ...
    def __contains__(self, value) -> bool:
        """Return whether the value is available in this source"""
    def search(self, query): ...
    def get(self, value): ...

class UsersSourceQueryView:
    """
    >>> from plone.app.vocabularies.tests.base import create_context
    >>> from plone.app.vocabularies.tests.base import DummyTool
    >>> from plone.app.vocabularies.tests.base import Request

    >>> context = create_context()

    >>> class User(object):
    ...     def __init__(self, id):
    ...         self.id = id
    ...
    ...     def getProperty(self, value, default):
    ...         return self.id
    ...
    ...     getId = getProperty

    >>> tool = DummyTool(\'acl_users\')
    >>> users = (\'user1\', \'user2\')
    >>> def getUserById(value, default):
    ...     return value in users and User(value) or None
    >>> tool.getUserById = getUserById
    >>> def searchUsers(fullname=None):
    ...     return [dict(userid=u) for u in users]
    >>> tool.searchUsers = searchUsers
    >>> context.acl_users = tool

    >>> source = UsersSource(context)
    >>> source
    <plone.app.vocabularies.users.UsersSource object at ...>

    >>> view = UsersSourceQueryView(source, Request())
    >>> view
    <plone.app.vocabularies.users.UsersSourceQueryView object at ...>

    >>> view.getTerm(\'user1\')
    <zope.schema.vocabulary.SimpleTerm object at ...>

    >>> view.getValue(\'user1\')
    \'user1\'

    >>> view.getValue(\'no one\')
    Traceback (most recent call last):
    ...
    LookupError: no one

    >>> template = view.render(name=\'t\')

    >>> u\'<input name="t.query" type="text" value="" />\' in template
    True

    >>> u\'<input name="t.search" type="submit" value="Search" />\' in template
    True

    >>> request = Request(form={\'t.search\' : True, \'t.query\' : \'value\'})
    >>> view = UsersSourceQueryView(source, request)
    >>> view.results(\'t\')
    [\'user1\', \'user2\']
    """

    template: Incomplete
    context: Incomplete
    request: Incomplete
    def __init__(self, context, request) -> None: ...
    def getTerm(self, value): ...
    def getValue(self, token): ...
    def render(self, name): ...
    def results(self, name): ...
