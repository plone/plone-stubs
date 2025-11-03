from _typeshed import Incomplete
from plone.supermodel import model
from zope import interface
from zope.browsermenu.interfaces import IBrowserMenu
from zope.browsermenu.interfaces import IBrowserSubMenuItem

def make_relation_root_path(context): ...

class IMultilingualLayer(interface.Interface):
    """browser layer"""

class ITranslateSubMenuItem(IBrowserSubMenuItem):
    """The menu item linking to the translate menu."""

class ITranslateMenu(IBrowserMenu):
    """The translate menu."""

class ICreateTranslation(interface.Interface):
    language: Incomplete

class IUpdateLanguage(interface.Interface):
    language: Incomplete

def request_language(context): ...

class IConnectTranslation(model.Schema):
    language: Incomplete
    content: Incomplete
