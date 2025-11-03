from _typeshed import Incomplete

_: Incomplete

class WorkflowsVocabulary:
    """Vocabulary factory for workflows.

    >>> from zope.component import queryUtility
    >>> from plone.app.vocabularies.tests.base import create_context
    >>> from plone.app.vocabularies.tests.base import DummyTool

    >>> name = 'plone.app.vocabularies.Workflows'
    >>> util = queryUtility(IVocabularyFactory, name)
    >>> context = create_context()

    >>> class Workflow(object):
    ...     def __init__(self, id, title):
    ...         self.id = id
    ...         self.title = title

    >>> tool = DummyTool('portal_workflow')
    >>> def values():
    ...     return (Workflow('default', 'Default Workflow'),
    ...             Workflow('intranet', 'Intranet Workflow'),
    ...             Workflow('noticias', 'Workflow de Notícias'),)
    >>> tool.values = values
    >>> context.portal_workflow = tool

    >>> workflows = util(context)
    >>> workflows
    <zope.schema.vocabulary.SimpleVocabulary object at ...>

    >>> len(workflows.by_token)
    3

    >>> intranet = workflows.by_token['intranet']
    >>> intranet.title, intranet.token, intranet.value
    (u'Intranet Workflow', 'intranet', 'intranet')

    >>> noticias = workflows.by_token['noticias']
    >>> title = 'Workflow de Notícias'
    >>> noticias.title == title
    True
    """
    def __call__(self, context): ...

WorkflowsVocabularyFactory: Incomplete

class WorkflowStatesVocabulary:
    """Vocabulary factory for workflow states.

    >>> from zope.component import queryUtility
    >>> from plone.app.vocabularies.tests.base import create_context
    >>> from plone.app.vocabularies.tests.base import DummyTool

    >>> name = 'plone.app.vocabularies.WorkflowStates'
    >>> util = queryUtility(IVocabularyFactory, name)
    >>> context = create_context()

    >>> tool = DummyTool('portal_workflow')
    >>> def listWFStatesByTitle(filter_similar=None):
    ...     return (('Private', 'private'),
    ...             ('Revisão', 'revisao'),
    ...             ('Published', 'published'))
    >>> tool.listWFStatesByTitle = listWFStatesByTitle
    >>> context.portal_workflow = tool

    >>> states = util(context)
    >>> states
    <zope.schema.vocabulary.SimpleVocabulary object at ...>

    >>> len(states.by_token)
    3

    >>> pub = states.by_token['published']
    >>> pub.title, pub.token, pub.value
    (u'Published [published]', 'published', 'published')

    >>> rev = states.by_token['revisao']
    >>> title = 'Revisão [revisao]'
    >>> rev.title == title
    True
    """
    def __call__(self, context): ...

WorkflowStatesVocabularyFactory: Incomplete

class WorkflowTransitionsVocabulary:
    """Vocabulary factory for workflow transitions

    >>> from zope.component import queryUtility
    >>> from plone.app.vocabularies.tests.base import create_context
    >>> from plone.app.vocabularies.tests.base import DummyTool

    >>> name = 'plone.app.vocabularies.WorkflowTransitions'
    >>> util = queryUtility(IVocabularyFactory, name)
    >>> context = create_context()

    >>> class Transition(object):
    ...     def __init__(self, id, actbox_name):
    ...         self.id = id
    ...         self.actbox_name = actbox_name

    >>> class TransitionsFolder(object):
    ...     def __init__(self, values):
    ...         self._values = values
    ...     def values(self):
    ...         return self._values

    >>> class Workflow(object):
    ...     def __init__(self, id, title, values):
    ...         self.id = id
    ...         self.title = title
    ...         self.transitions = TransitionsFolder(values)

    >>> tool = DummyTool('portal_workflow')
    >>> t1 = Transition('publish', 'Publish')
    >>> t2 = Transition('reject', 'Reject')
    >>> t3 = Transition('publicacao', u'Publicação')

    >>> wf1 = Workflow('default', 'Default Workflow', (t1, t2))
    >>> wf2 = Workflow('intranet', 'Intranet Workflow', (t1, ))
    >>> wf3 = Workflow('noticias', 'Workflow de Notícias', (t2, t3))

    >>> def values():
    ...     return  wf1, wf2, wf3
    >>> tool.values = values
    >>> context.portal_workflow = tool

    >>> transitions = util(context)
    >>> transitions
    <zope.schema.vocabulary.SimpleVocabulary object at ...>

    >>> len(transitions.by_token)
    3

    >>> pub = transitions.by_token['publish']
    >>> pub.title, pub.token, pub.value
    (u'Publish [publish]', 'publish', 'publish')

    >>> publ = transitions.by_token['publicacao']
    >>> publ.title == u'Publicação [publicacao]'
    True
    """
    def __call__(self, context): ...

WorkflowTransitionsVocabularyFactory: Incomplete
