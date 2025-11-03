from _typeshed import Incomplete
from OFS.Folder import Folder

class ViewTemplateContainer(Folder):
    """a local utility storing all ttw view templates provided
    by five.customerize in a folder"""

    id: str
    title: str
    meta_type: str
    security: Incomplete
    manage_options: Incomplete
    def addTemplate(self, id, template):
        """add the given ttw view template to the container"""
