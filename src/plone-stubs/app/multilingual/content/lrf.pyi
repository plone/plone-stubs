from plone.app.content.namechooser import NormalizingNameChooser
from plone.dexterity.content import Container

class LRFNameChooser(NormalizingNameChooser):
    """Special name chooser to fix issue where createContentInContainer is
    used to create a new content into LRF with an id, which exists already
    in the parent folder.

    """
    def chooseName(self, name, object): ...

class LanguageRootFolder(Container):
    """LanguageRootFolder custom base class"""
