from _typeshed import Incomplete
from Products.Five import BrowserView
from zope.interface import Interface

class IDexterityContent(Interface): ...

LP_TRANSLATABLE: str
portal_types_blacklist: Incomplete
logger: Incomplete

class LP2PAMView(BrowserView):
    """View for migrating multilingual catalog from LP to PAM."""

    template: Incomplete
    stepinfo: Incomplete
    results: Incomplete
    def __call__(self): ...

class LP2PAMAfterView(BrowserView):
    template: Incomplete
    stepinfo: Incomplete
    def reset_relation_catalog(self):
        """Sometimes there are dependencies to the ITranslatable interface
        hidden in the relation catalog. This reset gets rid of them. (Assuming
        that Products.LinguaPlone is already uninstalled).
        """
    total: Incomplete
    bad: Incomplete
    def __call__(self): ...

class moveContentToProperRLF(BrowserView):
    """This browser view moves the site's content to its corresponding root
    language folder and previously made a search for misplaced content through
    the site's content tree and moves them to its nearest translated parent.
    """

    template: Incomplete
    stepinfo: Incomplete
    blacklist: Incomplete
    def findContent(self, content, depth) -> None: ...
    def searchNearestTranslatedParent(self, content): ...
    results: Incomplete
    def __call__(self):
        """Note: Steps names don't correspond with the control panel ones"""
    content_tree: Incomplete
    def step1andstep2(self):
        """Explore the site's content searching for misplaced content and move
        it to its nearest translated parent.
        """
    def step3(self):
        """Move the existing site content to its correspondent RLF."""

class LP2PAMReindexLanguageIndex(BrowserView):
    template: Incomplete
    stepinfo: str
    items_before: Incomplete
    items_after: Incomplete
    def __call__(self): ...

class MigrateFolderToLRFView(BrowserView):
    def __call__(self) -> None: ...
