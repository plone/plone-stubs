from _typeshed import Incomplete
from plone.app.contentrules.browser.formhelper import AddForm
from plone.app.contentrules.browser.formhelper import EditForm

class ContentWrapper:
    """
    The sole purpose of this is to transform target_folder
    values from UUID to path, which all of content rules expects
    """
    def __init__(self, content) -> None: ...
    @property
    def target_folder(self): ...
    def __getattr__(self, name, default=None): ...
    def __setattr__(self, name, value) -> None: ...

class ActionAddForm(AddForm):
    Type: Incomplete
    def create(self, data):
        """
        Since content rules expects paths, we're transforming UUID, which
        is what the z3c form widget uses, to paths.
        """

class ActionEditForm(EditForm):
    def getContent(self): ...
