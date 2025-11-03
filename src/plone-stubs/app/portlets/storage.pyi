from _typeshed import Incomplete
from OFS.SimpleItem import SimpleItem
from plone.portlets.storage import PortletAssignmentMapping as BaseMapping
from zope.container.contained import NameChooser
from zope.container.traversal import ItemTraverser

ATTEMPTS: int
category_to_name: Incomplete

class PortletAssignmentMapping(BaseMapping, SimpleItem):
    """A Zope 2 version of the default assignment mapping storage."""
    def __init__(
        self, manager: str = "", category: str = "", name: str = "", context=None
    ) -> None: ...
    @property
    def id(self): ...
    def __getitem__(self, key): ...
    def __setitem__(self, key, assignment) -> None: ...

class UserPortletAssignmentMapping(PortletAssignmentMapping):
    """An assignment mapping for user/dashboard portlets"""

class GroupDashboardPortletAssignmentMapping(PortletAssignmentMapping):
    """An assignment mapping for group dashboard portlets"""
    @property
    def id(self): ...

class PortletAssignmentMappingTraverser(ItemTraverser):
    """A traverser for portlet assignment mappings, that is acqusition-aware"""
    def publishTraverse(self, request, name): ...

class PortletsNameChooser(NameChooser):
    """A name chooser for portlets"""

    context: Incomplete
    def __init__(self, context) -> None: ...
    def chooseName(self, name, object):
        """Choose a name based on a the portlet title

        >>> from plone.app.portlets.storage import PortletAssignmentMapping
        >>> mapping = PortletAssignmentMapping()

        >>> from zope.container.interfaces import INameChooser
        >>> chooser = INameChooser(mapping)

        >>> from plone.app.portlets.portlets import base
        >>> class DummyAssignment(base.Assignment):
        ...     title = u""

        >>> dummy = DummyAssignment()
        >>> dummy.title = u"A test title"

        >>> chooser.chooseName(None, dummy)
        \'a-test-title\'

        >>> chooser.chooseName(None, dummy)
        \'a-test-title\'

        >>> mapping[u\'a-test-title\'] = dummy
        >>> chooser.chooseName(None, dummy)
        \'a-test-title-1\'

        >>> dummy.title = \'RSS: http://plone.org\'
        >>> chooser.chooseName(None, dummy)
        \'rss-http-plone-org\'

        >>> dummy.title = None
        >>> chooser.chooseName(None, dummy)
        \'dummyassignment\'

        >>> mapping[u\'dummyassignment\'] = dummy
        >>> delattr(dummy, \'title\')
        >>> chooser.chooseName(None, dummy)
        \'dummyassignment-1\'
        """
