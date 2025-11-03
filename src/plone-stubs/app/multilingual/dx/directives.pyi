from _typeshed import Incomplete
from collections.abc import Generator
from plone.app.multilingual.dx.interfaces import MULTILINGUAL_KEY
from plone.supermodel.directives import CheckerPlugin
from plone.supermodel.directives import MetadataListDirective

__all__ = ["LanguageIndependentFieldsPlugin", "languageindependent"]

LANGUAGE_INDEPENDENT_KEY = MULTILINGUAL_KEY

class languageindependent(MetadataListDirective):
    """Directive used to mark one or more fields as 'languageindependent'"""

    key = LANGUAGE_INDEPENDENT_KEY
    value: str
    def factory(self, *args):
        """The languageindependent directive accepts as arguments one or more
        fieldnames (string) of fields which should be searchable.
        """

class LanguageIndependentFieldsPlugin(CheckerPlugin):
    key = LANGUAGE_INDEPENDENT_KEY
    def __call__(self) -> None: ...
    def fieldNames(self) -> Generator[Incomplete]: ...
