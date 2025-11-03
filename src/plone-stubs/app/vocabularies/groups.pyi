from _typeshed import Incomplete
from zope.interface import Interface

class ISourceQueryView(Interface): ...

class GroupsSource:
    """
    >>> from plone.app.vocabularies.tests.base import create_context
    >>> from plone.app.vocabularies.tests.base import DummyTool

    >>> context = create_context()

    >>> tool = DummyTool('acl_users')
    >>> groups = ('group1', 'group2')
    >>> def getGroupById(value, default):
    ...     return value in groups and value or default
    >>> tool.getGroupById = getGroupById
    >>> def searchGroups(name=None):
    ...     return [dict(groupid=u) for u in groups]
    >>> tool.searchGroups = searchGroups
    >>> context.acl_users = tool

    >>> source = GroupsSource(context)
    >>> source
    <plone.app.vocabularies.groups.GroupsSource object at ...>

    >>> len(source.search(''))
    2

    >>> len(source.search(u'¤'))
    2

    >>> 'group1' in source, 'noone' in source
    (True, False)

    >>> source.get('group1'), source.get('noone')
    ('group1', None)
    """

    context: Incomplete
    users: Incomplete
    def __init__(self, context) -> None: ...
    def __contains__(self, value) -> bool:
        """Return whether the value is available in this source"""
    def search(self, query): ...
    def get(self, value): ...

class GroupsSourceQueryView:
    """
    >>> from plone.app.vocabularies.tests.base import create_context
    >>> from plone.app.vocabularies.tests.base import DummyTool
    >>> from plone.app.vocabularies.tests.base import Request

    >>> context = create_context()

    >>> class Group(object):
    ...     def __init__(self, id):
    ...         self.id = id
    ...
    ...     def getProperty(self, value, default):
    ...         return self.id
    ...
    ...     getId = getProperty

    >>> tool = DummyTool(\'acl_users\')
    >>> groups = (\'group1\', \'group2\')
    >>> def getGroupById(value, default):
    ...     return value in groups and Group(value) or None
    >>> tool.getGroupById = getGroupById
    >>> def searchGroups(name=None):
    ...     return [dict(groupid=u) for u in groups]
    >>> tool.searchGroups = searchGroups
    >>> context.acl_users = tool

    >>> source = GroupsSource(context)
    >>> source
    <plone.app.vocabularies.groups.GroupsSource object at ...>

    >>> view = GroupsSourceQueryView(source, Request())
    >>> view
    <plone.app.vocabularies.groups.GroupsSourceQueryView object at ...>

    >>> view.getTerm(\'group1\')
    <zope.schema.vocabulary.SimpleTerm object at ...>

    >>> view.getValue(\'group1\')
    \'group1\'

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
    >>> view = GroupsSourceQueryView(source, request)
    >>> view.results(\'t\')
    [\'group1\', \'group2\']
    """

    template: Incomplete
    context: Incomplete
    request: Incomplete
    def __init__(self, context, request) -> None: ...
    def getTerm(self, value): ...
    def getValue(self, token): ...
    def render(self, name): ...
    def results(self, name): ...
